import unittest
from models.APIs import UsersAPI


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.api = UsersAPI.UsersApi()

    def test_createUser(self):
        user = self.api.createNewUser("akarduni2","password","alireza","karduni",1)
        self.assertEqual(user.firstname, "alireza")
        self.assertEqual(user.lastname, "karduni")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.username,"akarduni2")

    def test_save_user(self):
        user = self.api.createNewUser("akarduni3","password","alireza","karduni",1)
        result = self.api.saveNewUser(user)
        self.assertEqual(result,True)

    def test_duplicate_user(self):
        user = self.api.createNewUser("akarduni2","password","alireza","karduni",1)
        result = self.api.saveNewUser(user)
        self.assertEqual(result,False)

    def test_get_username(self):
        login = self.api.getUsers("akarduni2","password")
        self.assertEqual(len(login),1)

    def test_wrong_password(self):
        login = self.api.getUsers("akarduni2","password2")
        self.assertEqual(len(login),0)



if __name__ == '__main__':
    unittest.main()
