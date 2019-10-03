from flask import Flask, jsonify, render_template
from flaskext.mysql import MySQL
from flask import jsonify,request,make_response,url_for,redirect,session
from json import dumps
import simplejson as json
from flask import Response
import datetime
import hashlib
import db_connection


app = Flask(__name__)


def check_user(username,password):
    conn = db_connection.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT uid FROM tb_users WHERE uName = '"+username+"' AND uPass = '"+password+"'")
    result = cursor.fetchall()
    crows = cursor.rowcount

    session['logged_in'] = True
    session['user_id'] = result[0][0]


    #if(crows > 0):
        #session['logged_in'] = True
        #session['user_id'] = result[0][0]
    #else:
        #return redirect(url_for('login_user'))


    
    return crows

def get_privillages(user_id):
    conn = db_connection.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT uid,add_allowed,update_allowed,delete_allowed FROM tb_users WHERE uid = '"+str(user_id)+"'")
    result = cursor.fetchall()
    
    response = {'user_id':result[0][0],'add_allowed':result[0][1],'update_allowed':result[0][2],'delete_allowed':result[0][3]}
    
    return response
