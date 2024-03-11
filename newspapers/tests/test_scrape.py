import json, os
import pytest

from core.scrape import NewsBase

def test_get_response(url):
    news = NewsBase(url)
    res = news.get_response()
    assert res.status_code == 200


def test_create_soup(url):
    news = NewsBase(url)
    soup = news.create_soup(news.text)


@pytest.mark.parametrize('site_name, data, page',[
    ('test1', ['1', '2', '3'], 1),
    ('test2', [{'content': 'very new content'}], 1 )
])

def test_save_data(site_name, data, page):
    news = NewsBase()
    news.save_data(site_name, data, page)

    with open(f'{site_name}.json') as file:
        result = json.load(file)

    assert os.path.isfile(f'{site_name}.json') == True
    assert result['articles'][0] == data[0]
    

def test_get_page(site_name):
    news = NewsBase()
    result = news.get_page(site_name)
    assert result == 1


if __name__ == "__main__":
    test_get_response('https://google.com')
    # test_get_page('d')
    # test_save_data("test_file", [{'content': 'very new content'}], 1)
