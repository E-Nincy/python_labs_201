# Create a virtual environment and edit the activation script to add
# the following information:
# 
# - ENVIRONMENT="development"
# - SECRET="i ate your sweets"
# 
# Then write the necessary code to access and print the values of these
# two environment variables in this script.

import os

environment = os.getenv("ENVIRONMENT")
secret = os.getenv("SECRET")

print("ENVIRONMENT:", environment)
print("SECRET:", secret)
