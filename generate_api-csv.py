import json
import pandas as pd
from tqdm import tqdm


def desc_format(s):
    if s is None:
        return ''
    s = s.lstrip('<div class=\"api_description tabs-header_description\">')
    if s.startswith('['):
        s = s[s.find(']') + 1:-7]
    else:
        s = s[:-7]
    s = s.replace('\n', ' ')
    return s.strip()


f = open('api_data.json', 'r')
items = f.readlines()
columns = ['Name', 'Desc', 'Primary Category', 'Followers', 'Secondary Categories', 'API Provider', 'API Endpoint',
           'API Portal / Home Page', 'Docs Home Page URL', 'Terms Of Service URL',
           'Supported Request Formats', 'Supported Response Formats',
           'Is This an Unofficial API?', 'Is the API Design/Description Non-Proprietary ?',
           'Restricted Access ( Requires Provider Approval )',
           'Is This a Hypermedia API?', 'SSL Support', 'Architectural Style', 'Twitter URL', 'Authentication Model']
df = pd.DataFrame(columns=columns)
for i in tqdm(items):
    json2dict = json.loads(i)
    df = df.append(json2dict, ignore_index=True)
df = df.loc[:, columns]
df['Desc'] = df['Desc'].map(desc_format)
df['Name'] = df['Name'].map(lambda item: item.rstrip(' API'))
df.to_csv('./api.csv')
