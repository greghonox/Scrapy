# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
from requests import get

class ScraptestudosPipeline(object):
    def process_item(self, item, spider):
        self.gvImage(item['imagem'])
        img = self.lrImage()

        sql = f"INSERT INTO Gofilmes(titulo, imagem, descricao, url, trailer) VALUES(?, ?, ?, ?, ?);"
        ddos = (item['titulo'], img, item['descricao'], item['url'], item['trailer'])
        self.con.execute(sql, ddos)
        self.con.commit()

    def gvImage(self, img):
        with open('img.jpg', 'wb') as arq:
            try: arq.write(get(img).content)
            except: pass
    
    def lrImage(self):        
        try: 
            with open('img.jpg', 'rb') as arq: return arq.read()
        except: return ''

    def criarTabela(self):
        sql = "CREATE TABLE Gofilmes(codigo integer primary key autoincrement, titulo text, imagem blob, descricao text, url text, trailer  text);"
        try:
            self.con.execute(sql)
            self.con.commit()
        except: pass

    def open_spider(self, spider):
        self.con = sqlite3.connect('goFilmes.db')
        self.criarTabela()

    def close_spider(self, spider):
        try: self.con.close()
        except: pass

        

