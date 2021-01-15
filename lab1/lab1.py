import requests

print("The requests version: ", requests.__version__)

home_page = requests.get("http://www.google.com/")

print("The status code is: ", home_page.status_code)
print("The content is: ", home_page.content)



