import json 
import os 

path = "./../test2017"
dir_list = os.listdir(path)
for i in range(len(dir_list)):
    dir_list[i] = int(dir_list[i].replace('.jpg', '').lstrip('0'))

# print(dir_list)

with open('instances_train2017.json') as f: 
    data = json.load(f) 
    # for title in data.keys():
    #     print(title)
    new_annot = data
    new_image = [] 

    for d in data['images']:
        # print(d['id'])

        if d['id'] in dir_list: 
            print('found', d['id'])
            new_image.append(d)

new_annot['images'] = new_image
new_json = json.dumps(new_annot)
with open('custom_train2017.json', 'w') as wf: 
    wf.write(new_json)

