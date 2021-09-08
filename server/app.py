"""
Module Documentation Goes Here
"""
from flask import Flask, jsonify, request
from project import create_app
import profile_controller
from db import create_tables

# Flask App Setup
app = create_app() 

@app.route('/profiles', methods=["GET"])
def get_profiles():
    profiles = profile_controller.get_profiles()
    return jsonify(profiles)

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 5000, debug = True)