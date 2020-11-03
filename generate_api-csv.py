import json
import pandas as pd

f = open('api_data.json', 'r')
items = f.readlines()
columns = ['Name', 'Primary Category', 'Secondary Categories', 'API Provider',
           'API Endpoint', 'API Portal / Home Page', 'Docs Home Page URL', 'Terms Of Service URL',
           'Supported Request Formats', 'Supported Response Formats',
           'Is This an Unofficial API?', 'Is the API Design/Description Non-Proprietary ?',
           'Restricted Access ( Requires Provider Approval )',
           'Is This a Hypermedia API?', 'SSL Support', 'Architectural Style', 'Twitter URL', 'Authentication Model']
df = pd.DataFrame(columns=columns)
count = 0
for i in items:
    json2dict = json.loads(i)
    df = df.append(json2dict, ignore_index=True)
    count += 1
    print(count)
    # if count == 500:
    #     break
df = df.loc[:, columns]
df.to_csv('./api.csv', encoding='UTF-8')
