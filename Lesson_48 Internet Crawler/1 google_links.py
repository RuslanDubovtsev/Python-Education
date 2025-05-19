import requests
import bs4

req = requests.get("https://www.google.com/")
soup = bs4.BeautifulSoup(req.text, 'lxml')

dict = {}
for elem in soup.find_all("a"):
    href = elem.get('href')
    text = elem.text
    # dict[text] = href
    # try:
    #     req = requests.get(href)
    #     print(req.status_code)
    # except Exception as e:
    #     print(e)
    dict[text] = 'https://www.google.com/' + href if 'http' not in href else href

    # print(f"{text} - {href}")

for key, value in dict.items():
    # try:
    #     req = requests.get(value)
    #     print(req.status_code)
    # except Exception as e:
    #     print(e)
    req = requests.get(value)
    print(req.status_code)
    print(value)