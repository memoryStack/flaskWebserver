from flask import Flask, request, render_template, redirect, url_for, send_file
from flask import send_from_directory, flash ,current_app
from werkzeug import secure_filename
import os, logging
import os.path
import sys

app = Flask(__name__)

my_file = '/var/www/html/TodoList.txt'

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/add_todo", methods=['GET', 'POST'])
def upload_file():	
	item = request.args.get("todoItem")
	if not item:
		logging.exception('pls add a item')
		return redirect(request.url)
	file = open(my_file, "a")
	file.write(item)
	file.write("\n")
	file.close()
	return 'item added'

@app.route("/display_todo", methods=['GET', 'POST'])
def display_file():
	dictionary = dict()
	file = open(my_file)
	line = file.readline()
	noOfLines = 0
	
	while line:
		dictionary[noOfLines] = line
		noOfLines = noOfLines + 1	
		line = file.readline()
	file.close()
	return render_template('displayTodo.html', dictionary=dictionary)

if __name__ == '__main__':
 	app.run(port=5000, debug=True)

