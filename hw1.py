import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(words:str)->int:
    vowels = ['a','e','i','o','u','A','E','I','I','O','U']
    isvowel = [word for word in words if word in vowels]
    vowel_count = len(isvowel)
    return vowel_count

# Part 2
def short_lists(values:list[list[int]])->list:
    return [i for i in values if len(i) == 2]

# Part 3
def ascending_pairs(values:list[list[int]])->list:
    for value in range(len(values)):
        if len(values[value]) == 2 and values[value][0] > values[value][1]:
            placeholder = values[value][0]
            values[value][0] = values[value][1]
            values[value][1] = placeholder

    return [value for value in values if len(value) == 2]

# Part 4
def add_prices(price1:data.Price,price2:data.Price)->data.Price:
    pass


# Part 5
def rectangle_area(inp:data.Rectangle)->int:
    pass

# Part 6
def books_by_author(author_name:str, books:list[data.Book])->list[Book]:
    pass

# Part 7
def circle_bound(inp:data.Rectangle)->data.Circle:
    pass



# Part 8
def below_pay_average(employee:list[data.Employee])->list[str]:
    pass
