# -*- coding: utf-8 -*-
import scrapy.cmdline      

# Installation:
# - pip install scrapy (bzw. pip3 install scrapy)
# - Windows: pip install win32api (bzw. pip3 install win32api)
# initiales Projekt erzeugen:
# - scrapy startproject tutorial
# (- ggf. inneren tutorial-Ordner rausziehen, äußeren löschen)

def main():
    #cmd = 'scrapy runspider features_at_a_glance/quotes_spider.py -o quotes.xml'
    cmd = 'scrapy crawl iter -o res.json'
    scrapy.cmdline.execute(cmd.split())

if  __name__ =='__main__':
    main()