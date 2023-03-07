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
