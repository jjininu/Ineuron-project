from flask import Flask, render_template,request
import numpy as np
import pickle

from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier,RandomForestRegressor,GradientBoostingRegressor,AdaBoostClassifier,AdaBoostRegressor

import pickle





app  = Flask(__name__)

@ app.route('/',methods = ["GET","POST"])
def home_page():
    return render_template('index.html')

@ app.route("/outcome",methods = ["GET","POST"])
def outcome():
    Temperature = request.form["Temperature"]
    RH = request.form["RH"]
    Ws= request.form["Ws"]
    Rain = request.form["Rain"]
    FFMC = request.form["FFMC"]
    DMC= request.form["DMC"]
    DC = request.form["DC"]
    ISI= request.form["ISI"]
    FWI= request.form["FWI"]

    features = [float(x) for x in request.form.values()]
    arr  = np.array(features)
    arrs = arr.reshape(1, -1)
    loaded_model = pickle.load(open("model_cls.pkl", 'rb'))
    predict  =loaded_model.predict(arrs)
    if predict[0] == 1:
        return render_template("index.html", prediction_text="There is a possibility of forest fire.")
    else:
        return render_template("index.html", prediction_text="There is a possibility of forest fire.")




if __name__ == '__main__':
    app.run(debug=True)