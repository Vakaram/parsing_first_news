import time

from bs4 import BeautifulSoup
import requests

import random
import re
import time
import requests
from bs4 import BeautifulSoup

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
    print(zagolovok)
    text = soup_second.find_all(class_="detail__text")[0].text.strip() #получил текст
    print(text)
    url_in_news  = 'https://alshei.bashkortostan.ru'+link_first_url
    print(url_in_news)
    photo = soup_second.find_all(class_ ='detail__main-photo')[0].get('srcset') #получаем из списка нужный элемент
    photo_search = 'https://alshei.bashkortostan.ru' + photo[:-3]
    print(photo_search)






# прога будет проверять каждый час новости
#середина сделана
#
# вк если есть новость она принимает ссылку, фото, текст заголовок




















# print(soup.title)
# page_h1 = soup.find('div')
# print(page_h1)
# page_all_h1 = soup.find_all('div')
# print(page_all_h1) #возвращает все найденные заголовки.
#попробуем перебрать по циклу
# for i in page_all_h1:
#     print(i.text)

#Получаем заголовок типо
# zagolovok_1 = soup.find_all("h3", class_="list__title")
# print(zagolovok_1)
# print('____________________________________________________________________________________')
# for i in zagolovok_1:
#     print(i.text.strip())
# firs_news = zagolovok_1[1].text.strip() #strip как сплит типо пробелы удаляет. text вертает текст
# print(firs_news)

#теперь я получаю ссылку на новость
# firs_news_url = soup.find_all("h3", class_="list__title")
# firs_news_url = firs_news_url[1].next_element.next_element
# print(firs_news_url)
# print(type(firs_news_url))
# for i in firs_news_url:
#     link = i.get('href')
#     print(link)










# print(soup)
# trabe_list = soup.find('div', {"class": "sc-cURfjK gZrOaw"})
# trabe_list = soup.find_all('article', {'class' : 'list__item'})

# print(trabe_list)





    #
    # for item in items:
    #     comps.append({
    #         'title': item.find('a',class_ = 'title-root-zZCwT' ).get_text(strip = True)
    #     })
    #
    # for comp in comps:
    #     print(comp['title'])











# url = 'https://youla.ru/raevskiy?q=диван'
#
# request = requests.get(url)
# print(request.status_code)
#
# bs = BeautifulSoup(request.text, 'html.parser')
# print(bs)
#
# all_links = bs.findAll('a',class_ = 'sc-cOxWqc')
# print(all_links)
# # for link in all_links:
# #     print(link)

#
# resp = requests.get("http://www.something.com")
#
# soup = BeautifulSoup(resp.text, 'lxml')
#
# print(soup.title)
# print(soup.title.text)
# print(soup.title.parent)
#
#





