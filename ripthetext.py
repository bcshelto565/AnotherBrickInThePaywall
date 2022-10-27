from bs4 import BeautifulSoup
import requests
import webbrowser

url = input('Whats the url we wanna read?: ')
filename = input('whats the filename (end the filename with a .html filetype): ')
headers = {'User-Agent': 'Googlebot'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
text = (str(soup.prettify()))
with open(filename, 'w+') as file:
    test = file.write(text)
    # print(str(soup.prettify()))
    # print(page.json())
    # sleep(0.1)
    # print(filename)
webbrowser.open(filename)
# print(soup)
exit()

