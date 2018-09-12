from restapi import Search, Trumpia

# initialize object from searchkey.py
api = Search()
trm = Trumpia()

keys = ['spiderman']

# example functions
results_k = api.keywords(keys, 'United States')
print(results_k[1])
print(len(results_k))
print('-----------------')
#results_kr = api.keywords_related('waffles','US')
#print(results_kr)
#print('-------')
# send email
#trm.sendEmail('vu.kevin00@gmail.com', 'body message', 'subject')
