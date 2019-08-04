from dataStorage.userData import userData
import mysql.connector
import json

class dataAccess:        
    def saveUserData(userData):      
        userdataSets = dataAccess.getAllUserdata()

        with open('config.json') as data_file:    
            data = json.load(data_file)
            host = data["host"]
            databaseName = data["databaseName"]
            databaseUser = data["databaseUser"] 
            databasePassword = data["databasePassword"]   

        mydb = mysql.connector.connect(
            host=host,
            user=databaseUser,
            passwd=databasePassword,
            database=databaseName)
        mycursor = mydb.cursor()
        
        query = "SELECT * FROM userData WHERE ChatId = %s"    
        data = (userData.chatId,)       
        mycursor.execute(query, data) 
        rows = mycursor.fetchall()

        if len(rows) > 0:
            return False

        sql = "INSERT INTO userData (ChatId, ZipCode) VALUES (%s, %s)"
        val = (userData.chatId, userData.zipCode)
        mycursor.execute(sql, val)    
        mydb.commit()

        if mycursor.rowcount > 0:
            mycursor.close()
            return True
        else:
            mycursor.close()
            return False

    def getAllUserdata():   
        with open('config.json') as data_file:    
            data = json.load(data_file)
            host = data["host"]
            databaseName = data["databaseName"]
            databaseUser = data["databaseUser"] 
            databasePassword = data["databasePassword"]   

        mydb = mysql.connector.connect(
            host=host,
            user=databaseUser,
            passwd=databasePassword,
            database=databaseName)            
        mycursor = mydb.cursor()

        sql = "SELECT * FROM userData"
        mycursor.execute(sql)   
        rows = mycursor.fetchall()

        userDataSets = []

        for row in rows:
            userDataSets.append(userData(row[0],row[1]))

        mycursor.close()
        return userDataSets

    def deleteUserData(chatId):           
        with open('config.json') as data_file:    
            data = json.load(data_file)
            host = data["host"]
            databaseName = data["databaseName"]
            databaseUser = data["databaseUser"] 
            databasePassword = data["databasePassword"]   

        mydb = mysql.connector.connect(
            host=host,
            user=databaseUser,
            passwd=databasePassword,
            database=databaseName)            
        mycursor = mydb.cursor()

        query = "DELETE FROM userData WHERE ChatId = %s"    
        data = (chatId,)        
        mycursor.execute(query, data)      
        mydb.commit()        

        mycursor.close()


        
