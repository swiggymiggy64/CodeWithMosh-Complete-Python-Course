
# * Creating Modules

# . Weve moved this into sales.py
# def calc_tax():
#     pass

# def clac_shipping():
#     pass

# . & can now import it like this
# from sales import calc_tax, calc_shipping
# calc_tax()
# calc_shipping()

# . Or this way
# import sales
# sales.calc_tax()
# sales.calc_shipping()

# * Compiled Python Files

# check out the __pycache__ folder

# * Module Search Path

# import sales
# import sys

# print(sys.path)

# * Packages

# . We created the ecommerce folder & moved sales.py into it
# . Then we created __init__.py in the ecommerce folder
# . Now we can import from sales.py in various ways

# . 1
# import ecommerce.sales
# ecommerce.sales.calc_tax()

# . 2
# from ecommerce.sales import calc_tax, calc_shipping
# calc_tax()
# calc_shipping()

# . 3
# from ecommerce import sales
# sales.calc_tax()
# sales.calc_shipping()

# * Sub-Packages

# . We created a new sub folder "shopping" within the ecommerce folder

# from ecommerce.shopping import sales # We now have to add the .shopping to "ecommerce"

# * Intra-package References

# see sales.py

# * The dir Function

# from ecommerce.shopping import sales

# # print(dir(sales))
# print(sales.__name__)
# print(sales.__package__)
# print(sales.__file__)

# * Executing Modules as Scripts

# from ecommerce.shopping import sales
