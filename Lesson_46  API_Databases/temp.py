import bs4
import requests

resource = requests.get('https://github.com/RuslanDubovtsev?tab=repositories')
data = resource.text
parced_page = bs4.BeautifulSoup(data, 'lxml')
name = parced_page.find_all('a', itemprop="name codeRepository")
pars_dict = {}
for i in name:
    pars_dict[i.text] = 'https://github.com/'+i['href']
    # print(i)
for key, value in pars_dict.items():
    print(key, ":", value)