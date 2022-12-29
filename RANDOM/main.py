from flask import Flask,request
from helper import random_number

app=Flask(__name__)

@app.route("/")
def homepage():
    return {"result" : "ok"}

@app.route("/num")
def num():
    min=request.args.get("min")
    max=request.args.get("max")
    min1=int(min)
    max1=int(max)
    return random_number(min1,max1)


