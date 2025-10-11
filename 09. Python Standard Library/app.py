
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
