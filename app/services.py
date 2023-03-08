#Define all services for Country and City
from flask import Flask, request, jsonify
import conn

##Get All countries from db



def allCountries():
    
    conn.mydb._open_connection()
    mycursor=conn.mydb.cursor()
    mycursor.execute("select * from country")
    results= mycursor.fetchall()
    conn.mydb.close()
    return results


def createCountry(data):
    
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
  
