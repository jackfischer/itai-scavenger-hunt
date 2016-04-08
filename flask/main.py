import crud
import sqlite3
from flask import *

crudd = crud.Crud()
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/inject/<field>', methods=['GET', 'POST'])
def inject(field):
	print field
	query = crudd.execute(field)
	return render_template('inject.html', query=query)

app.run()
