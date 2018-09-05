from client import RestClient

client = RestClient('vu.kevin@csu.fullerton.edu', 'LD87rm8Od9dfWnVn')

# Search class has modules for different functions
class Search():
    # https://docs.dataforseo.com/#live-data
    def volume(self, word, location):
        keywords_list = [
            dict(
                language="en",
                loc_name_canonical=location,
                key=word
            ),
        ]

        response = client.post("/v2/kwrd_sv", dict(data=keywords_list))
        if response["status"] == "error":
            print("error. Code: %d Message: %s" % (response["error"]["code"], response["error"]["message"]))
        else:
            print(response["results"])

    # https://docs.dataforseo.com/#live-data53
    def keywords(self, word, location):
        keywords_list = [
            dict(
                language="en",
                loc_name_canonical=location,
                keys=word
            )
        ]
        response = client.post("/v2/kwrd_for_keywords", dict(data=keywords_list))
        if response["status"] == "error":
            print("error. Code: %d Message: %s" % (response["error"]["code"], response["error"]["message"]))
        else:
            print(response["results"])

    # https://docs.dataforseo.com/#get-related-keywords
    def similar_keywords(self, word, location):
        rnd = Random() #you can set as "index of post_data" your ID, string, etc. we will return it with all results.
        post_data = dict()

        post_data[rnd.randint(1, 30000000)] = dict(
            keyword=word,
            country_code="US",
            language="en",
            depth=2,
            limit=1,
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
            print(response["results"])