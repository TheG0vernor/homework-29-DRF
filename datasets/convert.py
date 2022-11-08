import csv
import json


def convert_ads_to_json(csv_file, json_file, model):
    result = []
    with open(csv_file, encoding='utf-8') as file_csv:
        for i in csv.DictReader(file_csv):
            dict_ = {'model': model, 'pk': int(i['Id'] or i['id'])}
            if 'id' in i:
                del i['id']
            elif 'Id' in i:
                del i["Id"]
            if i['is_published'] == 'TRUE':
                i['is_published'] = True
            elif i['is_published'] == 'FALSE':
                i['is_published'] = False
            if 'price' in i:
                i['price'] = int(i['price'])
            dict_['fields'] = i
            result.append(dict_)
    with open(json_file, 'w', encoding='utf-8') as file_json:
        file_json.write(json.dumps(result, ensure_ascii=False))


def convert_other_to_json(csv_file, json_file, model):
    result = []
    with open(csv_file, encoding='utf-8') as file_csv:
        for i in csv.DictReader(file_csv):
            dict_ = {'model': model, 'pk': int(i['id'])}
            if 'id' in i:
                del i['id']

            if 'location_id' in i:
                i['locations'] = [int(i['location_id'])]
                del i['location_id']

            dict_['fields'] = i
            result.append(dict_)
    with open(json_file, 'w', encoding='utf-8') as file_json:
        file_json.write(json.dumps(result, ensure_ascii=False))


# convert_ads_and_user_to_json('ad.csv', 'ad.json', 'ads.ad')
# convert_other_to_json('category.csv', 'category.json', 'ads.category')
# convert_other_to_json('location.csv', 'location.json', 'user.location')
# convert_other_to_json('user.csv', 'user.json', 'user.user')
