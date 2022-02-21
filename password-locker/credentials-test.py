import unittest
import pyperclip
from credentials import Credentials



class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for credentials class

    """ 
    def setUp(self):
        """
        Method that runs before each individual credentials test methods run.

        """
        self.new_credential = Credentials('Gmail','michaelmusili','mike2020')
    def test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credential.account,'Gmail')
        self.assertEqual(self.new_credential.userName,'michaelmusili')
        self.assertEqual(self.new_credential.password,'mike2020')

    def test_save_credentials(self):
        '''
        save credentials
        '''  
        self.new_credential.save_credintials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def saving_multiple_credentials(self):
        '''
        a method that enables users to  store multiple credentials
        '''
        self.new_credential.save_credintials()
        test_credentials = Credentials("Twitter", "testuser","password")
        test_credentials.save_credintials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        '''
        test if you can delete credentials test
        '''
        self.new_credential.save_credintials()
        test_credentials = Credentials("Twitter", "testuser","password")
        test_credentials.save_credintials()
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)
    

    def test_search_for_credentials(self):
        '''
        test if credentials can be searched for
        '''
        self.new_credential.save_credintials()
        test_credentials = Credentials("Twitter", "testuser","password")
        test_credentials.save_credintials()
        find_credential= Credentials.find_account("Twitter")
        self.assertEqual(find_credential.account, test_credentials.account)



    def test_confirm_credentials_exists(self):
        '''
        confirm that credentials actually exists
        '''
        self.new_credential.save_credentials()
        test_credentials = Credentials("Twitter", "testuser","password")
        test_credentials.save_credintials()
        cred_exists = Credentials.cred_exists("Twitter")
        self.assertTrue(cred_exists)


      

        
    def test_display_credentials(self):
        '''
        test if all credentials can be displayed
        '''
        self.assertEqual(Credentials.display_credrentials(), Credentials.credentials_list)





    def test_copy_password(self):
        '''
        test whether generated password can be copied
        '''
        self.new_credential.save_credintials()
        Credentials.copy_passlock("mike254")
        self.assertEqual(self.new_credential.passlock, pyperclip.paste())            