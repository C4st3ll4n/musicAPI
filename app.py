import PyMongo as PyMongo
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

import database
from deniallist import DENIALLIST

app = Flask(__name__)
app.config["MONGO_URI"] = database.url
# app.config["SQLALCHEMY_DATABASE_URI"] = database.DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "NOSQLMONGODBPYTHONFLASK"
app.config["JWT_BLACKLIST_ENABLED"] = True
api = Api(app)
jwt = JWTManager(app)
mongo = PyMongo(app)


@app.before_first_request
def init_banco():
    pass

@jwt.token_in_blacklist_loader
def check_deniallist(token):
    return token['jti'] in DENIALLIST


@jwt.revoked_token_loader
def token_invalido():
    return jsonify({"message": "revoked token"}), 401


if __name__ == "__main__":
    from sql_alchemy import db
    app.run(debug=True)
