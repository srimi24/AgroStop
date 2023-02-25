import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn import linear_model
from flask import Flask, render_template,redirect, url_for, request
import numpy as np
import pickle
import os
import pandas
def fun(input1, input2,input3,input4,input5,input6,input7):
    for dirname, _, filenames in os.walk('C:/Users/User/Documents/GitHub/9_Khichdi/recommendation/Crop_recommendation.csv'):
        for filename in filenames:
            print(os.path.join(dirname, filename))
   
    df = pandas.read_csv("C:/Users/User/Documents/GitHub/9_Khichdi/recommendation/Crop_recommendation.csv")
    filename='C:/Users/User/Documents/GitHub/9_Khichdi/recommendation/finalized_model.sav'
    loaded_model=pickle.load(open(filename,'rb'))
    features=np.array([[input1,input2,input3,input4,input5,input6,input7]])
    global crop
    crop=loaded_model.predict(features)
    result = "<h1>Crop predictor</h1></br>N : %s</br>P: %s</br> Crop is : %s" %(str(input1), str(input2), str(crop[0]))
    return result

app = Flask(__name__)

#@app.route("/home")
@app.route("/crop", methods=['POST', 'GET'])
def index():
    #print(request)
    #print(request.method)
    if request.method == 'GET':
        v = int(request.args.get('N'))
        w=int(request.args.get('P'))
        x=int(request.args.get('K'))
        x2=int(request.args.get('temperature'))
        y=int(request.args.get('humidity'))
        z=int(request.args.get('pH'))
        z2=int(request.args.get('rainfall'))
        return str(fun(v,w,x,x2,y,z,z2))
    else:
        v = int(request.form['N'])
        w = int(request.form['P'])
        x = int(request.form['K'])
        x2 = int(request.form['temperature'])
        y = int(request.form['humidity'])
        z = int(request.form['pH'])
        z2 = int(request.form['rainfall'])
        return str(fun(v,w,x,x2,y,z,z2))

@app.route("/fertilizer", methods=['POST', 'GET'])
def index():
    #print(request)
    #print(request.method)
    if request.method == 'GET':
        v = int(request.args.get('N'))
        w=int(request.args.get('P'))
        x=int(request.args.get('K'))
        x2=int(request.args.get('temperature'))
        y=int(request.args.get('humidity'))
        z=int(request.args.get('pH'))
        z2=int(request.args.get('rainfall'))
        return str(fun2(v,w,x,x2,y,z,z2))
    else:
        v = int(request.form['N'])
        w = int(request.form['P'])
        x = int(request.form['K'])
        x2 = int(request.form['temperature'])
        y = int(request.form['humidity'])
        z = int(request.form['pH'])
        z2 = int(request.form['rainfall'])
        return str(fun2(v,w,x,x2,y,z,z2))


if __name__=="__main__":
    app.run(debug=True, port=30000)