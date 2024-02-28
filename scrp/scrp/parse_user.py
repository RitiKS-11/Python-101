import requests, json

from utils.headers import profile_json_data

def user_request(username):
    """ Send a request to get json data """
    cookies, headers, json_data = profile_json_data(username)
    response = requests.post('https://www.tripadvisor.com/data/graphql/ids', cookies=cookies, headers=headers, json=json_data, timeout=10)
    
    return response.json()


def parse_content(response):
    json_response = response
    reviews_links = dict()
    
    user_id = json_response[2]['data']['memberProfiles'][0]['id']
    username = json_response[2]['data']['memberProfiles'][0]['username']
    total_reveiw = json_response[3]['data']['memberProfiles'][0]['contributionCounts']['sumReview']
    location = json_response[3]['data']['memberProfiles'][0]['hometown']['location']
    achievement_counts = json_response[3]['data']['memberProfiles'][0]['achievementCounts']['points']
    created = json_response[3]['data']['memberProfiles'][0]['created']
    url = json_response[3]['data']['memberProfiles'][0]['route']['url']
    reviews = json_response[3]['data']['socialFeed']['sections']
    for index, review in enumerate(reviews):
        reviews_links[f'url{index}'] = review['items'][0]['object']['route']['url']

    return {'user_id':user_id, 'username':username, 'total_review':total_reveiw, 'location':location, 
            'achievement_counts':achievement_counts, 'created':created, 'url':url, 'review_links': reviews_links}

def save_user_json(data):
    with open('user.json', 'w') as file:
        json.dump(data, file, indent=4)


def parse_user(filepath):
    results = []

    with open(filepath) as file:
        reviews = json.load(file)

    for review in reviews:
        name = review['name'].replace(' ','')
        response = user_request(name)

        try:
            err = response[0]['errors']
            continue
        except:
            pass
        
        results.append(parse_content(response))

    save_user_json(results)

    



if __name__ == "__main__":
    # user_request('Navigate424997')
    parse_user('data.json')