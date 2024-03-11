from core.scrape import *

def process():
    result = OnlineKhabar()
    result.parse_content()

if __name__ == "__main__":
    process()
