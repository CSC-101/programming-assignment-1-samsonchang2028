import data
from data import Circle


# Write your functions for each part in the space below.

# Part 1
def vowel_count(words:str)->int:
    vowels = ['a','e','i','o','u','A','E','I','I','O','U'] #letter bank that will be
    # used to compare if the letter is in the list
    isvowel = [word for word in words if word in vowels] #compare list to see if there are vowels
    # from the bank that are in a word
    vowel_count = len(isvowel) #returns the vowels in a word
    return vowel_count

# Part 2
def short_lists(values:list[list[int]])->list:
    return [i for i in values if len(i) == 2] #if the length of the nested list is 2, then it will be returned

# Part 3
def ascending_pairs(values:list[list[int]])->list:
    for value in range(len(values)):
        if len(values[value]) == 2 and values[value][0] > values[value][1]: #checks if the nested list's
            # length is 2
            # if the first avlue is greater than the second in the nested list, switches
            # the values so the smaller is the first value in the nested list
            placeholder = values[value][0]
            values[value][0] = values[value][1]
            values[value][1] = placeholder

    return [value for value in values if len(value) == 2]

# Part 4
def add_prices(price1:data.Price,price2:data.Price)->data.Price:
    cents_added = price1.cents + price2.cents #adds the cents together
    dollars_added = price1.dollars + price2.dollars # adds the dollars together
    if cents_added < 100:
        return data.Price(dollars_added, cents_added)
    else:# if the cents are added and equal more than 100 cents, add 1 to the dollars count
        return data.Price(dollars_added+1, cents_added - 100)


# Part 5
def rectangle_area(inp:data.Rectangle)-> float: #finds the height and width
    # of the rectangle and finds the area by multiplying them together
    width = abs(inp.top_left.x - inp.bottom_right.x)
    height = abs(inp.top_left.y - inp.bottom_right.y)
    area = width * height
    return area


# Part 6
def books_by_author(author_name:str, books:list[data.Book])->list[data.Book]:
    return [book for book in books if author_name in book.authors]

from math import sqrt
# Part 7
def circle_bound(inp:data.Rectangle)->data.Circle:
    height = abs(inp.top_left.y - inp.bottom_right.y) #finds the height of the rectangle
    width = abs(inp.top_left.x - inp.bottom_right.x)#finds the width of the rectangle
    r1 = height//2 #finds the center of the rectangle so it can be the center of the circle
    r2 = width//2
    center = data.Point(r2,r1)
    radius = sqrt((r1**2)+(r2**2)) #finds the radius of the circle using the pythag theorem
    return data.Circle(center,radius)




# Part 8
def below_pay_average(employees:list[data.Employee])->list[str]:
    average = 0
    newList = []
    if len(employees) == 0:
        return newList
    else:
        for employee in employees: #takes the average of each
            # employees pay rate by adding each value up
            # and dividing by the number of employees
            average = average + employee.pay_rate
            average = average / len(employees)
            if employee.pay_rate < average: #adds the name to the list if the
                # pay rate is lower than the average
                newList.append(employee.name)
        return newList


