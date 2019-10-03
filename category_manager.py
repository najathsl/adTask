from flask import Flask, jsonify, render_template
from flaskext.mysql import MySQL
from flask import jsonify,request,make_response,url_for,redirect
from json import dumps
import simplejson as json
from flask import Response
import datetime
import hashlib
import db_connection


app = Flask(__name__)

# Category 
def load_category_list():
    conn = db_connection.connect_db()
    cursor = conn.cursor()
    responce = []
    cursor.execute("SELECT * FROM `tb_categories`")
    result = cursor.fetchall()
    crows = cursor.rowcount
    i = 0
    if(crows > 0):
        for row in result:
            #cat_id = result[i][0]
            data_arr = {'id':result[i][0],'title':result[i][1]}
            responce.append(data_arr)
            
            i = i + 1
        response_arr = {'success':'success','category_data':responce,'massage':''+str(crows)+' Items Available.'}
    else:
        response_arr = {'success':'false','category_data':responce,'massage':''+str(crows)+' Items Available.'}

    return response_arr









#Products - Loading products 
#catId,catName,fl_catid

def load_product_list():
    conn = db_connection.connect_db()
    cursor = conn.cursor()
    responce = []
    #SELECT * FROM `tb_products` INNER JOIN tb_categories ON tb_products.fl_catid = tb_categories.fl_catid
    cursor.execute("SELECT tb_products.prdtId,tb_products.prdName,tb_categories.fl_catid,tb_categories.fl_catname FROM `tb_products` INNER JOIN tb_categories ON tb_products.fl_catid = tb_categories.fl_catid")
    result = cursor.fetchall()
    crows = cursor.rowcount
    i = 0
    if(crows > 0):
        for row in result:
            #cat_id = result[i][0]
            data_arr = {'prdId':result[i][0],'prdName':result[i][1],'catid':result[i][2],'catName':result[i][3]}
            responce.append(data_arr)
            
            i = i + 1
        response_arr = {'success':'success','category_data':responce,'massage':''+str(crows)+' Items Available.'}
    else:
        response_arr = {'success':'false','category_data':responce,'massage':''+str(crows)+' Items Available.'}

    return response_arr



    #load_user_list
    #SELECT `uid`, `uName`, `uPass`, `add_allowed`, `update_allowed`, `delete_allowed` FROM `tb_users` WHERE 1

def load_user_list():
    conn = db_connection.connect_db()
    cursor = conn.cursor()
    responce = []
    cursor.execute("SELECT * FROM `tb_users`")
    result = cursor.fetchall()
    crows = cursor.rowcount
    i = 0
    if(crows > 0):
        for row in result:
            data_arr = {'uID':result[i][0],'uName':result[i][1],'uPass':result[i][2],'add_y':result[i][3],'update_y':result[i][4],'delete_y':result[i][5]}
            responce.append(data_arr)
            
            i = i + 1
        response_arr = {'success':'success','category_data':responce,'massage':''+str(crows)+' Items Available.'}
    else:
        response_arr = {'success':'false','category_data':responce,'massage':''+str(crows)+' Items Available.'}

    return response_arr


# save new Cat
def cat_save(valcategory_desc):
    conn = db_connection.connect_db()
    cursor = conn.cursor()
    try:
        
        cursor.execute("INSERT INTO tb_categories (fl_catname) VALUES ('" + valcategory_desc + "')")
        conn.commit()
    except Exception as e:
        error_massage = str(e)
        error_response = {'success':'false','massage':'Database error occured.'+str(error_massage)}
        return error_response
    else:
        response = {'success':'success','massage':'Data Inserted successfully.'}
            
    return response





# save new Product_new -- Evening
#INSERT INTO `tb_products`(`prdtId`, `prdName`, `fl_catid`) VALUES ([value-1],[value-2],[value-3])
#txtprd_desc

def prd_save(valproduct_desc,txtcat_id):
    conn = db_connection.connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO tb_products (prdName,fl_catid) VALUES ('" + valproduct_desc + "'," + txtcat_id + ")")
        conn.commit()
    except Exception as e:
        error_massage = str(e)
        error_response = {'success':'false','massage':'Database error occured.'+str(error_massage)}
        return error_response
    else:
        response = {'success':'success','massage':'Data Inserted successfully.'}
            
    return response



    
# save new USERS -- Evening
# INSERT INTO `tb_users`(`uid`, `uName`, `uPass`, `add_allowed`, `update_allowed`, `delete_allowed`) VALUES ([value-1],[value-2],[value-3],[value-4],[value-5],[value-6])
# valtxtusername,valtxtpassword,valchkadd,valchkupdate,valchkdelete

#def user_save(valtxtusername,valtxtpassword,valchkadd,valchkupdate,valchkdelete):

def user_save(valtxtusername,valtxtpassword,valchkadd,valchkupdate,valchkdelete):
    conn = db_connection.connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO tb_users (uName,uPass,add_allowed,update_allowed,delete_allowed) VALUES ('" + valtxtusername + "','" + valtxtpassword + "'," + valchkadd + "," + valchkupdate + "," + valchkdelete + ")")
        conn.commit()
    except Exception as e:
        error_massage = str(e)
        error_response = {'success':'false','massage':'Database error occured.'+str(error_massage)}
        return error_response
    else:
        response = {'success':'success','massage':'Data Inserted successfully.'}
            
    return response

def delete_cat(cat_delete):
    response = []
    conn = db_connection.connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM tb_categories WHERE fl_catid='"+cat_delete+"'")
        conn.commit()
    except Exception as e:
        error_massage = str(e)
        error_response = {'success':'false','massage':'Database error occured.'+str(error_massage)}
        return error_response
    else:
        response = {'success':'success','massage':'Item Deleted successfully.'}
            
    return response

def delete_prod(p_id):
    response = []
    conn = db_connection.connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM tb_products WHERE prdtId='"+p_id+"'")
        conn.commit()
    except Exception as e:
        error_massage = str(e)
        error_response = {'success':'false','massage':'Database error occured.'+str(error_massage)}
        return error_response
    else:
        response = {'success':'success','massage':'Item Deleted successfully.'}
            
    return response