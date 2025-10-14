
# * Python Standard Library


# * Working With Paths

# from pathlib import Path

# # Path("C:\\Program Files\\Microsoft")
# # Path(r"C:\Program Files\Microsoft")  # Same as above, is a raw string so no need for double \\
# # Path("/usr/local/bin")  # Linux
# # Path()  # Current folder
# # Path("ecommerce/__init__.py")
# # Path() / Path("ecommerce")
# # Path() / "ecommerce" / "__init__.py"
# # Path.home()

# path = Path("../08. Modules/ecommerce/__init__.py")
# print(path)
# print(path.exists())
# path.is_file()
# path.is_dir()
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)

# # path = path.with_name("file.txt")
# path = path.with_suffix(".txt")
# print(path)
# print(path.absolute())

# * Working With Directories

# from pathlib import Path

# path = Path("../08. Modules/ecommerce")
# # path.exists()
# # path.mkdir()
# # path.rmdir() # remove dir
# # path.rename("../08. Modules/ecommerce2")

# # print(path.iterdir())
# # print(list(path.iterdir()))
# # print()
# # for p in path.iterdir():
# #     print(p)

# paths = [p for p in path.iterdir() if p.is_dir()]
# print(paths)
# # py_files = [p for p in path.glob("*.py")]
# py_files = [p for p in path.rglob("*.py")]
# print(py_files)

# * Working With Files

# from pathlib import Path
# from time import ctime
# import shutil

# # path = Path("../08. Modules/ecommerce/__init__.py")
# # path = Path("file.txt")

# # path.exists
# # path.rename("init.txt")
# # path.unlink()
# # print(ctime(path.stat().st_ctime))

# # path.read_bytes()

# # with open("file.txt", "r") as file:
# #     print("file opened")

# # You can straight read a file with this then doing the above
# # print(path.read_text())
# # path.write_text("Ayyy im walkin' ova here")

# source = Path("file.txt")
# target = Path("new folder") / "file.txt"

# # target.write_text(source.read_text())
# shutil.copy(source, target)  # This is same as above

# * Working With Zip Files

# from pathlib import Path
# from zipfile import ZipFile

# # zip = ZipFile("files.zip", "w")

# # for path in Path("../08. Modules/ecommerce/").rglob("*.*"):
# #     zip.write(path)
# # zip.close()

# # if something goes wrong with above final statements might not be called
# # so we need to use a try finally block or with
# # with ZipFile("files.zip", "w") as zip:
# #     for path in Path("../08. Modules/ecommerce/").rglob("*.*"):
# #         zip.write(path)

# with ZipFile("files.zip") as zip:
#     print(zip.namelist())
#     info = zip.getinfo("../08. Modules/ecommerce/__init__.py")
#     print(info.file_size)
#     print(info.compress_size)
#     zip.extractall("extract")

# * Working With CSV Files

import csv

# # Creating a csv file & writing data to it
# # with open("data.csv", "w") as file:
# #     writer = csv.writer(file)
# #     writer.writerow(["transaction_id", "product_id", "price"])
# #     writer.writerow([1000, 1, 5])
# #     writer.writerow([1001, 2, 15])

# # Reading data from a CSV file
# with open("data.csv") as file:
#     reader = csv.reader(file)
#     # print(list(reader))
#     for row in reader:
#         print(row)

# * Working With JSON Files

# import json
# from pathlib import Path

# # movies = [
# #     {"id": 1, "title": "Terminator", "year": 1989},
# #     {"id": 2, "title": "Kindergarten Cop", "year": 1993}
# # ]

# # data = json.dumps(movies)
# # Path("movies.json").write_text(data)

# data = Path("movies.json").read_text()
# # print(data)
# movies = json.loads(data)
# print(movies)
# print(movies[0]["title"])

# * Working with a SQLite Database

# import sqlite3
# import json
# from pathlib import Path

# # . Connecting to a sqlite db & adding data to it
# # movies = json.loads(Path("movies.json").read_text())
# # print(movies)

