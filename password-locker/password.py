import random
import string
import pyperclip

class User:
    '''
    class that generate new instances of user
    '''
    user_list =[],

    def _init_(self,username,password):

         '''
         user properties
         '''
         
         self.username = username
         self.password =password

    def save_user(self):
        """
        this  method  saves a new userto the user list
        """
        User.user_list.append(self)


    def delete_user(self):
        '''
        this method deletes a user account
        '''
        User.user_list.remove(self)


    @classmethod
    def find_user(cls, username):
        '''
        this method finds username 
        '''
        for user in cls.user_list:
            if user.username == username:
                return  user

