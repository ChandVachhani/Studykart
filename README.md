# StudyKart
## Purpose of this Web Application

This Application is built for exchanging book and other materials at University level. Currently book exchange is done through whatapp groups which is quiet time consuming and also variety of products is very less. In this our Web application products are sorted according to their price so buyer can find cheapest product at the top. So it makes very easy for buyer.

## Python Frameworks and APIs used

 <b>Django</b>: It is used for backend scripting with MYSQL.<br>
 <b>Selenium</b>: It is used for automated web testing of our application.<br>
 <b>Request</b>: It is used to request a web page and get data for web scrapping.<br>
 <b>Beautiful Soup</b>: It is used for web scrapping.<br>
 <b>Pandas</b>: It is used for filtering purpose in Django Admin Page.<br>

## Project Developers
#### 18BCE238
#### 18BCE249
#### 18BCE231

### Project Video
There is project description video name project_video.mp4

## How to run the Project
### Install XAMPP
Then open Xampp control panel and run mysql server.<br>
### Open Command Prompt
Enter into studykart_py folder
Then Activate Virtual Environment by enter command **venv\scripts\activate.bat**<br>
Then run command <b> python manage.py makemigrations </b> <br>
Then run command <b> python manage.py migrate </b> <br>
Keep open command prompt and follow next steps. <br>

#### Open PhpMyAdmin

In browser write <b>http://localhost/phpmyadmin</b> or in xampp control panel click <b> Admin </b> of Mysql. <br>
Then Create database named studykart. <br>
Then in studykart database click on <b>import</b> tab and choose file studykart.sql present in repository and click on <b>Go</b>. <br>
This should not give any errors. <br>
Then in command prompt run command <b> python manage.py runserver </b>. <br>
Then open link shown in command prompt. <br>

If any error comes then please contact me at 18BCE238@nirmauni.ac.in <br>
### Credentials
#### There are pre-registered buyer and seller accounts.
#### Buyer
##### Username: dss061200
##### Password: hello
#### Seller
##### Username: dss0620
##### Password: hello

<b>How Selenium Work<b><br>
 We can write some test cases for our websie and check it works parfectly or not.<br>
 In our project we use Log-In and Sin_Up test cases for test our website.<br>
 For that we need to add path of exe driver file of any brouser and then run the code.<br>
 It will open that brouser and fill that details which we given to in code and exicute and check. <br>
 Fro that we use <b>ID<b> of every html element to connect with Selenium.<br>

