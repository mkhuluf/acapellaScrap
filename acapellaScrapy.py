import scrapy

'''
This Spider will give the user to grab the files from the website https://archive.org/download/Acapellas_201711
and download each file one-by-one.
REMEMBER: When downloading files, you'll have to edit the default_settings.py file in the scrapy module folder
to enable your item pipeline and file location

FILES_STORE = 'File Path Location'
ITEM_PIPELINES = {'scrapy.pipelines.files.FilesPipeline': 1}

Also, when scraping files, it'll not name the file based on the name of the file in the website.
The file name will print out the SHA1 hash code of the file.
'''

class Songs(scrapy.Item):
    title = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()

class AcapellaSpider(scrapy.Spider):
    name = 'Acapella'
    allowed_domains = ['archive.org/']
    start_urls = ['https://archive.org/download/Acapellas_201711']

    def parse(self, response):
        fileURL = response.css('table.directory-listing-table > tbody > tr > td > a::attr(href)').extract()
        mp3List = []
        mp3Title = []
        for i in fileURL:
            if ".mp3" in i:
                mp3Title.append(i)
                mp3List.append("https://ia800103.us.archive.org/7/items/Acapellas_201711/" + i)

        yield Songs(title=mp3Title, file_urls=mp3List)