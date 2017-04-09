from abc import ABC, abstractmethod, abstractproperty
import models.setUpConnection as CD


class IPlaceDao(ABC):

    @abstractmethod
    def createNewPlace(self, place):
        """

        :param place: IPlace from Resources.places
        :return:
        """
        pass

    @abstractmethod
    def getPlaces(self):
        """

        :return: List IPlaces
        """
        pass

class PlaceDao(IPlaceDao):

    def __init__(self):
        connection_data = CD.ConnectionData()
        connection_utility = CD.ConnectionUtility()
        self._connection = connection_utility.getConnection(connection_data)

    def createNewPlace(self, place):
        """

        :param place: IPlace
        :return:
        """
        with self._connection.cursor() as cursor:
            try:
                sql = '''INSERT INTO places (placeID, providerName, Adress, X, Y) VALUES (%s,%s,%s,%s,%s)'''
                values = [place.id, place.name, place.address, place.X, place.Y]
                cursor.execute(sql,values)
                return True
            except Exception as e:
                print(e)
                return False

    def getPlaces(self):
        """

        :return: List Place
        """
        with self._connection.cursor() as cursor:
            try:
                sql = '''SELECT placeID, providerName, Adress, X, Y FROM places'''
                cursor.execute(sql)
                places = cursor.fetchall()
                data = []
                for place in places:
                    place = list(place)
                    place[3] = float(place[3])
                    place[4] = float(place[4])
                    placeObject = {
                        "placeID" : place[0],
                        "prvoiderName": place[1],
                        "Adress" : place[2],
                        "X" : place[3],
                        "Y": place[4]
                    }
                    data.append(placeObject)
                return data
            except Exception as e:
                print(e)
                return "Unable to get list of places"

    def getPlaceCounts(self):
        """

        :return: List Place
        """
        with self._connection.cursor() as cursor:
            try:
                sql = '''SELECT  placeids.placeid, raw_data.providername, count(raw_data.providername) FROM raw_data  JOIN
                                (
                                SELECT placeID, providername from places
                                ) placeids
                                ON raw_data.providername = placeids.providername
                                group by raw_data.providername, placeids.placeid;'''
                cursor.execute(sql)
                places = cursor.fetchall()
                data = []
                for place in places:
                    place = list(place)
                    place[0] = int(place[0])
                    place[2] = int(place[2])
                    placeObject = {
                        "placeID" : place[0],
                        "prvoiderName": place[1],
                        "count" : place[2]
                    }
                    data.append(placeObject)
                return data
            except Exception as e:
                print(e)
                return "Unable to get list of places"


if __name__ == "__main__":
    places = PlaceDao()
    print(places.getPlaceCounts())

