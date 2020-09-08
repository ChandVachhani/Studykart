# StudyKart
## Purpose of this Web Application

This Application is built for exchanging book and other materials at University level. Currently book exchange is done through whatapp groups which is quiet time consuming and also variety of products is very less. In this our Web application products are sorted according to their price so buyer can find cheapest product at the top. So it makes very easy for buyer.

## Project Description with Images

### Front Page

<br/>

![Top of Front Page](https://github.com/ChandVachhani/Studykart/blob/master/Project_images/front_ui.png?raw=true)

<br/>

![Products in Front Page](https://github.com/ChandVachhani/Studykart/blob/master/Project_images/products_ui.png?raw=true)

#### This is Front Page of our web application with sign in card and showing available products.

<br/> <br/>

### Sign Up Page

<br/>

![Products in Front Page](https://github.com/ChandVachhani/Studykart/blob/master/Project_images/signup_ui.png?raw=true)

<br/>

#### This is sign up page where buyers and sellers can signup and can proceed further.

<br/> <br/>

### Product Search

<br/>

![Prodcut Search Page](https://github.com/ChandVachhani/Studykart/blob/master/Project_images/search_image.png?raw=true)

<br/>

#### This page shows the result of searched product available in our database.

<br/> <br/>

### Checkout Page

<br/>

![Checkout Page](https://github.com/ChandVachhani/Studykart/blob/master/Project_images/check_out_ui.png?raw=true)

<br/>

#### This page shows products we are interested in buying along with the total price and total products.

<br/> <br/>

### Wishlist Page

<br/>

![Wishlist_ui](https://github.com/ChandVachhani/Studykart/blob/master/Project_images/whishlist_ui.png?raw=true)

<br/>

#### This page shows all the products that we have wishlisted.

<br/> <br/>

### Seller's Products Page

<br/>

![Seller_products](https://github.com/ChandVachhani/Studykart/blob/master/Project_images/your_products.png?raw=true)

<br/>

#### This page shows all the products that seller has listed on our application along with the current status of each product.

<br/> <br/>

### My Orders Page

<br/>

![My_orders_page](https://github.com/ChandVachhani/Studykart/blob/master/Project_images/our_orders_ui.png?raw=true)

<br/>

#### This page shows all the products that buyer had bought and along with the status of each product.

<br/> <br/>

## Python Frameworks and APIs used

 <b>Django</b>: It is used for backend scripting with MYSQL.<br>
 <b>Selenium</b>: It is used for automated web testing of our application.<br>
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

## Selenium Web Testing
 We can write some test cases for our websie and check it works perfectly or not.<br>
 In our project we use Log-In and Sing-Up test cases for test our website.<br>
 For that we need to add path of exe driver (which is present in selenium folder of repository) file of any browser and then run the code.<br>
 It will open that browser and fill that details which we given to in code and execute and check. <br>
 For that we use <b>ID<b> of every html element to connect with Selenium.<br>

