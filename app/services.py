#Define all services for Country and City
from flask import Flask, request, jsonify
import conn

##Get All countries from db



def allcountries():
    
    conn.mydb._open_connection()
    mycursor=conn.mydb.cursor()
    mycursor.execute("select * from country")
    results= mycursor.fetchall()
    conn.mydb.close()
    return results


def createcountry(data):
    
    conn.mydb._open_connection()
    mycursor=conn.mydb.cursor()

    countryId=data['CountryID']
    Name=data['Name']
    Population=data['Population']
    continent=data['Continent']

    mysql=("INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (%s,%s,%s,%s);")
    values=(countryId,Name,countryId,continent)
    
   
    mycursor.execute(mysql,values) 
    conn.mydb.close()
    
def deletecountry(country_id):
    
    conn.mydb._open_connection()
    mycursor=conn.mydb.cursor()
    values=[country_id]
    mysql=("DELETE FROM Country WHERE  CountryId = %s")
    
   
    mycursor.execute(mysql,(values)) 
    conn.mydb.close()
  
def getContinentContries(continent):
    conn.mydb._open_connection()
    mycursor=conn.mydb.cursor()
    
    values=[continent]
    mysql=("Select * from Country WHERE  Continent = %s")
    
    mycursor.execute(mysql,(values)) 
    results= mycursor.fetchall()
    conn.mydb.close()
    return results

def getLandMarks(CityId):
    conn.mydb._open_connection()
    mycursor=conn.mydb.cursor()
    
    values=[CityId]
    mysql=("Select * from city WHERE  CityId = %s")
    
    mycursor.execute(mysql,(values)) 
    results= mycursor.fetchall()
    conn.mydb.close()
    return results
    

def getAllCities():
    conn.mydb._open_connection()
    mycursor=conn.mydb.cursor()
    mycursor.execute("select * from city")
    results= mycursor.fetchall()
    conn.mydb.close()
    return results

def deletecitybyID(city_id):
    
    conn.mydb._open_connection()
    mycursor=conn.mydb.cursor()
    values=[city_id]
    mysql=("DELETE FROM City WHERE  CountryId = %s")
    
   
    mycursor.execute(mysql,(values)) 
    conn.mydb.close()
    
def createCities(data):
    
    conn.mydb._open_connection()
    mycursor=conn.mydb.cursor()

    CityId=data['CityId']
    Name=data['Name']
    CountryId=data['CountryId']
    Capital=data['Capital']
    FirstLandmark=data['FirstLandmark']
    SecondLandmark=data['SecondLandmark']
    ThirdLandMark=data['ThirdLandMark']
    

    mysql=("INSERT INTO City (CityId, Name, CountryId, Capital, FirstLandmark, SecondLandmark, ThirdLandMark) VALUES (%s,%s,%s,%s,%s,%s,%s);")
    values=(CityId,Name,CountryId,Capital,FirstLandmark,SecondLandmark,ThirdLandMark)
    
    mycursor.execute(mysql,values) 
    conn.mydb.close()
