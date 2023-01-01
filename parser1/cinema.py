import requests
from bs4 import BeautifulSoup

class Film_parser:
    __URL = 'http://www.manascinema.com/movies'
    __HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
    @classmethod
    def __get_html(cls,url=None):
        if url is not None:
            req = requests.get(url=url, headers=cls.__HEADERS)
        else:
            req = requests.get(url=cls.__URL, headers=cls.__HEADERS)
        return req
    @staticmethod
    def get_data(html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', class_="short_movie_info")
        movies = []
        for item in items:
            info= str(item.find('div', class_='m_data'))\
                .replace('<br/>', '').replace('\r', '').replace('\n', '')\
                .replace('<div class="m_data">', '').replace('</div>','')\
                .replace('             ','').replace('(',' ').split(')')
            card = {
                'title':item.find('div', class_='m_title').find('a').string,
                'link':'http://www.manascinema.com' + item.find('div', class_='m_title').find('a').get('href'),
                'inf' : info[0]
            }
            movies.append(card)
        return movies
    @classmethod
    def parser(cls):
        global cur_page
        html = cls.__get_html()
        if html.status_code == 200:
            movies = []
            for i in range(1,3):
                html = cls.__get_html(f'{cls.__URL}?page={i}/')
                cur_page = cls.__get_data(html.text)
                movies.extend(cur_page)
            return movies
        else:
            raise Exception('не правильный запрос')


