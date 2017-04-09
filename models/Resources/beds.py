from abc import ABC, abstractmethod, abstractproperty

class IBed(ABC):
    """
    abstract class for homless shelter places
    """

    @property
    @abstractproperty
    def bed_id(self):
        pass

    @property
    @abstractproperty
    def geust_id(self):
        pass

    @property
    @abstractproperty
    def placeid(self):
        pass

    @property
    @abstractproperty
    def availability(self):
        pass

    @abstractmethod
    def set_guest(self,new_guest_id):
        pass

    @abstractmethod
    def remove_guest(self):
        pass



class Bed(IBed):

    def __init__(self, bed_id, guest_id, placeid, availability):
        self._bed_id = bed_id
        self._guest_id = guest_id
        self._place_id = placeid
        self._availability = availability

    @property
    def bed_id(self):
        return self._bed_id

    @property
    def guest_id(self):
        return self._guest_id

    @property
    def placeid(self):
        return self._place_id

    @property
    def availability(self):
        return self._availability


    def set_guest(self,new_guest_id):
        self._guest_id = new_guest_id
        self._availability = False


    def remove_guest(self):
        self._guest_id = None
        self._availability = True




