from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import json


def main():
    url = 'https://walletconnect.com/_next/data/ou0j8RfCEqyvG6UhVPO72/index.json'
    response = urlopen(url)
    data_json = json.loads(response.read())
    d = dict(data_json['pageProps'])

    for record in d['walletData']:
        save_data(record['homepage'], record['name'])


def save_data(homepage, name):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([name, homepage])


if __name__ == '__main__':
    main()
