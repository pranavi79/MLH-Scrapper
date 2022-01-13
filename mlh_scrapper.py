import os
import requests
import html5lib
import bs4
import csv

def scraper(result):
    events = []
    dates = []
    soup = bs4.BeautifulSoup(result.text,'html5lib')
    events = soup.select('.event-name')
    dates = soup.select('.event-date')

    for event,date in zip(events,dates):
        events.append(event.getText())
        dates.append(date.getText())
    coulmns = ['Event Name','Event Date']
    with open('hackathon_list.csv','w',newline="") as csvfile:
        writer = csv.writer(csvfile) 
        writer.writerow(coulmns)
        for event,date in zip(events,dates):
            entry = [event,date]
            writer.writerow(entry)

result  = requests.get("https://mlh.io/seasons/2021/events")
scraper(result)