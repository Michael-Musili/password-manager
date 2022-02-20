import unittest
from password import User



class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """


    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user=User("michaelmusili,mike254")#create new user

    def tearDown(self):
        '''
        clean up after each test to prevent errors
        '''
        User.user_list = []


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username, "michaelmusili")
        self.assertEqual(self.new_user.password, "mike254")
