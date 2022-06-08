import requests
from bs4 import BeautifulSoup
import pyshorteners
import creds


class Shop():
    def __init__(self):
        self.page = None
        self.soup = None

    def GetURL(self, url):
        self.url = url
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.text, 'html.parser')

    def ShortenUrl(self):
        '''
        shorten the link to the page with the product offer
        using the api key from bitly.com
        '''
        type_bitly = pyshorteners.Shortener(
            api_key=creds.api_key)
        self.short_url = str(type_bitly.bitly.short(self.url))


class Hebe(Shop):
    def __init__(self):
        super().__init__()

    def GetName(self):
        '''Extract product name'''

        if self.soup.find_all('a', {'class': 'product-content__link'}):
            firm_name = self.soup.find('a', {'class':
                                       'product-content__link'}).next_element
            product_name = firm_name.next_element.strip()
            name = ('{}{}'.format(firm_name.strip(), product_name))
        else:
            firm_name = self.soup.find('h1', {'class': 'product-content__brand'
                                              })
            firm_name = firm_name.next_element.next_element.next_element
            product_name = firm_name.next_element.strip()
            name = (('{}-{}').format(firm_name.strip(), product_name))
        if len(name) > 30:
            name = name[:26]+'...'
        return name

    def GetRegularPrice(self):
        '''Extract product regular price'''
        reg_price_int = int(self.soup.find('div', {'class':
                                           'price-product__standard'
                                                   }).next_element.strip())
        reg_price_dec = int(self.soup.find('span', {'class':
                                           'price-product__decimal'}
                                           ).next_element.strip())/100
        reg_price = reg_price_int+reg_price_dec
        return reg_price

    def GetSalePrice(self):
        '''Extract product sale price'''
        sale_price_int = int(self.soup.find('div', {'class':
                                            'price-product__sales'}
                                            ).next_element.strip())
        sale_price_dec = int(self.soup.find('span', {'class':
                                            'price-product__decimal'}
                                            ).next_element.strip())/100
        sale_price = sale_price_dec+sale_price_int
        return sale_price

    def CalcPct(self):
        '''calculate the price reduction as a percentage'''
        reg_price = self.GetRegularPrice()
        sale_price = self.GetSalePrice()
        sale_pct = round((1-(sale_price/reg_price)) * 100)
        return sale_pct

    def GetInfo(self):
        '''
           create a product data list which includes:
           product name, regular price, sale price, 
           price reduction as a percentage and shortened link 
        '''
        name = self.GetName()
        reg_p = self.GetRegularPrice()
        sale_p = self.GetSalePrice()
        sale_pct = self.CalcPct()
        dane = [[name, str(reg_p), str(sale_p), str(sale_pct), self.short_url]]
        return dane
