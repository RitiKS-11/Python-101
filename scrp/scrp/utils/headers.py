

def json_header(url, geo, detail, offset, attraction, update_token):
    content_type = 'attraction' if attraction == 'Attraction_Review' else 'attraction_product'
    print(content_type, attraction, url)
    # print(geo, detail, offset)

    cookies = {
        'datadome': 'HzoMS4d9zQPohVkHwNryHUurcq1LMYl_ZZzuN8JB~~RYPoHo9Dv62h9oNaemiAPBdkzhm5ylx77eFUoQVaff83VcOSgNQzHhT1pIpSaFYNBurftfCLvn0E6qmxHEBo2M',
        'TASameSite': '1',
        'TAUnique': '%1%enc%3A5yphkXU%2B%2BLE12Ai27pmPshWwJnM%2F%2BIoJceiJCLjggzgTdR%2F89nytZX2VzCc4LdYwNox8JbUSTxk%3D',
        'TASSK': 'enc%3AAOZhcd88jgZx5Gsg6ghAZ%2BnEIw2nWbyNt2a86V%2Fxaoe%2B3el4fX7x%2BXx8BXZQ3NQEgAraizZaeCeD5XEXSa%2FQLuiqBYIWJ61wCvDFJ4YoStZf82FuVX1vmnFVCf2MVuixtg%3D%3D',
        'VRMCID': '%1%V1*id.10568*llp.%2FRestaurant_Review-g293890-d2343431-Reviews-Kathmandu_Grill_Restaurant_And_Wine_Bar-Kathmandu_Kathmandu_Valley_Bagmati_Zone_C%5C.html*e.1707917361815',
        'TATrkConsent': 'eyJvdXQiOiJBRFYsU09DSUFMX01FRElBIiwiaW4iOiJBTkEsRlVOQ1RJT05BTCJ9',
        'PMC': 'V2*MS.29*MD.20240207*LD.20240220',
        'TATravelInfo': 'V2*A.2*MG.-1*HP.2*FL.3*DSM.1707312617200*RS.1',
        'TAUD': 'LA-1707309208069-1*RDD-1-2024_02_07*HDD-3409041-2024_02_18.2024_02_19*ARC-96486623*LG-1130912658-2.1.F.*LD-1130912659-.....',
        'TADCID': '9qz0B74rwHqdovn8ABQCmq6heh9ZSU2yA8SXn9Wv5HvEXrwAodo3jMCk_sN9wVZuPoB1TtlipYkjO-HFGbjHXde5nLeopGN9WkE',
        'TASID': 'FAE1CD3A082907F062F50720FCA3AB2C',
        '_abck': '4586BF59B484F2C5F4E0FBCB035DD521~-1~YAAQhpbTZ0s2nFWNAQAAvQ+d1QuCjH8zxBI+tOxMb5sI1crkrmQ6iNMHBzpNKFtyxlYkoY2jvlw6ng/ocrwr8NdBwxSDq1HuIQ76MzvWKx8H3T1GRmgAa1wKBMpTwwQHy4OK/ina3IYL2SKc9InYZ57wL9WEy5Vr+LAPV7F6X1UP5hAQc+QtL3xkqZAXmmD1utAeurMbmrANUq9qQ2C0O0DbLx7gNS8BKJz3S4vupS+tmwBc1aKj2MkRdhs17+A0S4Myv0AIE6rPHe3+ZAcYOgCc33frUchg4kKsdzoO4LfJbN7eZn8cew4dLrgXHifQcjtwnp7BfTvIp2baMemIbung6zL2Cak3NhqIaBKDRJChLuomgzrV6MLawePkEKEJlsiawni10LjYhQkhvTc=~-1~-1~-1',
        'bm_sz': '4C0A195128DDB75AED11C4DFFF773280~YAAQhpbTZ0w2nFWNAQAAvQ+d1RaUCugYhJ/CrLQsseD8C2zGdI7+nuLZrewZ2mLcPoivUQRKSAkQvfjuYl0Q/zTP6+XGcU+gjeJ1sonLIEvk0niSrDxHfdrR9QFR9Xh4NPH4n4CwgeRee4TNOuVpSZKXx/wd9YJGAo8kpWv3m/q1cJEqYMB4n/qsIvyhKKBe0ZyFTM2O6oXv2U+JmdEPJvJjUk++kVkJ4RZfg+uvPs7AyxXRx8bO102jlghDGKOlaRahgHOXmGzAJR76NeirpKoaey//qgFqRF1XJQg8X8P1u9gDehP7EqNirbKWk7cCc8aEICCTvVKOh70arJ18WrC7WMYGTsWIdhXaJfY2H/LzNidrxxqDaaRscg==~3159619~3621441',
        'TART': '%1%enc%3A9zZlyhdOj38KSphF3FXw6xYJcETBXMBq%2Ffm1piT%2FWi%2BVCaMzj%2B1f6b%2F2uGqXJTalW1JxtpsONWQ%3D',
        'PAC': 'ACPMUus4UiIUfUIJfaCstx-G5Vhnitnfd4_Z1eigXy0DAnYBG1wDVFQ3LbWA0fbeBR4qkukbndzWvTWg4XFphw3FYPhVPnlV-jAp7Ybx-5mFefJm1qFYv1JafP2c7xAaNzggXWTGHDj9N6dJ8K_TeH2nYc2BT7ZwpiLjhrOEyvXA9FlXvwKQyn1_Hw41aPrR3eef1BXx6W2Inw8kzY6ZyRZFE74TSpq_XMCiR2pm0j6jPapb9IXnPY_3AWTfpDf45XtPlP7p8L1ZCNKvoWjEQGTwJZe612-FmUpCVUZItxw8',
        'SRT': 'TART_SYNC',
        'OptanonConsent': 'isGpcEnabled=1&datestamp=Fri+Feb+23+2024+18%3A38%3A28+GMT%2B0545+(Nepal+Time)&version=202310.2.0&browserGpcFlag=1&isIABGlobal=false&hosts=&consentId=0d5f4688-c039-4d12-bbaa-656e08345da8&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A0&AwaitingReconsent=false',
        'TASession': 'V2ID.FAE1CD3A082907F062F50720FCA3AB2C*SQ.31*LS.AttractionProductReview*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*TRA.true',
        '__vt': 'PrxPT-Cd--mng4VwABQCwRB1grfcRZKTnW7buAoPsSuiddRCDEGux5lHBRWGqwclQV-uwga015nvDfg32NQ62UZjG13A5u7HazDCaxM0E6hRu9rFdjF1imeUuNR7tIUqFKOMTVwlBcb8kohFHjkjGOJiyQ',
    }

    headers = {
        'authority': 'www.tripadvisor.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': 'datadome=HzoMS4d9zQPohVkHwNryHUurcq1LMYl_ZZzuN8JB~~RYPoHo9Dv62h9oNaemiAPBdkzhm5ylx77eFUoQVaff83VcOSgNQzHhT1pIpSaFYNBurftfCLvn0E6qmxHEBo2M; TASameSite=1; TAUnique=%1%enc%3A5yphkXU%2B%2BLE12Ai27pmPshWwJnM%2F%2BIoJceiJCLjggzgTdR%2F89nytZX2VzCc4LdYwNox8JbUSTxk%3D; TASSK=enc%3AAOZhcd88jgZx5Gsg6ghAZ%2BnEIw2nWbyNt2a86V%2Fxaoe%2B3el4fX7x%2BXx8BXZQ3NQEgAraizZaeCeD5XEXSa%2FQLuiqBYIWJ61wCvDFJ4YoStZf82FuVX1vmnFVCf2MVuixtg%3D%3D; VRMCID=%1%V1*id.10568*llp.%2FRestaurant_Review-g293890-d2343431-Reviews-Kathmandu_Grill_Restaurant_And_Wine_Bar-Kathmandu_Kathmandu_Valley_Bagmati_Zone_C%5C.html*e.1707917361815; TATrkConsent=eyJvdXQiOiJBRFYsU09DSUFMX01FRElBIiwiaW4iOiJBTkEsRlVOQ1RJT05BTCJ9; PMC=V2*MS.29*MD.20240207*LD.20240220; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*DSM.1707312617200*RS.1; TAUD=LA-1707309208069-1*RDD-1-2024_02_07*HDD-3409041-2024_02_18.2024_02_19*ARC-96486623*LG-1130912658-2.1.F.*LD-1130912659-.....; TADCID=9qz0B74rwHqdovn8ABQCmq6heh9ZSU2yA8SXn9Wv5HvEXrwAodo3jMCk_sN9wVZuPoB1TtlipYkjO-HFGbjHXde5nLeopGN9WkE; TASID=FAE1CD3A082907F062F50720FCA3AB2C; _abck=4586BF59B484F2C5F4E0FBCB035DD521~-1~YAAQhpbTZ0s2nFWNAQAAvQ+d1QuCjH8zxBI+tOxMb5sI1crkrmQ6iNMHBzpNKFtyxlYkoY2jvlw6ng/ocrwr8NdBwxSDq1HuIQ76MzvWKx8H3T1GRmgAa1wKBMpTwwQHy4OK/ina3IYL2SKc9InYZ57wL9WEy5Vr+LAPV7F6X1UP5hAQc+QtL3xkqZAXmmD1utAeurMbmrANUq9qQ2C0O0DbLx7gNS8BKJz3S4vupS+tmwBc1aKj2MkRdhs17+A0S4Myv0AIE6rPHe3+ZAcYOgCc33frUchg4kKsdzoO4LfJbN7eZn8cew4dLrgXHifQcjtwnp7BfTvIp2baMemIbung6zL2Cak3NhqIaBKDRJChLuomgzrV6MLawePkEKEJlsiawni10LjYhQkhvTc=~-1~-1~-1; bm_sz=4C0A195128DDB75AED11C4DFFF773280~YAAQhpbTZ0w2nFWNAQAAvQ+d1RaUCugYhJ/CrLQsseD8C2zGdI7+nuLZrewZ2mLcPoivUQRKSAkQvfjuYl0Q/zTP6+XGcU+gjeJ1sonLIEvk0niSrDxHfdrR9QFR9Xh4NPH4n4CwgeRee4TNOuVpSZKXx/wd9YJGAo8kpWv3m/q1cJEqYMB4n/qsIvyhKKBe0ZyFTM2O6oXv2U+JmdEPJvJjUk++kVkJ4RZfg+uvPs7AyxXRx8bO102jlghDGKOlaRahgHOXmGzAJR76NeirpKoaey//qgFqRF1XJQg8X8P1u9gDehP7EqNirbKWk7cCc8aEICCTvVKOh70arJ18WrC7WMYGTsWIdhXaJfY2H/LzNidrxxqDaaRscg==~3159619~3621441; TART=%1%enc%3A9zZlyhdOj38KSphF3FXw6xYJcETBXMBq%2Ffm1piT%2FWi%2BVCaMzj%2B1f6b%2F2uGqXJTalW1JxtpsONWQ%3D; PAC=ACPMUus4UiIUfUIJfaCstx-G5Vhnitnfd4_Z1eigXy0DAnYBG1wDVFQ3LbWA0fbeBR4qkukbndzWvTWg4XFphw3FYPhVPnlV-jAp7Ybx-5mFefJm1qFYv1JafP2c7xAaNzggXWTGHDj9N6dJ8K_TeH2nYc2BT7ZwpiLjhrOEyvXA9FlXvwKQyn1_Hw41aPrR3eef1BXx6W2Inw8kzY6ZyRZFE74TSpq_XMCiR2pm0j6jPapb9IXnPY_3AWTfpDf45XtPlP7p8L1ZCNKvoWjEQGTwJZe612-FmUpCVUZItxw8; SRT=TART_SYNC; OptanonConsent=isGpcEnabled=1&datestamp=Fri+Feb+23+2024+18%3A38%3A28+GMT%2B0545+(Nepal+Time)&version=202310.2.0&browserGpcFlag=1&isIABGlobal=false&hosts=&consentId=0d5f4688-c039-4d12-bbaa-656e08345da8&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A0&AwaitingReconsent=false; TASession=V2ID.FAE1CD3A082907F062F50720FCA3AB2C*SQ.31*LS.AttractionProductReview*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*TRA.true; __vt=PrxPT-Cd--mng4VwABQCwRB1grfcRZKTnW7buAoPsSuiddRCDEGux5lHBRWGqwclQV-uwga015nvDfg32NQ62UZjG13A5u7HazDCaxM0E6hRu9rFdjF1imeUuNR7tIUqFKOMTVwlBcb8kohFHjkjGOJiyQ',
        'origin': 'https://www.tripadvisor.com',
        'referer': f'https://www.tripadvisor.comurl',
        'sec-ch-ua': '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    json_data = [
        {
            'variables': {
                'page': attraction,
                'params': [
                    {
                        'key': 'offset',
                        'value': offset,
                    },
                    {
                        'key': 'geoId',
                        'value': geo,
                    },
                    {
                        'key': 'detailId',
                        'value': detail,
                    },
                ],
                'route': {
                    'page': attraction,
                    'params': {
                        'offset': offset,
                        'geoId': geo,
                        'detailId': detail,
                    },
                },
            },
            'extensions': {
                'preRegisteredQueryId': 'f742095592a84542',
            },
        },
        {
            'variables': {
                'pageName': attraction,
                'relativeUrl': url,
                'parameters': [
                    {
                        'key': 'offset',
                        'value': offset,
                    },
                    {
                        'key': 'geoId',
                        'value': geo,
                    },
                    {
                        'key': 'detailId',
                        'value': detail,
                    },
                ],
                'route': {
                    'page': attraction,
                    'params': {
                        'offset': offset,
                        'geoId': geo,
                        'detailId': detail,
                    },
                },
            },
            'extensions': {
                'preRegisteredQueryId': '1a7ccb2489381df5',
            },
        },
        {
            'variables': {
                'page': attraction,
                'pos': 'en-US',
                'parameters': [
                    {
                        'key': 'offset',
                        'value': offset,
                    },
                    {
                        'key': 'geoId',
                        'value': geo,
                    },
                    {
                        'key': 'detailId',
                        'value': detail,
                    },
                ],
                'factors': [
                    'TITLE',
                    'META_DESCRIPTION',
                    'MASTHEAD_H1',
                    'MAIN_H1',
                    'IS_INDEXABLE',
                    'RELCANONICAL',
                ],
                'route': {
                    'page': attraction,
                    'params': {
                        'offset': offset,
                        'geoId': geo,
                        'detailId': detail,
                    },
                },
            },
            'extensions': {
                'preRegisteredQueryId': '8ff5481f70241137',
            },
        },
        {
            'variables': {
                'route': {
                    'page': attraction,
                    'params': {
                        'offset': offset,
                        'geoId': geo,
                        'detailId': detail,
                    },
                },
                'currencyCode': 'USD',
            },
            'extensions': {
                'preRegisteredQueryId': '510e5b9576ce086f',
            },
        },
        {
            'variables': {
                'request': {
                    'tracking': {
                        'screenName': attraction,
                        'pageviewUid': 'd4b81d9a-7cf8-458a-aeea-fe7da8977452',
                    },
                    'routeParameters': {
                        'contentType': content_type,
                        'contentId': detail,
                        'pagee': '10',
                    },
                    'clientState': None,
                    'updateToken': update_token,
                },
                'commerce': {},
                'sessionId': 'FAE1CD3A082907F062F50720FCA3AB2C',
                'tracking': {
                    'screenName': attraction,
                    'pageviewUid': 'd4b81d9a-7cf8-458a-aeea-fe7da8977452',
                },
                'currency': 'USD',
                'currentGeoPoint': None,
                'unitLength': 'MILES',
            },
            'extensions': {
                'preRegisteredQueryId': '311a30d9581f524a',
            },
        },
        {
            'variables': {
                'page': attraction,
                'locale': 'en-US',
                'platform': 'tablet',
                'id': detail,
                'urlRoute': url,
            },
            'extensions': {
                'preRegisteredQueryId': 'd194875f0fc023a6',
            },
        },
    ]

    return (cookies, headers, json_data)

