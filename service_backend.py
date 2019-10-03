from flask import Flask, jsonify, render_template
from flaskext.mysql import MySQL
from flask import jsonify,request,make_response,url_for,redirect,session,escape
from json import dumps
import simplejson as json
from flask import Response
import datetime
import db_connection
import category_manager
import user




app = Flask(__name__)
app.secret_key = "fs34szds7zsd66zs786dd6"

# Login 
# Home
@app.route('/login-user',methods=['GET','POST'])
def login_user():
    data_arr = []
    return render_template('login.html',data=data_arr)

# Check Login
@app.route('/check-login' ,methods=['GET','POST'])
def check_login():
    username = request.form ['username']
    password = request.form ['password']
    users = user.check_user(username,password)
    if(users > 0):
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login_user'))
    

# Home
@app.route('/Home',methods=['GET','POST'])
def home():
    data_arr = []
    return render_template('home.html',data=data_arr)




# CATS - for Dropdown -------------------------------------

#----------------------- Listing Pages - With Json / Api 
# CATS
@app.route('/cat-list',methods=['GET','POST'])
def cat_list():
    data_arr = category_manager.load_category_list()
    return render_template('category_list.html',data=data_arr)

# Product List
@app.route('/prd-list',methods=['GET','POST'])
def prd_list():
    data_arr_CAT = category_manager.load_product_list()
    return render_template('product_list.html',data=data_arr_CAT)    


# User List
@app.route('/user-list',methods=['GET','POST'])
def user_list():
    data_arr_USR = category_manager.load_user_list()
    return render_template('user_list.html',data=data_arr_USR)    

# Access Denied Page
@app.route('/access-denied',methods=['GET','POST'])
def access_denied():
    data_arr_USR = category_manager.load_user_list()
    return render_template('bad_request.html',data=data_arr_USR)    


#------------------- Category ADD ---------------
# CATS
@app.route('/cat-create',methods=['GET','POST'])
def cat_create():
    user_id = session['user_id']
    data_arr = []
    result = user.get_privillages(user_id)
    if(result['add_allowed'] == 1):
        return render_template('category_add.html',data=data_arr)
    else:
        return redirect(url_for('access_denied'))
    
# CATEGORY SAVE - WEB
@app.route('/save-cat-form' ,methods=['GET','POST'])
def save_cat_form():
    valcategory_desc = request.form ['txtcategory_desc']
    category_manager.cat_save(valcategory_desc)
    return redirect(url_for('cat_list'))
    

#------------------- Product ADD---------------
# Products
@app.route('/prd_create',methods=['GET','POST'])
def prd_create():
    data_arr = []
    user_id = session['user_id']
    result = user.get_privillages(user_id)
    if(result['add_allowed'] == 1):
        return render_template('product_add.html',data=data_arr)
    else:
        return redirect(url_for('access_denied'))
    

# CATEGORY SAVE - WEB
@app.route('/save-prd-form' ,methods=['GET','POST'])
def save_prd_form():
    valproduct_desc = request.form ['txtprd_desc']
    txtcat_id = request.form ['txtcat_id']
    category_manager.prd_save(valproduct_desc,txtcat_id)
    return redirect(url_for('prd_list'))
    


#------------------- Users ADD---------------
# Products
@app.route('/user_create',methods=['GET','POST'])
def user_create():
    data_arr = []
    #function call to Check ADD / DELETE / Update 
    # have to write a new one
    return render_template('user_add.html',data=data_arr)


# Delete Category
@app.route('/cat-delete',methods=['GET','POST'])
def cat_delete():
    cat_delete = request.args.get('cat_id')
    user_id = session['user_id']
    result = user.get_privillages(user_id)
    if(result['delete_allowed'] == 1):
        res = category_manager.delete_cat(cat_delete)
        #return Response(json.dumps(res), mimetype='application/json')
        return redirect(url_for('cat_list'))
    else:
        return redirect(url_for('access_denied'))

# Delete product
@app.route('/prod-delete',methods=['GET','POST'])
def prod_delete():
    p_id = request.args.get('p_id')
    user_id = session['user_id']
    result = user.get_privillages(user_id)
    if(result['delete_allowed'] == 1):
        category_manager.delete_prod(p_id)
        return redirect(url_for('prd_list'))
    else:
        return redirect(url_for('access_denied'))

# CATEGORY SAVE - WEB
@app.route('/save-user-form' ,methods=['GET','POST'])
def save_user_form():
    valtxtusername = request.form ['txtusername']
    valtxtpassword = request.form ['txtpassword']

    #checkbox -- chkinsert chkupdate chkdelete
    valchkadd = request.form ['optinsert']
    valchkupdate = request.form ['optupdate']
    valchkdelete = request.form ['optdelete']

    #category_manager.user_save(valtxtusername,valtxtpassword,valchkadd,valchkupdate,valchkdelete)
    category_manager.user_save(valtxtusername,valtxtpassword,valchkadd,valchkupdate,valchkdelete)
    return redirect(url_for('user_list'))
    

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


# Flask App Run
app.run(host='0.0.0.0', port=4050, debug=True)