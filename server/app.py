"""
Module Documentation Goes Here
"""
from flask import Flask, jsonify, request
from project import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) 