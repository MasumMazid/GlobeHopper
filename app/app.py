## Starting point of application
##pip install flask

from flask import Flask, request, jsonify
import countries



##Using Flask Framework
app=Flask(__name__)

##Read API

@app.get('/countries')
def getallcountries():
    return countries.getcountries()
  
  
    
@app.post('/countries')
def createcountry():
    data= request.json
    return countries.createcountry(data)




if __name__=='__main__':
    app.run(debug=True)
