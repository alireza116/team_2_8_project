import unittest
import models.setUpConnection as setUpConnection

class MyTestCase(unittest.TestCase):

    def test_connection_data(self):
        connectionData = setUpConnection.ConnectionData()
        try:
            self.assertEqual(connectionData.password, "")
            self.assertEqual(connectionData.user_name,"root")
            self.assertEqual(connectionData.db_name, "hmis")
            self.assertEqual(connectionData.db_host, "localhost")
        except Exception as e:
            print(e)

    def test_connection(self):
        connection_data = setUpConnection.ConnectionData()
        connection_utility = setUpConnection.ConnectionUtility
        connection = connection_utility.getConnection(connection_data)

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM places"
            cursor.execute(sql)
            results = cursor.fetchall()
            self.assertEqual(len(results), 17)

if __name__ == '__main__':
    unittest.main()
