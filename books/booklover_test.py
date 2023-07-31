import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        expected = True
        testValue = test_object.has_read("War of the Worlds")
        # unittest.TestCase brings in the assertEqual() method
        self.assertEqual(testValue, expected)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("War of the Worlds", 4)
        
        testValue = test_object.num_books_read()
        expected = 1
        
        self.assertEqual(testValue, expected)

                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Frindle", 2)
        testValue = test_object.has_read("War of the Worlds")
        # error message in case if test case got failed
        message = "Test value is not false."
        # assetFalse() to check test value as false
        self.assertTrue( testValue, message)
        
    def test_4_has_read(self): 
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Frindle", 2)
        testValue = test_object.has_read("War and Peace")
        # error message in case if test case got failed
        message = "Test value is not false."
        # assetFalse() to check test value as false
        self.assertFalse( testValue, message)
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        
    def test_5_num_books_read(self): 
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Frindle", 2)
        # add some books to the list, and test num_books matches expected.
        firstValue = test_object.num_books_read()
        secondValue = 2
        # error message in case if test case got failed
        message = "First value and second value are not equal !"
        # assertEqual() to check equality of first & second value
        self.assertEqual(firstValue, secondValue, message)

    def test_6_fav_books(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Frindle", 2)
        test_object.add_book("Atomic Habits", 3)
        test_object.add_book("War and Peace", 1)
        test_object.add_book("Divergent", 5)
        self.assertTrue(all(x>3) for x in test_object.fav_books()['book_rating'])
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
    
    
    