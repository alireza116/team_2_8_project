from abc import ABC, abstractmethod, abstractproperty

class IPlace(ABC):
    """
    abstract class for homless shelter places
    """

    @property
    @abstractproperty
    def name(self):
        pass


    @property
    @abstractproperty
    def id(self):
        pass


    @property
    @abstractproperty
    def X(self):
        pass


    @property
    @abstractproperty
    def Y(self):
        pass

    @property
    @abstractproperty
    def address(self):
        pass



class Place(IPlace):

    def __init__(self, id, name, address, X, Y):
        self._name = name
        self._id = id
        self._X = X
        self._Y = Y
        self._address = address

    @property
    def name(self):
        return self._name


    @property
    def id(self):
        return self._id


    @property
    def X(self):
        return self._X


    @property
    def Y(self):
        return self._Y

    @property
    def address(self):
        return self._address


