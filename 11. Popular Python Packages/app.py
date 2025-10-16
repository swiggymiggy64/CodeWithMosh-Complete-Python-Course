
# * Introduction

# * What are APIs
# Application Programming Interface

# * Yelp API

# * Searching for Businesses

# pipenv install requests
# Change Virtual Env to new one

# import requests
# # Should be Yelp URL but im not creating an API, just following along.
# url = ""
# api_key = ""
# headers = {
#     "Authorization": "Bearer" + api_key
# }
# params = {
#     "term": "barber",
#     "location": "NYC"
# }
# response = requests.get(url, headers=headers, params=params)
# businesses = response.json()["businesses"]
# names = [business["name"]
#          for business in businesses if business["rating"] > 4.5]
# print(names)

# * Hiding the API Keys
# import config

# config.api_key

# * Sending Text Messages

# mkdir PyText
# pipenv install twilio
# Change Virtual Env to new one

# from twilio import Client

# account_sid = ""
# auth_token = ""
# client = Client(account_sid, auth_token)

# call = client.messages.create(
#     to="..."
#     from_="..."
#     body="Message goes here"
# )

# * Web Scraping

# pipenv install beautifulsoup4
# pipenv install requests
# Change Virtual Env to new one

# import requests
# from bs4 import BeautifulSoup

# url = ""
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# questions = soup.select(".question-summary")
# # print(type(questions[0].get("id", 0)))
# # print(questions[0].select(".question-hyperlink")))
# for question in questions:
#     print(question.select_one(".question-hyperlink").getText())
#     print(question.select_one(".vote-count-post").getText())

# * Browser Automation

# pipenv install selenium
# pipenv install requests
# Change Virtual Env to new one
# Download Selenium drivers

# from selenium import webdriver

# browser = webdriver.Chrome()
# url = ""
# browser.get(url)

# signin_link = browser.find_element_by_link_text("Sign in")
# signin_link.click()

# username_box = browser.find_element_by_id("login_field")
# username_box.send_keys("ninjacoder22")

# password_box = browser.find_element_by_id("password")
# password_box .send_keys("todayismonday1")
# password_box.submit()

# assert "ninjacoder22" in browser.page_source

# profile_link = browser.find_element_by_class_name("user_profile-link")
# link_label = profile_link.get_attribute("innerHTML")

# assert "ninjacoder22" in link_label

# browser.quit()

# * Working with PDFs
