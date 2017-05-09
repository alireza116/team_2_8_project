from abc import ABC, abstractmethod, abstractproperty
import models.setUpConnection as CD
import models.Resources.beds as Beds


class IBedDao(ABC):

    @abstractmethod
    def createNewBed(self, bed):
        """

        :param bed: IPlace from Resources.places
        :return:
        """
        pass

    @abstractmethod
    def getBeds(self, place_id):
        """

        :return: List IBeds
        """
        pass

    @abstractmethod
    def getAvailableBeds(self, placeid):
        pass

    @abstractmethod
    def setNewGuest(self, bed_id, new_guest):
        pass

    @abstractmethod
    def removeGuest(self, bed_id):
        pass


class BedDao(IBedDao):

    def __init__(self):
        connection_data = CD.ConnectionData()
        connection_utility = CD.ConnectionUtility()
        self._connection = connection_utility.getConnection(connection_data)


    def createNewBed(self, bed):
        """

        :param bed: IBed from Resources.places
        :return:
        """
        with self._connection.cursor() as cursor:
            try:
                sql = '''INSERT INTO beds (placeid, guest_id, bed_id, availability) VALUES (%s,%s,%s,%s)'''
                values = [bed.placeid, bed.guest_id, bed.bed_id, bed.availability]
                cursor.execute(sql,values)
                return True
            except Exception as e:
                print(e)
                return str(e)

    def getBeds(self, placeid):
        """

        :return: List IBeds
        """
        with self._connection.cursor() as cursor:
            try:
                sql = '''SELECT * from beds WHERE placeid = (%s) '''

                cursor.execute(sql, placeid)
                beds = cursor.fetchall()
                data = []
                for bed in beds:
                    bed = list(bed)
                    bed[0] = int(bed[0])
                    bed[1] = int(bed[1])
                    bed[2] = int(bed[2])
                    availability = "no"
                    if bed[3] == 1:
                        availability = "yes"
                    bedObject = {
                        "palce_id": bed[0],
                        # "guest_id": bed[1],
                        "bed_id" : bed[2],
                        "Availability" : availability
                    }
                    data.append(bedObject)
                return data
            except Exception as e:
                print(e)
                return str(e)

    def getAvailableBeds(self, placeid):
        with self._connection.cursor() as cursor:
            try:
                sql = '''SELECT * from beds WHERE placeid = (%s) and availability = 1 '''

                cursor.execute(sql, placeid)
                beds = cursor.fetchall()
                data = []
                for bed in beds:
                    bed = list(bed)
                    bed[0] = int(bed[0])
                    bed[1] = int(bed[1])
                    bed[2] = int(bed[2])
                    bedObject = {
                        "palce_id": bed[0],
                        "guest_id": bed[1],
                        "bed_id" : bed[2],
                        "Availability" : bed[3]
                    }
                    data.append(bedObject)
                return data
            except Exception as e:
                print(e)
                return str(e)

    def setNewGuest(self, bed_id, new_guest):
        with self._connection.cursor() as cursor:
            try:
                sql = '''UPDATE beds SET guest_id = (%s), availability = 0 WHERE bed_id = (%s) '''

                cursor.execute(sql, [new_guest, bed_id])
                return True
            except Exception as e:
                print(e)
                return str(e)

    def removeGuest(self, bed_id, guest_id):
        with self._connection.cursor() as cursor:
            try:
                sql = '''UPDATE beds SET guest_id = -1, availability = 1 WHERE bed_id = (%s) AND guest_id = (%s) '''

                cursor.execute(sql, [bed_id, guest_id])
                sql = '''SELECT availability from beds where bed_id = (%s)'''
                cursor.execute(sql, bed_id)
                result = cursor.fetchone()[0]
                return result
            except Exception as e:
                print(e)
                return str(e)


if __name__ == "__main__":
    new_bed = Beds.Bed(999,-1,6,1)
    beds = BedDao()
    print(beds.createNewBed(new_bed))
    print(beds.getBeds(6))
    print(beds.getAvailableBeds(6))
    print(beds.setNewGuest(555,10))
    print(beds.removeGuest(10))