# import requests
# from bs4 import BeautifulSoup

# site =  requests.get('https://op.gg')
# source = BeautifulSoup(site.text, 'html.parser')
# print(source)
# issue = source.select('.css-1pirsze e17e77tq9 .vm-placement')
# print(issue)
# for title in issue:
#     print(title.get_text())


import requests

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'}
url = "https://www.op.gg"
source = requests.get(url, headers = header)
print("응답코드 : ", source.status_code)

with open("opgg.html", "w", encoding = "utf8") as f:
    f.write(source.text)