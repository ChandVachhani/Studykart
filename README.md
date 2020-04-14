# StudyKart
## Purpose of this Web Application

This Application is built for exchanging book and other materials at University level. Currently book exchange is done through whatapp groups which is quiet time consuming and also variety of products is very less. In this our Web application products are sorted according to their price so buyer can find cheapest product at the top. So it makes very easy for buyer.

## Python Frameworks and APIs used

 <b>Django</b>: It is used for backend scripting with MYSQL.
 <b>Selenium</b>: It is used for automated web testing of our application.
 <b>Request</b>: It is used to request a web page and get data for web scrapping.
 <b>Beautiful Soup</b>: It is used for web scrapping.
 <b>Pandas</b>: It is used for filtering purpose in Django Admin Page.

## Project Developers
#### 18BCE238
#### 18BCE249
#### 18BCE231

## How to run the Project
### Install XAMPP
Then open Xampp control panel and run mysql server.
### Open Command Prompt
Enter into studykart_py folder
Then Activate Virtual Environment by enter command <b> venv\scripts\activate.bat <\b>
Then run command <b> python manage.py makemigrations </b>
Then run command <b> python manage.py migrate </b>
Keep open command prompt and follow next steps.

#### Open PhpMyAdmin

In browser write <b>http://localhost/phpmyadmin</b> or in xampp control panel click <b> Admin </b> of Mysql.
Then Create database named studykart.
Then in studykart database click on <b>import</b> tab and choose file studykart.sql present in repository and click on <b>Go</b>.
This should not give any errors. 
Then in command prompt run command <b> python manage.py runserver </b>.
Then open link shown in command prompt.

If any error comes then please contact me at 18BCE238@nirmauni.ac.in
