from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify,request
from flask_session import Session
import pymongo
import json
from flask import render_template,redirect,url_for
from flask import Flask, request, render_template,redirect,url_for,flash,session
app=Flask(__name__)

myclient            =  pymongo.MongoClient("mongodb://localhost:27017/")
mydb                =  myclient['Template']
test                =  mydb['test']


@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/insert",methods=['POST'])
def insert():
    if request.method=='POST':
        _json   =request.form
        Name    =_json['name']
        Email   =_json['email']
        Subject =_json['subject']
        Message =_json['message']
        print(Name,Email,Subject,Message)
        if Name and Email and Subject and Message and request.method=='POST':
            test.insert_one({'name':Name,'email':Email,'subject':Subject,'message':Message})
        #return redirect(url_for('insert'))
        return 'OK',200

app.run(debug=True)