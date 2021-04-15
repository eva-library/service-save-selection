#Guardar seleccion
import json
import requests
import logging.config
import sys
import os
import sqlite3
from flask import Flask, request, jsonify
from itertools import cycle
app = Flask(__name__)

class Service:    
    def __init__(self):
        print("BBDD")

    def saveSelection(self):
        # arrangement of items specified in the EVA flow
        items =     [["ITEM_NAME","ITEM_DESCRIPTION"],
                     ["ITEM_NAME","ITEM_DESCRIPTION"],
                     ["ITEM_NAME","ITEM_DESCRIPTION"],
                     ["ITEM_NAME","ITEM_DESCRIPTION"],
                     ["ITEM_NAME","ITEM_DESCRIPTION"]]
        try:
            # We save in a variable the request that comes from eva
            variable_request = request.json
            name_variable_request = variable_request["openContext"]["VARIABLE_REQUEST"]
            checker = True
            # logical operator that checks if there is a previous arrangement in the list of articles
            if 'selectedMaterialsList' in variable_request['hiddenContext']:
                materials = variable_request['hiddenContext']['selectedMaterialsList']
                for i in range(len(materials)):
                    if name_variable_request in materiales[i]['name_variable_request']:
                        checker = False
                        break
            index = 0 #Index Allows you to verify in the position found in the array, -1 means that the article does not exist within the array.
            # check if the name that comes from the request is contained in the items array
            for i in range(len(items)):
                if items[i][0] == name_varible_request:
                    cantidad = 1
                    name_variable_request = items[i][1]
                    name_variable_request = items[i][0]
                    index = i
                    break
                else:
                    index = -1
            # answer to be returned in eva format
            result = {
                "openContext": name_variable_request['openContext'],
                "visibleContext": name_variable_request['visibleContext'],
                "hiddenContext": name_variable_request['hiddenContext'],
                # the option variable registered in this answer will be read by eva to take a path as a service cell
                "option" : "OPCION_EVA"
            }
            # verifies that if there is no list created of the items it will create them with the name "selectMaterialsList" with the format corresponding to eva
            if index != -1 and checker:
                    if 'selectedMaterialsList' in result['hiddenContext']:
                        result['hiddenContext']['selectedMaterialsList'].append({
                            "name_variable_request": variable_items,
                            "name_attribute": variable_items,
                            "name_attribute": variable_items
                        })
                    else :
                        result['hiddenContext']['selectedMaterialsList'] = [
                            {
                            "name_variable_request": variable_items,
                            "name_attribute": variable_items,
                            "name_attribute": variable_items
                            }
                        ]
            # returns in JSON format the response in eva format
            return result

        # If any error happens, this is the answer with the formatvo eva
        except:
            result = {
                "openContext":{},
                "visibleContext":{},
                "hiddenContext":{},
                # It will return the ERROR response in the option variable
                "option" : "ERROR"
            }
            # returns in JSON format the response in eva format
            return result


@app.route("/save_selection", methods=["POST"])

def test_functions(self):
    service = Service()    
    return service.saveSelection()
    
if __name__ == "__main__":
    app.run(debug=True, port=8002, ssl_context='adhoc')
    