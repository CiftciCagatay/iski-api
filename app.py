# -*- coding: utf-8 -*-
# API
import pickle
from flask import Flask
from flask import request
from flask_cors import CORS
import requests
import json
from flask import jsonify

filename = 'model.sav'
app_id = "2dd42896-f1dd-4cad-b867-cbcc05b9aaea"
api_key = "M2NlYjA0YmQtNDU1My00YWUzLWI1ZDEtZTYwNTcwMDUwYjc0"
t = 0.2

model = pickle.load(open(filename, 'rb'))
app = Flask(__name__)
guncel = 0.0

CORS(app)

@app.route('/guncel', methods=['GET'])
def guncel():
    return jsonify({ "guncel": guncel })

@app.route('/fault', methods=['POST'])
def fault():
    sendPush(request.json['ilce'] + " ilçesinde " + request.json['baslangic'] + " ile " + request.json['bitis'] + " tarihleri arası " + request.json['sebep'] + " sebebiyle sular kesik olacaktır. Bilginize.")
    return "OK"

@app.route('/predict', methods=['POST'])
def predictValue():
    value = request.json['value']
    hourOfWeek = request.json['hourOfWeek']
    firstValueOfWeek = request.json['firstValueOfWeek']
    
    value_pred = model.predict([hourOfWeek])[0]
    diff = (value - firstValueOfWeek) - value_pred 
    
    global guncel
    guncel = value
    
    print(guncel)
    
    print("Value sent : " + str(value))
    print("Value predicted : " + str(value_pred))
    print("Diff : " + str(diff))
    
    if diff > t:
        sendPush("Abnormal use detected")
        return jsonify({ "value_pred": value_pred, "diff": diff })
    else:
        return jsonify({ "value_pred": value_pred, "diff": diff })
    
def sendPush(message):
    header = {"Content-Type": "application/json; charset=utf-8",
          "Authorization": "Basic " + api_key}

    payload = {"app_id": app_id, "included_segments": ["All"], "contents": {"en": message}}
     
    req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
     
    print(req.status_code, req.reason)    
    
if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
