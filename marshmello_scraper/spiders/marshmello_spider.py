import scrapy

class MarshmelloSpider(scrapy.Spider):
    name = 'marshmello'
    start_urls = ['https://music.migu.cn/v3/search?page=1&type=song&i=1918dbd04d541f9e3b1d01f5167530d4c2dd9782&f=html&s=1704316157&c=001002A&keyword=marshmello&v=3.25.6']

    def parse(self, response):
        # Extracting song title and artist information
        songs = response.xpath('//div[@class="search-main"]//div[@class="songlist-body"]//div[@class="row J_CopySong"]')

        for song in songs:
            title = song.xpath('.//div[@class="song-name J_SongName"]/a/text()').get()
            
            # Handling cases where there are multiple artists
            artists = song.xpath('.//div[@class="song-singers J_SongSingers"]/a/text()').getall()
            
            yield {
                'title': title,
                'artists': artists,
            }
