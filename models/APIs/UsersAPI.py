from models.DAOs import UserDao
from models.Resources import users


class UsersApi():
    def __init__(self):
        self._users_Dao = UserDao.UserDao()

    def createNewUser(self, username, password, firstname, lastname, user_type):
        newUser = users.User('NULL', username, password, firstname, lastname, user_type)
        return newUser

    def getUsers(self, username, password):
        result = self._users_Dao.getUser(username, password)
        return result
