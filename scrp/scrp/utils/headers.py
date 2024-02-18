

def json_header(url, geo, detail, offset):
    cookies = {
            'datadome': 'HzoMS4d9zQPohVkHwNryHUurcq1LMYl_ZZzuN8JB~~RYPoHo9Dv62h9oNaemiAPBdkzhm5ylx77eFUoQVaff83VcOSgNQzHhT1pIpSaFYNBurftfCLvn0E6qmxHEBo2M',
            'TASameSite': '1',
            'TAUnique': '%1%enc%3A5yphkXU%2B%2BLE12Ai27pmPshWwJnM%2F%2BIoJceiJCLjggzgTdR%2F89nytZX2VzCc4LdYwNox8JbUSTxk%3D',
            'TASSK': 'enc%3AAOZhcd88jgZx5Gsg6ghAZ%2BnEIw2nWbyNt2a86V%2Fxaoe%2B3el4fX7x%2BXx8BXZQ3NQEgAraizZaeCeD5XEXSa%2FQLuiqBYIWJ61wCvDFJ4YoStZf82FuVX1vmnFVCf2MVuixtg%3D%3D',
            'VRMCID': '%1%V1*id.10568*llp.%2FRestaurant_Review-g293890-d2343431-Reviews-Kathmandu_Grill_Restaurant_And_Wine_Bar-Kathmandu_Kathmandu_Valley_Bagmati_Zone_C%5C.html*e.1707917361815',
            'TATravelInfo': 'V2*AY.2024*AM.2*AD.18*DY.2024*DM.2*DD.19*A.2*MG.-1*HP.2*FL.3*DSM.1707312617200*RS.1',
            'TADCID': 't_A7Fq5GDiSnj2gxABQCmq6heh9ZSU2yA8SXn9Wv5Hui4kh3HJ-CDz2wi2pu6xvSpxvOB_CvMT-DLLOzMzL6Ze7twW-DTyCL1wI',
            'TASID': '956C011FB28514BB4C6AF6D750A0A15C',
            '_abck': '4586BF59B484F2C5F4E0FBCB035DD521~-1~YAAQhpbTZ41vfFWNAQAAU6b0tgtfc0NWeW9qESgxmNvHDVWju69ktXoTr2OS8ue2nTjNTFuoawIq6anQlcA1iIUSgTTGffzmK/PDwxnFI/FCbGiUB15Hri3/3hZJwjFVPZ4ZYHBoMPxBg3qa8G286QebQMkyk3McQoJjALYSNksi9SsiuJOjNvA7i6PELXQi42lZOPsFVm/i2wra/fBT6Eww14LwtKHlCS8u9Fh2HVMVOosWVT2DGOl3O68INGG+GdSk5MgxFAVgzXLGQfpO7nZZa7VqOiN5GOf5a7d2RKcOgODCeD9YvlWHh8Q2XGxwiBNhED2hmzBGxoHPZFdbOHPsDB05JHL2DR4ga6tR5ZuwUYHurnVP2sx2ah6C9Uh14y9EUB8n6Rga+G8tJ2A=~-1~-1~-1',
            'bm_sz': '5FE88A0CB99848B89573E8AC9126F632~YAAQhpbTZ45vfFWNAQAAU6b0thZfyWrg8o58JbdrHEH1J/I3JKcvaNbl+EkzVjMc5Fv+ESqaWwoO9HgPBgfO8yBtfm268xyO/qij7SRiArgqwx6cYOfB61KjI3Os1infR60vRIW5juTwjPgyKyfCke1pph3w4teMG+dsPmXfuZOOTt4JzGIZev02xcPhuLYxMhlsOT8wmugLMH9ZAKd7YFvfNkVtBvCXCWF7jr8OvMAuCylRXwP7aY1PaUlxuo/9jGxmT/nvb8SsejmY3Xg7ijaak7Ihet4hMhShbuaG3w8kNW+CHgghyWu4nHjQQSpU62ZI5B/AOMNgZoceJdf9+zCnX72fMjcDfVZk47to3zBbMsDwub4lmg04Aw==~3159363~4470579',
            'TATrkConsent': 'eyJvdXQiOiJBRFYsU09DSUFMX01FRElBIiwiaW4iOiJBTkEsRlVOQ1RJT05BTCJ9',
            'PAC': 'AEL0dlSrz7nAz4NVwcPSMyO9nRdXE417rweACKCzu4Pb7qXxSEa6CPlxfP5lGRPXLvex6QkcF80fVVW-a1MmuHwC1BZAxo_VPpI_ictvSwSdDCqxaPlgePURIABvSMdBiA%3D%3D',
            'TART': '%1%enc%3A9zZlyhdOj3%2BKWMwYS5BtTZuQ%2FOkdlKsJ4mFrh%2BM5vGkFXMzUVl4X9c0ppUBuDioOyx9HjuV9fk0%3D',
            'ServerPool': 'X',
            'PMC': 'V2*MS.29*MD.20240207*LD.20240217',
            'TAUD': 'LA-1707309208069-1*RDD-1-2024_02_07*HDD-3409041-2024_02_18.2024_02_19*ARC-96486623*LG-864285898-2.1.F.*LD-864285899-.....',
            'OptanonConsent': 'isGpcEnabled=1&datestamp=Sat+Feb+17+2024+18%3A23%3A16+GMT%2B0545+(Nepal+Time)&version=202310.2.0&browserGpcFlag=1&isIABGlobal=false&hosts=&consentId=0d5f4688-c039-4d12-bbaa-656e08345da8&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A0&AwaitingReconsent=false',
            'TASession': 'V2ID.956C011FB28514BB4C6AF6D750A0A15C*SQ.4*LS.AttractionProductReview*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*TRA.true*LD.12962337*EAU._',
            '__vt': 'hgzj2PZGEe1wujV1ABQCwRB1grfcRZKTnW7buAoPsSuAqNdP0RMr-zjkDIsaL2aA146mmFb561uDr7lV3KvL4PxncAeL_BkRAIinFKjVX3jTGEmiGZpIPCacjY-Ly_DF25hm42wvYx7gz-K55x4ZXZV1tw',
        }

    headers = {
            'authority': 'www.tripadvisor.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.5',
            'content-type': 'application/json',
            'origin': 'https://www.tripadvisor.com',
            'referer': f'https://www.tripadvisor.com{url}',
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
                    'page': 'AttractionProductReview',
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
                        'page': 'AttractionProductReview',
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
                        'page': 'AttractionProductReview',
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
                    'pageName': 'AttractionProductReview',
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
                        'page': 'AttractionProductReview',
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
                    'page': 'AttractionProductReview',
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
                        'page': 'AttractionProductReview',
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
                    'request': {
                        'tracking': {
                            'screenName': 'AttractionProductReview',
                            'pageviewUid': 'ef4c58ef-0087-47a2-801c-5cafecfc927a',
                        },
                        'routeParameters': {
                            'contentType': 'attraction_product',
                            'contentId': '12962337',
                            'pagee': '40',
                        },
                        'clientState': None,
                        'updateToken': 'eyJ2ZXIiOiJ2MiIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2IiwidmVyc2lvbiI6IjEifQ.eyJvYmplY3QiOiJ7XCJAY1wiOlwiLlBhZ2luZ1VwZGF0ZVRva2VuXCIsXCJjbHVzdGVySWRzXCI6W1wiUE9JX1JFVklFV1NfV0VCXCJdLFwicHJvdmlkZXJVcGRhdGVUb2tlbnNcIjp7XCJUUkFOU0xBVEVfUkVWSUVXU1wiOntcIkBjXCI6XCJjb20udHJpcGFkdmlzb3Iuc2VydmljZS5hcHMuYWRhcHRlcnMuaG90ZWxzLlRyYW5zbGF0ZVJldmlld3NUb2tlblwiLFwic2hvdWxkVHJhbnNsYXRlXCI6dHJ1ZSxcInJldmlld0lkc1wiOls4NjYxNDEzODcsODY0MTc5NzEyLDg2MzQ2MDU3MCw4NjMzNTU0MTMsODU5ODI1MDEzLDg0MDYyNjM2MCw4MTkyODQzOTgsNzcyMzIyNjA2LDc1OTA3ODgyOSw3NTgwMDU3MTNdLFwidG90YWxDb3VudFwiOjE2MSxcInNob3dUcmFuc2xhdGVIZWFkZXJcIjpmYWxzZSxcImZhdm9yaXRlUmV2aWV3SWRcIjpudWxsfX0sXCJwYWdlSW5kZXhcIjo3MCxcInR5cGVcIjpcIlBBR0lOQVRJT05cIixcInBvbGxpbmdTZXF1ZW5jZU51bVwiOjB9In0.MjRlNTU4MmItMGIyNS00YTI1LTk4NDUtYTY0YjFiNzYxODc0Lk1FVUNJUURZOWh5Mmc5Uy14T0UtY2FUSlAyWDdiWjBIVWNoRkZtdVR6eEIwT1lXOEVBSWdYWE5meHM3RlRVRmlzbnp4NDRiRGxGaldVd1E0VWFDSDhYTDRqVmc4Z3lj',
                    },
                    'commerce': {},
                    'sessionId': '956C011FB28514BB4C6AF6D750A0A15C',
                    'tracking': {
                        'screenName': 'AttractionProductReview',
                        'pageviewUid': 'ef4c58ef-0087-47a2-801c-5cafecfc927a',
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
                    'page': 'AttractionProductReview',
                    'locale': 'en-US',
                    'platform': 'mobileweb',
                    'id': '12962337',
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