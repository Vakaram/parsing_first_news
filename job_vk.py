import requests
token = "Ваш токен" # str ваш токен #разрешить работу с группой и смс для токена
owner_id_group = 7777777  #itn-число знак минус для id группы itn-число
foo = 'Пишем текст' #переменная текст
response = requests.post('https://api.vk.com/method/wall.post', params={'access_token': token,
                                                                    'owner_id': owner_id_group,
                                                                    'from_group': 1,
                                                                    'message': foo,
                                                                    'signed': 0,
                                                                    'v':"5.131"}).json()
print(response)




