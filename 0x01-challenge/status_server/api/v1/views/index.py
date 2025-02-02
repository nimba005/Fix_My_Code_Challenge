#!/usr/bin/python3
""" Index view
"""
from flask import Flask,jsonify, make_response
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.errorhandler(404)
def not_found(error):
    """ json 404 page """
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    # Python -m api.v1.app
    app.run(host="0.0.0.0", port=5000)
