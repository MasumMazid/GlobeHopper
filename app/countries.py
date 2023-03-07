##Defines all countries in Country api

from flask import Flask, request, jsonify
import services


def getCountries():
    results= services.allCountries()
    return jsonify(results)