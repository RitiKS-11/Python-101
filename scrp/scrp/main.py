import requests, csv
from collections import defaultdict

from urls import provide_urls

def get_page(url):
    try:
        cookies = {
            'datadome': 'HzoMS4d9zQPohVkHwNryHUurcq1LMYl_ZZzuN8JB~~RYPoHo9Dv62h9oNaemiAPBdkzhm5ylx77eFUoQVaff83VcOSgNQzHhT1pIpSaFYNBurftfCLvn0E6qmxHEBo2M',
            'TASameSite': '1',
            'TAUnique': '%1%enc%3A5yphkXU%2B%2BLE12Ai27pmPshWwJnM%2F%2BIoJceiJCLjggzgTdR%2F89nytZX2VzCc4LdYwNox8JbUSTxk%3D',
            'TATrkConsent': 'eyJvdXQiOiJBRFYsU09DSUFMX01FRElBIiwiaW4iOiJBTkEsRlVOQ1RJT05BTCJ9',
            'TASSK': 'enc%3AAOZhcd88jgZx5Gsg6ghAZ%2BnEIw2nWbyNt2a86V%2Fxaoe%2B3el4fX7x%2BXx8BXZQ3NQEgAraizZaeCeD5XEXSa%2FQLuiqBYIWJ61wCvDFJ4YoStZf82FuVX1vmnFVCf2MVuixtg%3D%3D',
            'TART': '%1%enc%3A9zZlyhdOj3%2BGjsFP5n%2FeuFwA13lc73bXJ%2F8siwmntBgC7Cb4Yt1LIFh0A7jrkulyfYtftmnsPgU%3D',
            'VRMCID': '%1%V1*id.10568*llp.%2FRestaurant_Review-g293890-d2343431-Reviews-Kathmandu_Grill_Restaurant_And_Wine_Bar-Kathmandu_Kathmandu_Valley_Bagmati_Zone_C%5C.html*e.1707917361815',
            'TATravelInfo': 'V2*AY.2024*AM.2*AD.18*DY.2024*DM.2*DD.19*A.2*MG.-1*HP.2*FL.3*DSM.1707312617200*RS.1',
            'ServerPool': 'A',
            'PMC': 'V2*MS.29*MD.20240207*LD.20240208',
            '__vt': 'QgEF9W_o81o6qK0sABQCwRB1grfcRZKTnW7buAoPsStOcPaMUmg45mKFNHpw056hwKkwIJPHmCYyExCkHhjSld1UiRRx62_Xx4yxUUy7IYxb2ejMUaYVxdhM68zw3JYw27bdvn21oxKJ8wOUaul96qguiQ',
            'TADCID': 'qix_3iDdPOUE__RqABQCmq6heh9ZSU2yA8SXn9Wv5Htw0JqppRds4BfM46DOyoFsr3Haqt3gees8ns3h8nHQDrDTD2aMoZxoGhs',
            'SRT': 'TART_SYNC',
            'TAUD': 'LA-1707309208069-1*RDD-1-2024_02_07*HDD-3409041-2024_02_18.2024_02_19*LG-93268474-2.1.F.*LD-93268475-.....',
            'TASID': 'A7A49C92710F430D8BA773DB9F926428',
            '_abck': '4586BF59B484F2C5F4E0FBCB035DD521~-1~YAAQjwVaaOcr0nqNAQAAlzweiQtJzyKy8MWtpGkIMmq1K/0JvngmbaxDCT5lb3LVqhlWg8hviw374S4wdgQYih5Z0yN8j6HxdJMq+NOZ3YZp66MHFDcMXNFFyFm0llQrRcwkLbszYRc2Xl7XD5sceDdApojVVof7FQdvl9g22ML6hQmWfflN0Hgkg9w0vHHcewczw+zC+SEhGCQsWJcFtfs+RC7j+yihfZMrxX+vdZpOss0eLduQutgNgaHgnbnD/vju9h6BPmgfhgwbWZhwVP8oqDJ2uhDdeAwqgOge8ZYGhj0u71fDtcODXvngoRm3lY2YDfR8krNRZXEynUaVgqnIpA8bU29efHG1hSz949PXLVBxQkvomLP59aLl+WwKlX5Me44jDNqwDQ/RmYU=~-1~-1~-1',
            'bm_sz': '2E626DB98F926F58D4D790F5594E9F1D~YAAQjwVaaOgr0nqNAQAAlzweiRYbMJSTkjyN9nkjrvXiVLqen8q9SnRlc7rF+TXKQ/UIT/tmauZfNcS6l83keDzLRfYT5QXp5/iepMUr8zAUaix3jnlZ4pjPO8DgAE9tISRNaLYG6C7quuFE2hJ29E+3xYlroCsKk/qqfcdAvqHQAXqi6EvDXijzEcAFmmrtMcYHlh1m6zCGpIn308A5kW/QaXEcrdOEsXnM+0itSdsJIiGnJqj+toMUuTHF1Z/7f1s8/lJPjQXP5EeSG9bUAPd0MUONecSUZ/hC2lfhOXwM9jEsntw+gGDxzuhXjMHyJ+VBHkzH78ZJ3ed1kokM7DM=~4408630~4605251',
            'OptanonConsent': 'isGpcEnabled=1&datestamp=Thu+Feb+08+2024+20%3A13%3A01+GMT%2B0545+(Nepal+Time)&version=202310.2.0&browserGpcFlag=1&isIABGlobal=false&hosts=&consentId=4f46448b-88ed-4a92-bd87-ee42bd527e31&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A0&AwaitingReconsent=false',
            'TASession': 'V2ID.A7A49C92710F430D8BA773DB9F926428*SQ.4*LS.Attraction_Review*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*TRA.true*LD.447384*EAU._',
            'PAC': 'AIMmqvhQg1U77s_1otwr_P3PPBW7WtmshR-DSf2PwvgtWYNZmYVdu1Mxc9TPXh2MZS3vAv7c95LteQRYE4mJHc6OUjyl9zGTDsR0y7d5gFOsE1zGxhaWYXaiOp00l17HPh-kB0Pl2-1f3XV_O29tFbeoqY0TCZGizDFiwjvVJ4ANoVMVTmoT0fUa1tccwLbbyKEs9dXVnD4WXg8-G5x37dvjchM8SE39zs7OqH_c4mziFBbGmkaagy-dzJbx91Brgg%3D%3D',
        }

        headers = {
            'authority': 'www.tripadvisor.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.6',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'sec-ch-ua': '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        }

        response = requests.get(
            'https://www.tripadvisor.com/Attraction_Review-g298570-d447384-Reviews-Chinatown-Kuala_Lumpur_Wilayah_Persekutuan.html',
            # cookies=cookies,
            headers=headers,
            timeout=10
        )

        return response.text

    except Exception as e:
        print(e)
        raise e
    

def parse_content(response):
    parsed_text = defaultdict()

    content = response.split('<span class="biGQs _P fiohW fOtGX"><a target="_self" href="/Profile/ianb111" class="BMQDV _F Gv wSSLS SwZTJ FGwzt ukgoS">ianb111</a></span><div class="JINyA"><div class="biGQs _P pZUbB osNWb"><span>')[-1].split('<div class="HdolS"></div><div class="xkSty">')[0]
    reviews = content.split('<div class="biGQs _P fiohW qWPrE ncFvv fOtGX">')[1:]

    for review in reviews:
        title = review.split('<span class="yCeTE">')[1].split('</span></a></div><div class="RpeCd">')[0]
        review_date = review.split('</div><div class="RpeCd">')[1].split('</div><div class="_T FKffI bmUTE">')[0]
        review_body = review.split('<span class="JguWG"><span class="yCeTE">')[1].split('</span></span></div></div><div class="lszDU">')[0]
        
        parsed_text[title] = {'title': title, 'date': review_date, 'body': review_body}    
    
    return dict(parsed_text)


def clean_content(text):
    for _, item in text.items():
        item['title'] = item['title'].replace('<br />', '')
        item['date'] = item['date'].replace('<br />', '')
        item['body'] = item['body'].replace('<br />', '')

    return text


def save_csv(cleaned_reviews):
    with open('data.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'date', 'body'])
        for _, review in cleaned_reviews.items():
            writer.writerow({'title': review['title'], 'date': review['date'], 'body':review['body']})
        



def handle_process(url):
    response = get_page(url)
    reviews_dict = parse_content(response)
    cleaned_reviews = clean_content(reviews_dict)
    save_csv(cleaned_reviews)



if __name__ == "__main__":
    urls = provide_urls()
    for url in urls:
        handle_process(url)