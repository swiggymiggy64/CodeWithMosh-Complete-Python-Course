
# * Python Standard Library


# * Working With Paths

from pathlib import Path

# Path("C:\\Program Files\\Microsoft")
# Path(r"C:\Program Files\Microsoft")  # Same as above, is a raw string so no need for double \\
# Path("/usr/local/bin")  # Linux
# Path()  # Current folder
# Path("ecommerce/__init__.py")
# Path() / Path("ecommerce")
# Path() / "ecommerce" / "__init__.py"
# Path.home()

path = Path("../08. Modules/ecommerce/__init__.py")
print(path)
print(path.exists())
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

# path = path.with_name("file.txt")
path = path.with_suffix(".txt")
print(path)
print(path.absolute())

# * Working With Directories
