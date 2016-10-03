from flask import Flask, render_template, request, redirect, flash, session
from connection import MySQLConnector
import re

# CONSTANTS
app = Flask(__name__)
db = MySQLConnector(app, 'AJAX_Posts')
app.secret_key = 'keepitsecretkeepitsafe'

# SQL QUERIES
queries = {
	
}


# ROUTING
@app.route('/')
def index():
	return render_template('index.html')



# HELPER FUNCTIONS

app.run(debug=True)