# # with sqlite3.connect("db.sqlite3") as conn:
# #     command = "INSERT INTO Movies VALUES(?, ?, ?)"
# #     for movie in movies:
# #         conn.execute(command, tuple(movie.values()))
# #     conn.commit()

# # . Reading data from a db
# with sqlite3.connect("db.sqlite3") as conn:
#     command = "SELECT * FROM Movies"
#     cursor = conn.execute(command)
#     # for row in cursor:
#     #     print(row)
#     movies = cursor.fetchall()
#     print(movies)

# * Working with  Timestamps

# import time

# # da_time = time.time()
# # print(da_time)


# def send_emails():
#     for i in range(10000):
#         pass


# start = time.time()
# send_emails()
# end = time.time()
# duration = end - start
# print(duration)

# * Working with  DateTimes

# from datetime import datetime
# import time

# da_datetime = datetime(2018, 1, 1)
# da_datetime = datetime.now()
# da_datetime = datetime.strptime("2018/01/01", "%Y/%m/%d")
# print(da_datetime)

# da_time = datetime.fromtimestamp(time.time())
# print(da_time)
# print(f"{da_datetime.year}/{da_datetime.month}")
# da_datetime.strftime("%Y/%m")

# * Working with  Time Deltas

# from datetime import datetime, timedelta

# # dt1 = datetime(2018, 1, 1)
# dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000)
# dt2 = datetime.now()

# duration = dt2 - dt1
# print(duration)
# print("days", duration.days)
# print("seconds", duration.seconds)
# print("total seconds", duration.total_seconds())

# * Generating Random Values
# import random
# import string

# print(random.random())
# print(random.randint(1, 10))
# print(random.choice([1, 2, 3, 4]))
# print(random.choices([1, 2, 3, 4], k=2))
# print(",".join(random.choices(string.ascii_letters + string.digits, k=4)))

# numbers = [1, 2, 3, 4]
# random.shuffle(numbers)
# print(numbers)

# * Opening the Browser

# import webbrowser

# print("Deployment completed")
# webbrowser.open("http://google.com")

# * Sending Emails

# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from pathlib import Path
# import smtplib

# message = MIMEMultipart()
# message["from"] = "Mig"
# message["to"] = "test@hotmail.com"
# message["subject"] = "This is a test email via Python!"
# message.attach(MIMEText("Body"))
# # message.attach(MIMEImage(Path("image.png").read_bytes()))

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("test@hotmail.com", "password")
#     smtp.send_message(message)
#     print("sent...")

# * Working with Templates

# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from pathlib import Path
# from string import Template
# import smtplib

# template = Template(Path("template.html").read_text())
# # template.substitute()

# message = MIMEMultipart()
# message["from"] = "Mig"
# message["to"] = "test@hotmail.com"
# message["subject"] = "This is a test email via Python!"
# # body = template.substitute({"name": "John"})
# body = template.substitute(name="John")
# message.attach(MIMEText(body, "html"))
# # message.attach(MIMEImage(Path("image.png").read_bytes()))

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("test@hotmail.com", "password")
#     smtp.send_message(message)
#     print("sent...")

# * Command-line Arguements

# import sys

# # print(sys.argv)

# if len(sys.argv) == 1:
#     print("Usage: python app.py <password>")
# else:
#     password = sys.argv[1]
#     print("Password", password)

# * Running External Programs

# import subprocess

# #. Legacy outdated
# # subprocess.call
# # subprocess.check_call
# # subprocess.check_output
# # subprocess.Popen

# try:
#     # result = subprocess.run(["ls", "-l"]) # for Unix
#     completed = subprocess.run(
#         # ["cmd", "/c", "dir"],
#         ["python", "other.py"],
#         capture_output=True,
#         text=True,
#         check=True
#     )
#     # completed.args
#     print("args", completed.args)
#     print("returncode", completed.returncode)
#     print("stderr", completed.stderr)
#     print("stdout", completed.stdout)
#     if completed.returncode != 0:
#         print(completed.stderr)
# except subprocess.CalledProcessError as ex:
#     print(ex)
