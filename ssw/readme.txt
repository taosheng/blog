
(1) gather user request from web
(2) fill up single user config file 
    name = ''
    email = ''
    urls = [] should be 3
    cronstring = ''
(3) tool to create User setting (TBD? maybe not necessary)
    (3.1) create folder /var/www/html/ss/<username>/<date>
   
(4) ssw.py
     (4.1) create user daily folder
     (4.2) do snapshoot by call cap.js
     (4.3) send email by zohoemail.py
(5) TODO: setup cronjob
 
     
