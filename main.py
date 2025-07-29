#start a flask app 
from flask import Flask, request, jsonify, render_template,redirect, url_for
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return render_template('index.html')
# @app.route('/home')
# def home():
#     return render_template('home.html')
# @app.route('/patients',methods=['GET','POST'])
# def patients():
#     return render_template('patients.html') 
# @app.route('/doctors',methods=['GET','POST'])
# def doctors():
#     return #render_template('doctors.html')
# @app.route('/appointments',methods=['GET','POST'])
# def appointments():
#     return #render_template('appointments.html')
#run app
if __name__ == '__main__':
    app.run(port="5000",host="localhost")