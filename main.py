import requests

#Данная программа выдает словарь с распределением возрастов у друзей в вк.

def right_year_birth(str):
    a = str.split('.')
    if len(a) == 3:
        return int(a[2])
    else:
        return None


def calc_age(uid):

    vk_params_user = {'v': '5.71','access_token': '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711',  'user_ids' : uid}
    r = requests.get('https://api.vk.com/method/users.get', params=vk_params_user)

    user_id = r.json()['response'][0]['id']



    vk_params_friends = {'v': '5.71','access_token': '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711',  'user_id' : user_id,
                         'fields' : ['bdate']}

    r = requests.get('https://api.vk.com/method/friends.get', params=vk_params_friends)

    friends_list = r.json()['response']['items']
    friends_dict = dict()
    for fr in friends_list:

        if 'bdate' in fr.keys() and right_year_birth(fr['bdate']) is not None:
            age = 2020 - int(right_year_birth(fr['bdate']))
            friends_dict[2020 - age] = friends_dict.get(2020 - age, 0) + 1

    print(friends_dict)






if __name__ == '__main__':
    res = calc_age('maratkhasanov86')
    print(res)
