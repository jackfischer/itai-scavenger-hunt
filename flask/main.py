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
	c=sqlite3.connect("schema.db").cursor()
	query = c.execute(field)
	query = str(c.fetchall())
	return render_template('inject.html', query=query)

app.run(debug=True)
