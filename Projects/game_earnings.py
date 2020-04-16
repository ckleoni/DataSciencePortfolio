# -*- coding: utf-8 -*-
import scrapy


class GameEarningsSpider(scrapy.Spider):
    name = 'game_earnings'
    allowed_domains = ['www.esportsearnings.com']
    start_urls = ['http://www.esportsearnings.com/history/2020/games']

    def parse(self, response):
        year = response.xpath("//div[@class='info_box']/nav/span/text()").get()
        game_list = response.xpath("//tbody/tr")
        for game in game_list:
            name = game.xpath(".//td/a/text()").get()
            earnings = game.xpath(".//td[3]/text()").get()
            players = game.xpath(".//td[4]/text()").get()
            events = game.xpath(".//td[5]/text()").get()
            yield{
                'game_title' : name,
                'total_earnings' : earnings,
                'total_players' : players,
                'total_events' : events,
                'year' : year
            }
        next_year = str(int(year) - 1)
        next_page = 'http://www.esportsearnings.com/history/{}/games'.format(next_year)
        if next_year is not '1997':
            yield response.follow(url=next_page, callback=self.parse)

