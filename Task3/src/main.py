from bs4 import BeautifulSoup
import requests
import jsonStructure
import json
import re

url = 'http://гддют.рф/'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
news = soup.findAll(class_='panel-group')

filteredNews = []
allNews = []

#сбор всех новостей
for nw in news:
    _allNews = soup.findAll(class_='panel panel-default pt-cv-content-item pt-cv-1-col')
    for alNw in _allNews:
        allNews.append(alNw)

#перебор каждой новости
for data in allNews:
    _title = ""
    _link = ""
    _date = ""
    _uHeader = ""

    title = data.find(class_='panel-title')
    if title is not None:
        _title = title.text
    else:
        _title = "Нет слов"

    body = data.find(class_='pt-cv-meta-fields')
    if body is not None:
        _date = body.text
    else:
        _date = "Нет даты"

    link = data.find('a', class_='panel-title')
    if link is not None:
        _link = link.get('href')
    else:
        _link = "Нет ссылки"
    
    underHeader = data.find(class_='pt-cv-content')
    if underHeader is not None:
        _uHeader = underHeader.text
    else:
        _uHeader = "Нет 2го подбородка"
        

    #удаление форматирования из строк
    _title = re.sub(r'\n?|\t?|\r?', '', _title)
    _link = re.sub(r'\n?|\t?|\r?', '', _link)
    _date = re.sub(r'\n?|\t?|\r?| ?', '', _date)
    _uHeader = re.sub(r'\n?|\t?|\r?', '', _uHeader)

    filteredNews.append(jsonStructure.News(title=_title, link=_link,date=_date,underHeader=_uHeader))

#сериализация
serializedData = json.dumps(filteredNews, cls=jsonStructure.NewsEncoder, ensure_ascii=False, indent=4)
file = open("jsonSolutionSerialized.json", 'w', encoding ='utf-8')
file.writelines(serializedData)
file.close()

