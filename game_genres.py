# -*- coding: utf-8 -*-
import scrapy


class GameGenresSpider(scrapy.Spider):
    name = 'game_genres'
    allowed_domains = ['www.esportsearnings.com']
    start_urls = ['https://www.esportsearnings.com/games/browse-by-genre']

    def parse(self, response):
        for i in range(1,12):
            i = str(i)
            genre = response.xpath("//div[@class='games_main_genre_header'][{}]/span[@class='games_main_genre_title']/text()".format(i)).get()
            games = response.xpath("//div[@class='games_main_genre_body'][{}]/div/div[@class='games_main_game_title']".format(i))
            for game in games:
                name = game.xpath(".//a/text()").get()
                yield{
                    'game_title' : name,
                    'genre' : genre
                }
        
            

            