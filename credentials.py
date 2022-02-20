import pyperclip


class Credentials:
    '''
    class that creates instaces of user accounts
    '''
    credentials_list = [] 

    def __init__(self, account , email , passlock):
        '''
        method that assigns value to credentials
        '''
    
        self.account = account
        self.email = email
        self.passlock = passlock

    def setUp(self):
        """
        Method that runs before each individual credentials test methods run.

        """
        self.new_credential = Credentials('Gmail','michaelmusili','mike254')


    def delete_credentials(self):
        """
        method to delete credentials 
         """
        Credentials.cred_list.remove(self)  

    @classmethod
    def find_account(cls, account):
        '''
        test to search for accounts
        '''
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return credentials

                
                  

    # def test_init(self):
    #     """
    #     Test case to check if a new Credentials instance has been initialized correctly
    #     """
    #     self.assertEqual(self.new_credential.account,'Gmail')
    #     self.assertEqual(self.new_credential.userName,"michaelmusili")
    #     self.assertEqual(self.new_credential.password,'mike254')
