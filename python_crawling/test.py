import requests
from bs4 import BeautifulSoup

site =  requests.get('https://op.gg')
source = BeautifulSoup(site.text, 'html.parser')
print(source)
issue = source.select('.css-1pirsze e17e77tq9 .vm-placement')
print(issue)
for title in issue:
    print(title.get_text())