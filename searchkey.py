from client import RestClient
#You can download this file from here https://api.dataforseo.com/_examples/python/_python_Client.zip

#Instead of 'login' and 'password' use your credentials from https://my.dataforseo.com/login
client = RestClient('vu.kevin@csu.fullerton.edu', 'LD87rm8Od9dfWnVn')

class Search():
    def stats(self, word, location):
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