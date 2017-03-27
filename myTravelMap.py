from flask import Flask, render_template, url_for
from flask_mysqldb import MySQL
import config

app = Flask(__name__)
mysql = MySQL(app)

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = config.db_password
app.config['MYSQL_DB'] = 'TravelMap'
app.config['MYSQL_HOST'] = 'localhost'

@app.route("/test")
def hello():
	return "Welcome to My TravelMap!"

@app.route("/")
def file():
	# creating a database cursor.
	cur = mysql.connection.cursor()

	# Collecting all the entries from database into a python object.
	cur.execute('''SELECT * FROM TravelMap.PHOTOS''')
	photos = cur.fetchall()

	# Rendering map html page with the database entries object.
 	return render_template("map.html", photos = photos)

if __name__ == "__main__":
	app.run(port=5000,debug=True)
