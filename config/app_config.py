from flask import Flask, request, jsonify
from flask_cors import CORS

web_app = Flask(__name__)
CORS(web_app)
