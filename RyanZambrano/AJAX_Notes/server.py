from flask import Flask, render_template, request, redirect
from connection import MySQLConnector

# CONSTANTS
app = Flask(__name__)
mysql = MySQLConnector(app, 'AJAX_Notes')

# ROUTING
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/notes/create', methods=['POST'])
def create():
	query = "INSERT INTO notes (title, created_at, updated_at) VALUES (:title, NOW(), NOW())"
	data = {
		'title': request.form['title']
	}
	mysql.query_db(query, data)

	return redirect('/notes')

@app.route('/notes/<id>/update', methods=['POST'])
def update(id):
	query = "UPDATE notes SET description = :description WHERE id = :id"
	data = {
		'description': request.form['description'],
		'id': id
	}
	mysql.query_db(query, data)

	return redirect('/notes')

@app.route('/notes/<id>/destroy')
def destroy(id):
	query = "DELETE FROM notes WHERE id = :id"
	data = {
		'id' : id
	}
	mysql.query_db(query, data)

	return redirect('/notes')

@app.route('/notes')
def notes():
	all_notes = mysql.query_db("SELECT * FROM notes")
	return render_template('partials/notes.html', all_notes=all_notes)

app.run(debug=True)