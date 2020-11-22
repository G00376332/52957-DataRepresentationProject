# Server python solution to Baltic Berry database

from flask import Flask, url_for, jsonify, session, make_response, request, abort, render_template, redirect
from BalticDao import balticDao

# Create the Flask app
app = Flask(__name__,
            static_url_path='',
            static_folder='templates')