# Score API here
from flask import Blueprint, request
import sys, jwt
from db import db
sys.path.append("../")

auth_api = Blueprint("auth", __name__)

@auth_api.route("/register", methods = ["POST"])
def register():
    content = request.get_json()
    try:
        # Check if username is provided
        userName = content["userName"]
    except KeyError:
        return {"status": "fail", "message": "no userName"}
    try:
        # Check if password is provided
        passwordHash = content["passwordHash"]
    except KeyError:
        return {"status": "fail", "message": "no password"}
    
    credentials.append(
        {
            "userName": userName,
            "passwordHash": passwordHash
        }
    )
    return {"status": "success", "message": "registered successfully"}

@auth_api.route("/login", methods = ["POST"])
def login():
    content = request.get_json()
    try:
        # Check if username is provided
        userName = content["userName"]
    except KeyError:
        return {"status": "fail", "message": "no userName"}
    try:
        # Check if password is provided
        passwordHash = content["passwordHash"]
    except KeyError:
        return {"status": "fail", "message": "no password"}
    
    try:
        #Check for username and password in my dictionary
        exists = credentials[userName] == passwordHash
    except KeyError:
        return {"status": "fail", "message": "password is wrong"}
    if exists:
        token = jwt.encode({
            "userName": userName,
            "passwordHash": passwordHash
        })
        return {"status": "success", 
        "message": {
            "userName": userName,
            "passwordHash": passwordHash,
            "createdAt": 
        }}
    else:
        return {"status": "fail", "message": "username is wrong"}
