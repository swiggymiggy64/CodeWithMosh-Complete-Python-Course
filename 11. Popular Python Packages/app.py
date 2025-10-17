
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

# import PyPDF2

# # with open("first.pdf", "rb") as file:
# #     reader = PyPDF2.PdfFileReader()
# #     print(reader.numPages)
# #     page = reader.getPage(0)
# #     page.rotateClockwise(90)
# #     writer = PyPDF2.PdfFileWriter()
# #     writer.addPage(page)
# #     # writer.insertPage(page, 0)
# #     with open("rotated.pdf", "wb") as output:
# #         writer.write(output)

# merger = PyPDF2.PdfFileMerger()
# file_names = ["first.pdf", "second.pdf"]
# for file_name in file_names:
#     merger.append(file_name)
# merger.write("combined.pdf")

# * Working with Excel Spreadsheets

# pipenv install openpyxl
# Change virtual env

# import openpyxl

# # wb = openpyxl.Workbook()
# wb = openpyxl.load_workbook("transactions.xlsx")
# print(wb.sheetnames)

# sheet = wb["Sheet1"]

# # wb.create_sheet("Sheet2", 0)
# # wb.remove_sheet(sheet)

# cell = sheet["a1"]
# # for row in range(1, sheet.max_row + 1):
# #     for column in range(1, sheet.max_column + 1):
# #         cell = sheet.cell(row, column)
# #         print(cell.value)

# column = sheet["a"]
# cells = sheet["a:c"]

# print(column)
# print(cells)

# sheet.append([1, 2, 3])
# # sheet.delete_cols()
# wb.save("transactions2.xlsx")

# * Command Query Separation Principle

# import openpyxl

# wb = openpyxl.load_workbook("transactions.xlsx")
# sheet = wb["Sheet1"]
# for row in range(1, 10):
#     cell = sheet.cell(row, 1)
#     print(cell.value)
# sheet.append([1, 2, 3])
# wb.save("transactions2.xlsx")

# * NumPy

# pipenv install numpy

# import numpy as np

# # # array = np.array([1, 2, 3])
# # array = np.array([[1, 2, 3], [4, 5, 6]])
# # print(array)
# # print(type(array))
# # print(array.shape)

# # array = np.zeros((3, 4), dtype=int)
# # array = np.ones((3, 4), dtype=int)
# # array = np.full((3, 4), 5, dtype=int)
# # array = np.random.random((3, 4))
# # print(array)
# # # print(array[0, 0])
# # # print(array > 0.2)
# # # print(array[array > 0.2])
# # # print(np.sum(array))
# # # print(np.floor(array))
# # # print(np.ceil(array))
# # print(np.round(array))

# # first = np.array([1, 2, 3])
# # second = np.array([1, 2, 3])
# # print(first + second)
# # print(first + 2)

# dimensions_inch = np.array([1, 2, 3])
# dimensions_cm = dimensions_inch * 2.54
# print(dimensions_cm)
