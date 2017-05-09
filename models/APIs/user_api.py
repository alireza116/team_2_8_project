import unittest
from models.apis import usersapi


class mytestcase(unittest.testcase):
    def setup(self):
        self.api = usersapi.usersapi()

    def test_createuser(self):
        user = self.api.createnewuser("akarduni2","password","alireza","karduni",1)
        self.assertequal(user.firstname, "alireza")
        self.assertequal(user.lastname, "karduni")
        self.assertequal(user.password, "password")
        self.assertequal(user.username,"akarduni2")

    def test_save_user(self):
        user = self.api.createnewuser("akarduni3","password","alireza","karduni",1)
        result = self.api.savenewuser(user)
        self.assertequal(result,true)

    def test_duplicate_user(self):
        user = self.api.createnewuser("akarduni2","password","alireza","karduni",1)
        result = self.api.savenewuser(user)
        self.assertequal(result,false)

    def test_get_username(self):
        login = self.api.getusers("akarduni2","password")
        self.assertequal(len(login),1)

    def test_wrong_password(self):
        login = self.api.getusers("akarduni2","password2")
        self.assertequal(len(login),0)

if __name__ == '__main__':
    unittest.main()
