Project 
------------------
+
+ 30-9-2019 to 3-10-2019 
+ LOCAL IP CAN BE YOUR SETTING IP INSTEAD OF -> 127.0.0.1
+ CURRENT PORT ID -> 4050
++

Task has been completed usnig python , flask and mysql , clone or download the folder to pc.
setup the python enviorment setups. 



Project is developed on Python and MySql on Flask framwork 
+---------------------------------------------+

Softwares Needed
+---------------------------------------------+

Install Python
Install Flask for Python
install MySql

Database (Mysql) 
+---------------------------------------------+
Run mysql db Script in the project folder


Python 
+---------------------------------------------+
open the project and change the python file below with database credintials 
db_connection.py 



Python app run 
+---------------------------------------------+
Open the windows powershel using the SHIFT KEY inside the project folder and Run 

python service_backend.py


Python app 
+---------------------------------------------+
http://127.0.0.1:4050/login-user
(LOCAL IP CAN BE YOUR SETTING IP)

Table Structure 
+---------------------------------------------+

Made a simple structure with a 2 + table design 

-----------------------------
|tb_categories               |
|----------------------------|
|fl_catid (PK) | fl_catname  |
-----------------------------
          |
	  |
         /|\
---------------------------------------
|tb_products                           |
|--------------------------------------|
|prdtId (pk) | prdName | fl_catid (FK) |
----------------------------------------



--------------------------------------------------------------------------
|tb_users								  |
|-------------------------------------------------------------------------|
|uid (PK) | uName | uPass | add_allowed | update_allowed | delete_allowed |
|-------------------------------------------------------------------------|


Postman Links (Json )
+---------------------------------------------+

with the 
"localhost ip /prd-list"
"localhost ip /user-list"
"localhost ip /cat-list"



Task
+---------------------------------------------+

1. Product categories
2. Products which belong to some category (one product may belong to several categories)
3. Users, who can authorize

The following actions should be implemented:
1.1 Getting the list of all categories - Done 
2.1 Getting the list of products of the concrete category - Done 

3.1 Users authorization - ( Done ) 

1.2 + 3.2 Create/update/delete of category for authorized users only 
2.1 + 3.3 Create/update/delete of product for authorized users only

