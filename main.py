from calendar import monthrange
from json import dumps, loads
import requests
import datetime
from datetime import datetime, timedelta


def save_to_file(dates_number):
    date = datetime.date(2020, 12, 31)
    dollar_rates = []

    for i in range(dates_number):
        date = date + timedelta(days=1)
        url = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=usd&date={date.strftime("%Y%m%d")}&json'
        request = requests.get(url).json()[0]
        dollar_rates.append({'rate':request['rate'], 'date':request['exchangedate']})
    with open('USD.json', 'w') as file:
        file.write(dumps(dollar_rates))

    print(dollar_rates)


def read_from_file_and_search_maxmin():
    with open('USD.json', 'r') as file:
        dollar_rates = loads(file.read())
    print(dollar_rates)
    min = 0
    max = 0
    for i in range(len(dollar_rates)):
        if dollar_rates[min]['rate']>dollar_rates[i]['rate']:
            min = i
        if dollar_rates[max]['rate']<dollar_rates[i]['rate']:
            max = i
    print("Min:", dollar_rates[min])
    print("Max:", dollar_rates[max])
    return dollar_rates


def search_midinmonth():
    with open('USD.json', 'r') as file:
        dollar_rates = loads(file.read())
    sum_month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(dollar_rates)):
        month_number = int(datetime.strptime(dollar_rates[i]['date'], '%d.%m.%Y').strftime('%m')) - 1
        sum_month[month_number] += dollar_rates[i]['rate']
    midinmonth = []
    for i in range(12):
        midinmonth.append(i)
        midinmonth[i] = sum_month[i]/monthrange(2021, i + 1)[1]
        print(i+1)
        print(midinmonth[i])
    print(sum_month)


search_midinmonth()
read_from_file_and_search_maxmin()





