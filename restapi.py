from client import RestClient
import json, logging, requests, random

client = RestClient('vu.kevin@csu.fullerton.edu', 'LD87rm8Od9dfWnVn')

# Search class has modules for different functions
class Search():
    # https://docs.dataforseo.com/#get-related-keywords
    def keywords_related(self, word, location):
        rnd = random.Random() #you can set as "index of post_data" your ID, string, etc. we will return it with all results.
        post_data = dict()

        post_data[rnd.randint(1, 30000000)] = dict(
            keyword=word,
            country_code='US',
            language="en",
            depth=1,
            limit=3,
            offset=0,
            orderby="cpc,desc",
            filters=[
                ["cpc", ">", 0],
                "or", 
                [
                    ["search_volume", ">", 0],
                    "and",
                    ["search_volume", "<=", 1000]
                ]
            ]
        )

        response = client.post("/v2/kwrd_finder_related_keywords_get", dict(data=post_data))
        if response["status"] == "error":
            print("error. Code: %d Message: %s" % (response["error"]["code"], response["error"]["message"]))
        else:
            return response["results"]

class Trumpia():
    def __init__(self):
        self.apiKey = '7f5a72d074cff3222bfa0b079af236fc'
        self.username = 'vuskeedoo'
        self.header = {'Content-Type':'application/json',
                        'x-Apikey':self.apiKey}

    def sendEmail(self, to_email, msg_body, msg_subject):
        url = 'https://api.trumpia.com/rest/v1/' + self.username + '/email'
        body = {'from':'apisupport@mytrum.com', 'to':to_email,'subject':msg_subject, 'content_html':msg_body}
        try:
            resp = requests.request('PUT', url, headers =self.header, json=body)
            resp.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return print('Error: ' + str(e))
        if 'request_id' in resp.json():
            print('request id returned')
            return resp.json()['request_id']
        else:
            print('request id not returned')
            return None

