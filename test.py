import json
with open('mail_list.json', 'r') as file:
    data = json.load(file)
    print('Raw data', data)
    recievers_list = data['reciever']
    print('Parse 1', recievers_list)
    name1 = recievers_list
    print('Parse 2', recievers_list)
    name2 = name1[0]
    print('Parse 3', name2)
    name3 = name2['email']
    print('Parse 4', name3)