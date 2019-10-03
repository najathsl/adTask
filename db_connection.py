from flask import Flask
from flaskext.mysql import MySQL
from flask import jsonify,request,make_response,url_for,redirect

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'ad_task'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

def connect_db():
    conn = mysql.connect() 
    return conn