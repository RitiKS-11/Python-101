from scrape import *

def process():
    result = SetoPati()
    result.parse_content()
    # result.next()

if __name__ == "__main__":
    process()
    # r = Republica('https://myrepublica.nagariknetwork.com/news/ajax/query?key=tech&page=1')
    # s = r.parse_content()
    # print(s)