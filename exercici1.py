#!/usr/bin/env python
'''
Simple client web per treure el titol

@author: err8@alumnes.udl.cat
'''

import urllib2
import bs4

class Client(object):
    # obtenir plana web
    def get_webpage(self,page):
        f = urllib2.urlopen(page)
        htmlpage = f.read()
        f.close()
        return htmlpage

    # buscar deades
    def search_data(self, html):
        bd = bs4.BeautifulSoup(html, "lxml")
        caixa = bd.find("div", "dotd-title").text
	return caixa.strip()

    def main(self):
        webpage = self.get_webpage('https://www.packtpub.com/packt/offers/free-learning/')
        results = self.search_data(webpage)
        # imprimir resultats
        print results
        

if __name__ == "__main__":
    cw = Client()
    cw.main()
