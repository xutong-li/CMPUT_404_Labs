import requests

print("The requests version: ", requests.__version__)

home_page = requests.get("http://www.google.com/")
print("The status code is: ", home_page.status_code)
print("The content is: ", home_page.content)

# The raw url of lab1 is: https://raw.githubusercontent.com/xutong-li/CMPUT_404_Labs/main/lab1/lab1.py
raw_code = requests.get("https://raw.githubusercontent.com/xutong-li/CMPUT_404_Labs/main/lab1/lab1.py")

f = open("lab1_code.txt", "w")
f.write(raw_code.text)
f.close()
f = open("lab1_code.txt", "r")
print('THE CODE BELOW: \n', f.read())
