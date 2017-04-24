from abc import ABC, abstractmethod
import models.setUpConnection as CD
import models.Resources.users as Users


class IUserDao(ABC):

    @abstractmethod
    def createNewUser(self, username):
        """
        :param bed: IPlace from Resources.places
        :return:
        """
        pass

    @abstractmethod
    def getUser(self, username, password):
        """
        :return: List IBeds
        """
        pass


class UserDao(IUserDao):

    def __init__(self):
        connection_data = CD.ConnectionData()
        connection_utility = CD.ConnectionUtility()
        self._connection = connection_utility.getConnection(connection_data)

    def createNewUser(self, user):
        """
        :param bed: IBed from Resources.places
        :return:
        """
        with self._connection.cursor() as cursor:
            try:
                sql = '''INSERT INTO users (user_id, username, password, firstname, lastname, user_type) VALUES (NULL,%s,%s,%s,%s,%s)'''
                values = [user.username, user.password, user.firstname, user.lastname, user.user_type]
                cursor.execute(sql,values)
                return True
            except Exception as e:
                print(e)
                return str(e)

    def getUser(self, username, password):
        """
        :return: List IBeds
        """
        with self._connection.cursor() as cursor:
            try:
                sql = '''SELECT * from users WHERE username = (%s) and password = (%s) '''
                values = [username, password]
                cursor.execute(sql, values)
                users = cursor.fetchall()
                data = []
                for user in users:
                    user = list(user)
                    user[0] = int(user[0])
                    user[5] = int(user[5])
                    userObject = {
                        "user_id": user[0],
                        "username": user[1],
                        "password": user[2],
                        "firstname": user[3],
                        "lastname": user[4],
                        "user_type": user[5]
                    }
                    data.append(userObject)
                return data
            except Exception as e:
                print(e)
                return str(e)


if __name__ == "__main__":
    new_user = Users.User('NULL', 'admin', 'password', 'John', 'Doe', 1)
    users = UserDao()
    print(users.createNewUser(new_user))
    print(users.getUser('admin', "password"))
