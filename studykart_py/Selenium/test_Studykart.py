from selenium import webdriver

def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="D:/clg projects/python/studykart/selenium/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()

def test_login():
    
    driver.get("http://127.0.0.1:8000/user/")
    driver.find_element_by_id("uname").send_keys("chand4")
    driver.find_element_by_id("login-password").send_keys("chandvachhani")
    driver.find_element_by_id("btnLogin").click()
    x = driver.title
    assert x == "StudyKart"

    driver.get("http://127.0.0.1:8000/user/buyer_signup/")
    driver.find_element_by_id("fname").send_keys("test")
    driver.find_element_by_id("lname").send_keys("user")    
    driver.find_element_by_id("e-mail").send_keys("testuser@gmail.com")
    driver.find_element_by_id("mobile").send_keys("1234567891")
    driver.find_element_by_id("cuname").send_keys("testuser1")
    driver.find_element_by_id("signup-password").send_keys("StudyKart@123")
    driver.find_element_by_id("btnsup").click()
    x = driver.title
    assert x == "Log In"

def test_teardown():
    driver.close()
    driver.quit()
    print("Test Completed!")

