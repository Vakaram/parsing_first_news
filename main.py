import requests
from bs4 import BeautifulSoup
import vk_authorization
import time
from datetime import datetime
from random import randint

def take_information():
    HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }
    #обратились к серву вернул 200!
    r = requests.get('https://alshei.bashkortostan.ru/presscenter/news/', headers=HEADERS)
    #создали объект соупа
    soup = BeautifulSoup(r.text, 'lxml')
    #обратились по классу, взяли второй элемент в списке т.к. первый закреплён постоянно он мне не нужен он не обновляется
    firs_news_url = soup.find_all(class_="list__title")[1] #получаем из списка нужный элемент
    link_first_url = firs_news_url.find('a').get('href') #собираем href у первой новости чтобы попасть во внутр страницы
    # print(link_first_url)
    #Теперь получим ссылку, текст, фото, заголовок в 3 переменные ) и потом отправим в группу вк
    r_second = requests.get('https://alshei.bashkortostan.ru'+ link_first_url, headers=HEADERS) #отправляемся по ссылке во внутр новости
    soup_second = BeautifulSoup(r_second.text, 'lxml')
    zagolovok = soup_second.find_all(class_="detail__title")[0].text.strip() #получил заголовок
    # print(zagolovok)
    text = soup_second.find_all(class_="detail__text")[0].text.strip() #получил текст
    # print(text)
    url_in_news  = 'https://alshei.bashkortostan.ru'+link_first_url
    # print(url_in_news)
    photo = soup_second.find_all(class_ ='detail__main-photo')[0].get('srcset') #получаем из списка нужный элемент
    photo_search = 'https://alshei.bashkortostan.ru' + photo[:-3]
    # print(photo_search)
    super_text = '💥 ' + zagolovok + '.' + ' 💥' + '\n' + text + '\n' + ' Источник: ' + url_in_news  #формирую единный текст

    return super_text , photo_search, zagolovok

zagolovok_na_sravnenie  = 'Заглушка заголовка'
while True:
    print(f'Заголовок старый {zagolovok_na_sravnenie}')
    try:
        token = vk_authorization.token # str ваш токен #разрешить работу с группой и смс для токена
        owner_id_group = vk_authorization.owner_id_group  #itn-число знак минус для id группы itn-число
        text_vk, photo_url, zagolovok_iz_def = take_information() #берём данные из функции #по счёт 1.2.3
        if zagolovok_na_sravnenie != zagolovok_iz_def:
            zagolovok_na_sravnenie = zagolovok_iz_def #перепишем переменную которая выше
            print(f'Заголовок переписали на  {zagolovok_iz_def}')
            response = requests.post('https://api.vk.com/method/wall.post', params={'access_token': token,
                                                                                'owner_id': owner_id_group, #передаём параметры  типо смс, фото url и т.д.
                                                                                'from_group': 1,
                                                                                'message': text_vk,
                                                                                'attachments': photo_url,
                                                                                'signed': 0,
                                                                                'v':"5.131"})
        #     time_now = datetime.now()
        #     logi_in = str(time_now) + ' | ' + str(response.text) + ' | ' + ' OK' + '\n'
            print(response.text)
        #     with open('loger.txt', 'a') as f:
        #         f.write(logi_in) #всё что выше остаётся в цикле, и если ок то он пишет в логи но каждый час мы всё рановно будем делать действие ниже, будем записывать что новость не менялась и зачем её вообще ещё раз постить, отдыхаем час.
        # else:
        #     time_now = datetime.now()
        #     text_otdixaem = str(time_now) + ' | ' + ' Мы проверили новость она не обновилась, просто спим 60 минут '  + ' | ' + ' OK' + '\n'
        #     with open('loger.txt', 'a') as f:
        #         f.write(text_otdixaem)
    except Exception as e: #ловим любую ошибку дописываем её в файл нот ок
        pass
    time.sleep(randint(1900,3500)) # поменяй на каждые 20-30 минут видать часто новости прилетают


