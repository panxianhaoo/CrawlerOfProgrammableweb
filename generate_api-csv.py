import json
import pandas as pd

f = open('./api_data.json', 'r')
items = f.readlines()
# keysset = set()
# for i in items:
#     json2dict = json.loads(i)
#     for it in json2dict.keys():
#         keysset.add(it)
# print(keysset)
# print(len(keysset))
columns = ['Name', 'Primary Category', 'Secondary Categories', 'API Provider',
           'API Endpoint', 'API Portal / Home Pag', 'Docs Home Page URL', 'Terms Of Service URL',
           'Supported Request Formats', 'Supported Response Formats',
           'Is This an Unofficial API?', 'Is the API Design/Description Non-Proprietary ?',
           'Restricted Access ( Requires Provider Approval )',
           'Is This a Hypermedia API?', 'SSL Support', 'Architectural Sty', 'Twitter URL', 'Authentication Mod']
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
df = df.rename(columns={'API Portal / Home Pag': 'API Portal / Home Page',
                        'Is the API Design/Description Non-Proprietary ?': 'Non-Proprietary',
                        'Restricted Access ( Requires Provider Approval )': 'Restricted Access',
                        'Architectural Sty': 'Architectural Style', 'Authentication Mod': 'Authentication Model'})


def handle(item):
    item = str(item)
    if '</a>' in item:
        return item.split('</a>')[0]
    else:
        return item


def handle_ye(item):
    item = str(item)
    if item == 'Ye':
        return item + 's'
    else:
        return item


df['Secondary Categories'] = df['Secondary Categories'].map(handle)
df['Is This an Unofficial API?'] = df['Is This an Unofficial API?'].map(handle_ye)
df['Non-Proprietary'] = df['Non-Proprietary'].map(handle_ye)
df['Restricted Access'] = df['Restricted Access'].map(handle_ye)
df['Is This a Hypermedia API?'] = df['Is This a Hypermedia API?'].map(handle_ye)
df['Is This a Hypermedia API?'] = df['Is This a Hypermedia API?'].map(handle_ye)
df['SSL Support'] = df['SSL Support'].map(handle_ye)
df.to_csv('./api.csv', encoding='UTF-8')
