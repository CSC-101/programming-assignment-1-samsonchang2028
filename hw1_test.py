from xmlrpc.client import Boolean

import data
import hw1
import unittest

from data import Rectangle


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        words = 'String'
        results = hw1.vowel_count(words)
        expected = 1
        self.assertEqual(expected, results)
    def test_vowel_count_2(self):
        words = 'Education'
        results = hw1.vowel_count(words)
        expected = 5
        self.assertEqual(expected, results)

    # Part 2
    def test_short_lists1(self):
        values = [[1,2],[3],[4,5,6],[7,8]]
        results = hw1.short_lists(values)
        expected = [[1,2],[7,8]]
        self.assertEqual(expected, results)

    def test_short_lists_2(self):
        values = [[9, 10], [], [1], [12, 8]]
        results = hw1.short_lists(values)
        expected = [[9, 10], [12, 8]]
        self.assertEqual(expected, results)

    # Part 3
    def test_ascending_pairs_1(self):
        values = [[1,2],[3],[4,5,6],[10,9]]
        results = hw1.ascending_pairs(values)
        expected = [[1, 2], [9, 10]]
        self.assertEqual(expected, results)
    def test_ascending_pairs_2(self):
        values = [[5,3],[8,8],[12,6],[7,9]]
        results = hw1.ascending_pairs(values)
        expected = [[3, 5], [8, 8], [6, 12], [7, 9]]
        self.assertEqual(expected, results)
    # Part 4
    def test_add_prices(self):
        price1 = data.Price(6,65)
        price2 = data.Price(3,35)
        results = hw1.add_prices(price1, price2)
        expected = data.Price(10,0)
        self.assertEqual(expected, results)
    def test_add_prices_2(self):
        price1 = data.Price(7,45)
        price2 = data.Price(4,60)
        results = hw1.add_prices(price1, price2)
        expected = data.Price(12,5)
        self.assertEqual(expected, results)
    # Part 5
    def test_rectangle_area_1(self):
        inp =data.Rectangle(data.Point(1,5),data.Point(4,1))
        results = hw1.rectangle_area(inp)
        expected = 12.0
        self.assertEqual(expected, results)
    def test_rectangle_area_2(self):
        inp =data.Rectangle(data.Point(0,0),data.Point(5,2))
        results = hw1.rectangle_area(inp)
        expected = 10.0
        self.assertEqual(expected, results)
    # Part 6
    def test_books_by_author_1(self):
        book1 = data.Book(['Rowling'],'Harry Potter 1')
        book2 = data.Book(['Rowling'],'Harry Potter 2')
        book3 = data.Book(['Tolkien'],'Hobbit')
        books = [book1,book2,book3]
        results = hw1.books_by_author('Rowling', books)
        expected = [book1, book2]
        self.assertEqual(expected, results)
    def test_books_by_author_2(self):
        book1 = data.Book(['Rowling'],'Harry Potter 7')
        book2 = data.Book(['Tolkien'],'The Lord of the Rings')
        book3 = data.Book(['Tolkien'], 'Hobbit')
        book4 = data.Book(['Rowling'], 'Harry Potter 3')
        books = [book1,book2,book3,book4]
        results = hw1.books_by_author('Rowling', books)
        expected = [book1, book4]
        self.assertEqual(expected, results)

    # Part 7
    def test_circle_bound_1(self):
        inp = Rectangle(data.Point(0,0),data.Point(6,8))
        results = hw1.circle_bound(inp)
        expected = data.Circle(data.Point(3,4),5)
        self.assertEqual(expected, results)
    def test_circle_bound_2(self):
        inp = Rectangle(data.Point(2,3),data.Point(8,10))
        results = hw1.circle_bound(inp)
        expected = data.Circle(data.Point(5,6.5),3.5)
        self.assertEqual(expected, results)
    # Part 8
    def test_below_pay_average(self):
        employees = [data.Employee('Neil', 5),
                     data.Employee('Bob', 19),
                     data.Employee('Dan', 17)]
        results = hw1.below_pay_average(employees)
        expected = ['Neil']
        self.assertEqual(expected, results)

    def test_below_pay_average_2(self):
        employees = [data.Employee('Alice', 25),
                     data.Employee('Charlie', 15),
                     data.Employee('Eve', 30)]
        results = hw1.below_pay_average(employees)
        expected = ['Charlie']
        self.assertEqual(expected, results)



if __name__ == '__main__':
    unittest.main()
