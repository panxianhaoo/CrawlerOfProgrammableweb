import json
import pandas as pd


def desc_format(s):
    if s is None:
        return ''
    s = s.replace('\n', ' ')
    return s.strip()


f = open('mashup_data.json', 'r')
items = f.readlines()
columns = ['Name', 'Related APIs', 'Categories', 'Desc', 'URL', 'Company', 'Mashup/App Type']
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
df['Desc'] = df['Desc'].map(desc_format)
df.to_csv('./mashup.csv', encoding='UTF-8')
