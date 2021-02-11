import mysql.connector

def isPasswordAdmin(password, dbConnection):
    dbCursor = dbConnection.cursor()
    
    dbCursor.execute(   "SELECT * "
                        "FROM permission "
                        "WHERE password = %s AND role = 'admin'", (password, ))
    passwords = dbCursor.fetchall()
    dbCursor.close()

    return passwords

def openConnection(databaseYamlData):
    return mysql.connector.connect(
        host = databaseYamlData['host'],
        user = databaseYamlData['user'],
        password = databaseYamlData['password'],
        database = databaseYamlData['database']
    )

def closeConnection(dbConnection):
    dbConnection.close()