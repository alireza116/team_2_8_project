from abc import ABC, abstractmethod, abstractproperty


class IUser(ABC):
    """
    abstract class for homeless shelter site admin
    """

    @property
    @abstractproperty
    def user_id(self):
        pass

    @property
    @abstractproperty
    def username(self):
        pass

    @property
    @abstractproperty
    def password(self):
        pass

    @property
    @abstractproperty
    def firstname(self):
        pass

    @abstractmethod
    def lastname(self):
        pass

    @abstractmethod
    def user_type(self):
        pass


class User(IUser):

    def __init__(self, user_id, username, password, firstname, lastname, user_type):
        self._user_id = user_id
        self._username = username
        self._password = password
        self._firstname = firstname
        self._lastname = lastname
        self._user_type = user_type

    @property
    def user_id(self):
        return self._user_id

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname

    @property
    def user_type(self):
        return self._user_type