def request_headers():
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
     
    return (cookies, headers)


def profile_json_data(username):
    # json_data = [
    #     {
    #         'variables': {
    #             'experimentKeys': [
    #                 'datadome_envoy_bucketing_1697032802',
    #             ],
    #         },
    #         'extensions': {
    #             'preRegisteredQueryId': '21d24a06e22ceef2',
    #         },
    #     },
    #     {
    #         'variables': {
    #             'experimentKeys': [
    #                 'amazon_publisher_audiences_1695657425',
    #             ],
    #         },
    #         'extensions': {
    #             'preRegisteredQueryId': '21d24a06e22ceef2',
    #         },
    #     },
    #     {
    #         'variables': {
    #             'experimentKeys': [
    #                 'braze_sdk_feature_toggle_1706895311',
    #             ],
    #         },
    #         'extensions': {
    #             'preRegisteredQueryId': '21d24a06e22ceef2',
    #         },
    #     },
    #     {
    #         'variables': {
    #             'page': 'Profile',
    #             'locale': 'en-US',
    #             'platform': 'tablet',
    #             'id': None,
    #             'urlRoute': '/Profile/Navigate424997?fid=d68c9e21-2d62-4240-80bb-92bcc2b409a3',
    #         },
    #         'extensions': {
    #             'preRegisteredQueryId': 'd194875f0fc023a6',
    #         },
    #     },
    #     {
    #         'variables': {
    #             'page': 'Profile',
    #             'platform': 'tablet',
    #         },
    #         'extensions': {
    #             'preRegisteredQueryId': 'b4613962d98df032',
    #         },
    #     },
    #     {
    #         'variables': {
    #             'userName': 'Navigate424997',
    #         },
    #         'extensions': {
    #             'preRegisteredQueryId': 'ecb4eb0c5349550c',
    #         },
    #     },
    #     {
    #         'variables': {
    #             'allowedTypes': [],
    #             'locationId': 1,
    #             'owner': 'E28CF4070A4C056580C6EF0352B4B3F4',
    #             'placement': 'PROFILE',
    #             'puid': '27a7269e-3fdc-4814-98b1-fe0b2ad6b03c',
    #             'sessionType': 'DESKTOP',
    #             'sectionId': '4612a389-fdcc-4446-8626-327e8ce53b94_0',
    #         },
    #         'extensions': {
    #             'preRegisteredQueryId': 'c1178a2624e1fd8e',
    #         },
    #     },
    #     {
    #         'variables': {
    #             'username': 'Navigate424997',
    #         },
    #         'extensions': {
    #             'preRegisteredQueryId': 'd06b57a5164dd54b',
    #         },
    #     },
    #     {
    #         'variables': {
    #             'username': 'Navigate424997',
    #             'reset': False,
    #             'allowedTypes': [],
    #             'sessionType': 'TABLET_WEB',
    #             'puid': '27a7269e-3fdc-4814-98b1-fe0b2ad6b03c',
    #             'preloadForumPostIds': [],
    #             'preloadLinkPostIds': [],
    #             'preloadPhotoIds': [],
    #             'preloadMediaBatchIds': [],
    #             'preloadRepostIds': [],
    #             'preloadReviewIds': [],
    #             'preloadVideoIds': [],
    #             'restoreFromFeedId': 'd68c9e21-2d62-4240-80bb-92bcc2b409a3',
    #             'socialReference': True,
    #             'shouldFetchTripsStatuses': False,
    #         },
    #         'extensions': {
    #             'preRegisteredQueryId': '991491c725fc1626',
    #         },
    #     },
    #     {
    #         'variables': {
    #             'currency': 'USD',
    #             'trafficSourceInfo': {
    #                 'mcid': None,
    #                 'servletName': 'Profile',
    #                 'sessionId': '7ED23334028EBCDF6E6646243E27F2A5',
    #                 'referrer': 'https://www.tripadvisor.com/Attraction_Review-g298570-d12276424-Reviews-Vespalicious-Kuala_Lumpur_Wilayah_Persekutuan.html',
    #             },
    #         },
    #         'extensions': {
    #             'preRegisteredQueryId': '3c36e4d2aa11f4c7',
    #         },
    #     },
    #     {
    #         'variables': {
    #             'request': [
    #                 {
    #                     'timestamp': '1708874109041',
    #                 },
    #             ],
    #         },
    #         'extensions': {
    #             'preRegisteredQueryId': '7e232d3cbc211ec6',
    #         },
    #     },
    #     {
    #         'variables': {
    #             'request': [
    #                 {
    #                     'locationIds': [],
    #                     'timestamp': '1708874109288',
    #                     'pageContentId': None,
    #                     'pageType': None,
    #                 },
    #             ],
    #         },
    #         'extensions': {
    #             'preRegisteredQueryId': 'bc99048f6dd84da1',
    #         },
    #     },
    # ]

    cookies = {
        'datadome': 'HzoMS4d9zQPohVkHwNryHUurcq1LMYl_ZZzuN8JB~~RYPoHo9Dv62h9oNaemiAPBdkzhm5ylx77eFUoQVaff83VcOSgNQzHhT1pIpSaFYNBurftfCLvn0E6qmxHEBo2M',
        'TASameSite': '1',
        'TAUnique': '%1%enc%3A5yphkXU%2B%2BLE12Ai27pmPshWwJnM%2F%2BIoJceiJCLjggzgTdR%2F89nytZX2VzCc4LdYwNox8JbUSTxk%3D',
        'TASSK': 'enc%3AAOZhcd88jgZx5Gsg6ghAZ%2BnEIw2nWbyNt2a86V%2Fxaoe%2B3el4fX7x%2BXx8BXZQ3NQEgAraizZaeCeD5XEXSa%2FQLuiqBYIWJ61wCvDFJ4YoStZf82FuVX1vmnFVCf2MVuixtg%3D%3D',
        'TATrkConsent': 'eyJvdXQiOiJBRFYsU09DSUFMX01FRElBIiwiaW4iOiJBTkEsRlVOQ1RJT05BTCJ9',
        'TATravelInfo': 'V2*A.2*MG.-1*HP.2*FL.3*DSM.1707312617200*RS.1',
        'TART': '%1%enc%3A9zZlyhdOj38KSphF3FXw6xYJcETBXMBq%2Ffm1piT%2FWi%2BVCaMzj%2B1f6b%2F2uGqXJTalW1JxtpsONWQ%3D',
        'VRMCID': '%1%V1*id.10568*llp.%2FAttractionProductReview-g298570-d19765373-Country_Batu_Cave_Half_Day_Tour_SIC_Join_In_Tour-Kuala_Lumpur_Wilayah_Persekutuan%5C.html*e.1709372788257',
        'TADCID': 'QXqLUkLHzHBJmrMRABQCmq6heh9ZSU2yA8SXn9Wv5HvQn-Y33B4xfO7p1i-Qw5kkJpDObtcP915YMtW0N5AcPkh-75RzvqnB80k',
        'TASID': '7ED23334028EBCDF6E6646243E27F2A5',
        '_abck': '4586BF59B484F2C5F4E0FBCB035DD521~-1~YAAQhpbTZwNXpFWNAQAACwPV4AuWSOk/4m1kYCuf99W+YpT/H0YtrxRPKuDV3YGFvEBOFWKGgn+DSkZOCv5u8ny3waAqrATbRbGN975UAJq9ufB1YElaLt/0TJKzSYHH4DszaR/XTrmwGq53W9ue0RVtICtFs4GNqSbugYiEc/c2MS4T2KdWX1svIc9Dn9ZyOM5DEMUBT5n7x08J+uNgYdpJgnhAu/cE3yLxCoVEvKFsXk3j+MuYAxmCIeQLJZWagfQI0p3DZ86IVJJpJul506ZNmEY73rwOavOgQfGWBufb6mfslM2ry29u1xUkU8hNzLZjXc2/divAduwKaUQ4ZkdZ/mFub42+zFEvYpFSHjC+mKbTU0LTBPORnPUAt5Ell42daY/WU7/BvVn/CtM=~-1~-1~-1',
        'bm_sz': '055476BCC7F4EAAD393E17082546A6AB~YAAQhpbTZwRXpFWNAQAACwPV4BYOO8wQB7xuFtn7QN8nIGH9u4EE2J3flQWho5AWkDK2InqNTJNiEUHWXjcyLoiBqC9QWcRP6K4PxAf10/A4YJkk4Sldlm6z+YW8p8867ZlWjMqhhIiJo914kTM+WJyCIBTSg7sNButWX/n/eG28nQmbL2+hIu8dl896O6/E13Y2RTQdpS6mCT7VvnazbxnSJJTtujgKLtLdsW+Fc+sUt24g69d71Aqs1PmObPVp/dcjj24wPtSwI02AccPZcbT2miqY23TnbShy8ep+SpBZJUf7b8H5YPhf2RUFcX5l6pql2IVDEr5sSDFNoW/ZvhejsckrtbQk/uls5Sr++zCW7O5dM25jOCwriQ==~4604467~3552070',
        'PAC': 'AMDRD6nJxe4c542wticy1zAkYeizseNInXYimPOHrBs9mRllihhWKvERTM6YPVYqQyKzC_QZipzkEqbcsA-C5rT3ZV7pukd59-tkxKprgBDFtsCdu5XOobjwDGeyYJ5eCcUFJmqc5fLLqhngTfE2d-M%3D',
        'SRT': 'TART_SYNC',
        'ServerPool': 'R',
        'PMC': 'V2*MS.29*MD.20240207*LD.20240225',
        'OptanonConsent': 'isGpcEnabled=1&datestamp=Sun+Feb+25+2024+21%3A04%3A26+GMT%2B0545+(Nepal+Time)&version=202310.2.0&browserGpcFlag=1&isIABGlobal=false&hosts=&consentId=0d5f4688-c039-4d12-bbaa-656e08345da8&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A0&AwaitingReconsent=false',
        '__vt': 'uBx-KpNRwE0G3XPIABQCwRB1grfcRZKTnW7buAoPsSuuTvKqwzfSq4CJU7Vjphmifrmns4q4Nv2HJHXep43kzzcm_np6LKxYM_CWFk4F7SdBN86gyGmKPDtglnNZPYUAbrSKd3fEzSI07viIf8WLIg0b_g',
        'roybatty': 'TNI1625!AGaopfC8r%2BXkGioblp2qWcBh6r5WCHKCgb%2FKsF%2FYhl7G1iA%2FOfunwpn2paNrEWJlIrR%2BTJTrsNVQkx1t6PHg6KYpQROLtEfnx6p1ATq4CLVFrANc8j8vs5BJC3JB0U3m39XWBcRuchH3AL9Vr2Ru0lmwQYdo2alOcbh46gt%2BXEfwYD%2BwwUbfWxJ2M4uRfh%2BNKw%3D%3D%2C1',
        'TASession': 'V2ID.7ED23334028EBCDF6E6646243E27F2A5*SQ.20*LS.DemandLoadAjax*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*TRA.true*EAU._',
        'TAUD': 'LA-1707309208069-1*RDD-1-2024_02_07*HDD-3409041-2024_02_18.2024_02_19*ARC-96486623*LG-1565744525-2.1.F.*LD-1565744526-.....',
    }

    headers = {
        'authority': 'www.tripadvisor.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        # 'cookie': 'datadome=HzoMS4d9zQPohVkHwNryHUurcq1LMYl_ZZzuN8JB~~RYPoHo9Dv62h9oNaemiAPBdkzhm5ylx77eFUoQVaff83VcOSgNQzHhT1pIpSaFYNBurftfCLvn0E6qmxHEBo2M; TASameSite=1; TAUnique=%1%enc%3A5yphkXU%2B%2BLE12Ai27pmPshWwJnM%2F%2BIoJceiJCLjggzgTdR%2F89nytZX2VzCc4LdYwNox8JbUSTxk%3D; TASSK=enc%3AAOZhcd88jgZx5Gsg6ghAZ%2BnEIw2nWbyNt2a86V%2Fxaoe%2B3el4fX7x%2BXx8BXZQ3NQEgAraizZaeCeD5XEXSa%2FQLuiqBYIWJ61wCvDFJ4YoStZf82FuVX1vmnFVCf2MVuixtg%3D%3D; TATrkConsent=eyJvdXQiOiJBRFYsU09DSUFMX01FRElBIiwiaW4iOiJBTkEsRlVOQ1RJT05BTCJ9; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*DSM.1707312617200*RS.1; TART=%1%enc%3A9zZlyhdOj38KSphF3FXw6xYJcETBXMBq%2Ffm1piT%2FWi%2BVCaMzj%2B1f6b%2F2uGqXJTalW1JxtpsONWQ%3D; VRMCID=%1%V1*id.10568*llp.%2FAttractionProductReview-g298570-d19765373-Country_Batu_Cave_Half_Day_Tour_SIC_Join_In_Tour-Kuala_Lumpur_Wilayah_Persekutuan%5C.html*e.1709372788257; TADCID=QXqLUkLHzHBJmrMRABQCmq6heh9ZSU2yA8SXn9Wv5HvQn-Y33B4xfO7p1i-Qw5kkJpDObtcP915YMtW0N5AcPkh-75RzvqnB80k; TASID=7ED23334028EBCDF6E6646243E27F2A5; _abck=4586BF59B484F2C5F4E0FBCB035DD521~-1~YAAQhpbTZwNXpFWNAQAACwPV4AuWSOk/4m1kYCuf99W+YpT/H0YtrxRPKuDV3YGFvEBOFWKGgn+DSkZOCv5u8ny3waAqrATbRbGN975UAJq9ufB1YElaLt/0TJKzSYHH4DszaR/XTrmwGq53W9ue0RVtICtFs4GNqSbugYiEc/c2MS4T2KdWX1svIc9Dn9ZyOM5DEMUBT5n7x08J+uNgYdpJgnhAu/cE3yLxCoVEvKFsXk3j+MuYAxmCIeQLJZWagfQI0p3DZ86IVJJpJul506ZNmEY73rwOavOgQfGWBufb6mfslM2ry29u1xUkU8hNzLZjXc2/divAduwKaUQ4ZkdZ/mFub42+zFEvYpFSHjC+mKbTU0LTBPORnPUAt5Ell42daY/WU7/BvVn/CtM=~-1~-1~-1; bm_sz=055476BCC7F4EAAD393E17082546A6AB~YAAQhpbTZwRXpFWNAQAACwPV4BYOO8wQB7xuFtn7QN8nIGH9u4EE2J3flQWho5AWkDK2InqNTJNiEUHWXjcyLoiBqC9QWcRP6K4PxAf10/A4YJkk4Sldlm6z+YW8p8867ZlWjMqhhIiJo914kTM+WJyCIBTSg7sNButWX/n/eG28nQmbL2+hIu8dl896O6/E13Y2RTQdpS6mCT7VvnazbxnSJJTtujgKLtLdsW+Fc+sUt24g69d71Aqs1PmObPVp/dcjj24wPtSwI02AccPZcbT2miqY23TnbShy8ep+SpBZJUf7b8H5YPhf2RUFcX5l6pql2IVDEr5sSDFNoW/ZvhejsckrtbQk/uls5Sr++zCW7O5dM25jOCwriQ==~4604467~3552070; PAC=AMDRD6nJxe4c542wticy1zAkYeizseNInXYimPOHrBs9mRllihhWKvERTM6YPVYqQyKzC_QZipzkEqbcsA-C5rT3ZV7pukd59-tkxKprgBDFtsCdu5XOobjwDGeyYJ5eCcUFJmqc5fLLqhngTfE2d-M%3D; SRT=TART_SYNC; ServerPool=R; PMC=V2*MS.29*MD.20240207*LD.20240225; OptanonConsent=isGpcEnabled=1&datestamp=Sun+Feb+25+2024+21%3A04%3A26+GMT%2B0545+(Nepal+Time)&version=202310.2.0&browserGpcFlag=1&isIABGlobal=false&hosts=&consentId=0d5f4688-c039-4d12-bbaa-656e08345da8&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A0&AwaitingReconsent=false; __vt=uBx-KpNRwE0G3XPIABQCwRB1grfcRZKTnW7buAoPsSuuTvKqwzfSq4CJU7Vjphmifrmns4q4Nv2HJHXep43kzzcm_np6LKxYM_CWFk4F7SdBN86gyGmKPDtglnNZPYUAbrSKd3fEzSI07viIf8WLIg0b_g; roybatty=TNI1625!AGaopfC8r%2BXkGioblp2qWcBh6r5WCHKCgb%2FKsF%2FYhl7G1iA%2FOfunwpn2paNrEWJlIrR%2BTJTrsNVQkx1t6PHg6KYpQROLtEfnx6p1ATq4CLVFrANc8j8vs5BJC3JB0U3m39XWBcRuchH3AL9Vr2Ru0lmwQYdo2alOcbh46gt%2BXEfwYD%2BwwUbfWxJ2M4uRfh%2BNKw%3D%3D%2C1; TASession=V2ID.7ED23334028EBCDF6E6646243E27F2A5*SQ.20*LS.DemandLoadAjax*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*TRA.true*EAU._; TAUD=LA-1707309208069-1*RDD-1-2024_02_07*HDD-3409041-2024_02_18.2024_02_19*ARC-96486623*LG-1565744525-2.1.F.*LD-1565744526-.....',
        'origin': 'https://www.tripadvisor.com',
        'referer': f'https://www.tripadvisor.com/Profile/{username}',
        'sec-ch-ua': '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    json_data = [
        {
            'variables': {
                'userName': username,
            },
            'extensions': {
                'preRegisteredQueryId': 'ecb4eb0c5349550c',
            },
        },
        {
            'variables': {
                'allowedTypes': [],
                'locationId': 1,
                'owner': 'E28CF4070A4C056580C6EF0352B4B3F4',
                'placement': 'PROFILE',
                'puid': '096e1981-9a04-469e-975e-fb94efc023b6',
                'sessionType': 'DESKTOP',
                'sectionId': 'a0de2f22-49ba-4377-9109-5853a19c7eae_0',
            },
            'extensions': {
                'preRegisteredQueryId': 'c1178a2624e1fd8e',
            },
        },
        {
            'variables': {
                'username': username,
            },
            'extensions': {
                'preRegisteredQueryId': 'd06b57a5164dd54b',
            },
        },
        {
            'variables': {
                'username': username,
                'reset': True,
                'allowedTypes': [],
                'sessionType': 'TABLET_WEB',
                'puid': '096e1981-9a04-469e-975e-fb94efc023b6',
                'preloadForumPostIds': [],
                'preloadLinkPostIds': [],
                'preloadPhotoIds': [],
                'preloadMediaBatchIds': [],
                'preloadRepostIds': [],
                'preloadReviewIds': [],
                'preloadVideoIds': [],
                'socialReference': True,
                'shouldFetchTripsStatuses': False,
            },
            'extensions': {
                'preRegisteredQueryId': '991491c725fc1626',
            },
        },
    ]

    return (cookies, headers, json_data)