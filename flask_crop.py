import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn import linear_model
from flask import Flask, render_template,redirect, url_for, request
import numpy as np
import pickle
import os
import pandas
def fun2(a,b,c,d):
    opt=pd.read_csv("C:/Users/User/Documents/GitHub/9_Khichdi/recommendation/optimal.csv")
    fert=pd.read_csv("C:/Users/User/Documents/GitHub/9_Khichdi/recommendation/fertilizer_dataset.csv")
    ro=opt.loc[opt['Crop'] == d[0]]
    n=int(ro['N'])
    p=int(ro['P'])
    k=int(ro['K'])
    count =0
    if(n>a):
        count = count+10
    if (p > b):
        count+=30
    if(k>c):
        count+=50
    if(count == 0):
        return -1
    elif (count == 10):
        result="<h1>Fertilizer options are</h1></br>    %s" %("Urea, Ammonium sulphate, CAN")
    elif(count == 30):
        result="<h1>Fertilizer options are</h1></br> %s" %("ssp, tsp")
    elif(count==50):
        result="<h1>Fertilizer options are</h1></br> %s" %("MOP, SOP,DAP")
    elif(count==40):
        result="<h1>Fertilizer options are</h1></br> %s" %("urea + ssp, npk,DAP")
    elif(count == 60):
        result="<h1>Fertilizer options are</h1></br> %s" %("urea + mop, npk")
    elif(count == 80):
        result="<h1>Fertilizer options are</h1></br> %s" %("ssp+mop, npk")
    else:
        result="<h1>Fertilizer options are</h1></br> %s" %("NPK")
    return result


def fun(input1, input2,input3,input4,input5,input6,input7):
    for dirname, _, filenames in os.walk('C:/Users/User/Documents/GitHub/9_Khichdi/recommendation/Crop_recommendation.csv'):
        for filename in filenames:
            print(os.path.join(dirname, filename))
   
    df = pandas.read_csv("C:/Users/User/Documents/GitHub/9_Khichdi/recommendation/Crop_recommendation.csv")
    filename='C:/Users/User/Documents/GitHub/9_Khichdi/recommendation/finalized_model.sav'
    loaded_model=pickle.load(open(filename,'rb'))
    features=np.array([[input1,input2,input3,input4,input5,input6,input7]])
    
    crop=loaded_model.predict(features)
    result = "<h1>Crop predictor</h1></br> Crop is : %s" %(str(crop[0]))
    result2=fun2(input1,input2,input3,crop)
    return str(result)+str(result2)


    
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
def index2():
    #print(request)
    #print(request.method)
    if request.method == 'GET':
        v = int(request.args.get('N'))
        w=int(request.args.get('P'))
        x=int(request.args.get('K'))
        return str(fun2(v,w,x,1))
    else:
        v = int(request.form['N'])
        w = int(request.form['P'])
        x = int(request.form['K'])
        return str(fun2(v,w,x,1))


if __name__=="__main__":
    app.run(debug=True, port=30000)