from selenium import webdriver

# change executable_path value to path where your chromedirver is located
driver = webdriver.Chrome(executable_path="/Users/ernesto/Downloads/chromedriver")

# make sure simple_login app is running on localhost:3000 else change value
driver.get("localhost:3000")


# ******** Test Scenarios For Simple Login *********

# driver.find_element_by_name("user[email]").send_keys("guy@mail.com")
# driver.find_element_by_name("user[password]").send_keys("123456")
# user successfully navigates to the login page
# in the log in page, user enters all input fields with valid data and clicks submit and logs in successfully and is redirected to a welcome page
# in the log in page, user enters all input fields with valid data and checks the remember me checkbox and logs in successfully
# as a signed in user, user can click the sign out link and is redirected back to the log in page
# in the login page, user enters all input fields with some invalid data and gets an alert

# in the login page, user clicks on sign up link and navigates to the sign up page successfully
links = driver.find_elements_by_xpath("//a[@href]")
links[0].click()
sign_up = driver.find_element_by_tag_name("h2").text
form = driver.find_elements_by_class_name("field")

assert "Sign up" in sign_up
assert len(form) == 3
assert "Email" in form[0].text
assert "Password (6 characters minimum)" in form[1].text
assert "Password confirmation" in form[2].text


# in the sign up page, user fills in all input fields with valid data and is redirected to a welcome page
driver.find_element_by_id("user_email").send_keys("foo@mail.com")  # make sure db doesnt have a user with same email
driver.find_element_by_id("user_password").send_keys("123456")
driver.find_element_by_id("user_password_confirmation").send_keys("123456")
driver.find_element_by_xpath("//div[@class='actions']/input").submit()
message = "Welcome! You have signed up successfully."
success_alert = driver.find_element_by_class_name("alert-success").text

assert message in success_alert


# in the sign up page, user fills in all input fields with invalid email and gets an alert
# in the sign up page, user fills in all input fields with invalid password and gets an alert
# in the sign up page, user fills in all input fields with invalid password confirmation and gets an alert
# in the sign up page, user clicks on log in link and navigates back to the log in page
# in the log in page, user clicks on forgot your password? link and is redirected to the forgot password page
# in the forgot your password page, user fills input field with valid email and gets a notification
# in the forgot your password page, user fills input field with invalid email and gets an alert
# in the forgot your password page, user clicks on log in link to navigate to the log in page
# in the forgot your password page, user clicks on sign up link to navigate to the sign up page
