from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

browser = webdriver.Chrome()

def getVacancies(pageNumber):
    def openPage(num):
        browser.get(f'https://www.evraz.com/ru/careers/vacancies/?page={int(num)}')
        time.sleep(1)

    openPage(pageNumber)

    result = []
    box = browser.find_element(By.CLASS_NAME, 'vacancies-results').find_element(By.CLASS_NAME, 'row').find_elements(By.CLASS_NAME, 'z-card__wrapper')
    for vacancy in box:
        _date = vacancy.find_element(By.CLASS_NAME, 'z-card__date').text
        _title = vacancy.find_element(By.CLASS_NAME, 'z-card__title').text
        _table = vacancy.find_elements(By.TAG_NAME, 'td')
        _salary = _table[1].text
        _city = _table[3].text
        
        card = {
            "date":_date,
            "title":_title,
            "salary":_salary,
            "city":_city
            }
        
        result.append(card)

    return result

def writeBodyInCSV(vacancies):
    for row in vacancies:
        file.write(str(row['date'] + ';' + row['title'] + ';' + row['salary'] + ';' + row['city'] + '\n'))

file = open("vacncies.csv", 'w+', encoding="utf-8")

headers = str("Дата" + ';' + "Должность" + ';' + "Зарплата" + ';' + "Город\n")
file.write(headers)
writeBodyInCSV(getVacancies(1))
writeBodyInCSV(getVacancies(2))
writeBodyInCSV(getVacancies(3))

file.close()