import unittest
from user import User



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
        test_init test case to test if the user is initialized properly
        '''
        self.assertEqual(self.new_user.username, "michaelmusili")
        self.assertEqual(self.new_user.password, "mike254")

    def test_save_user(self):
        """
        test case to test if a new user has been saved into the list

        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_mutliple_users(self):
        '''
         test to check if we can save multiple users objects to our user list
        '''
        self.new_user.save_user()
        test_user = User("test", "password")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

   