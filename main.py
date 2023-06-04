from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import t_catalog_catalog
from sqlalchemy.sql.expression import func
import re
import os
import urllib.request
from io import BytesIO
import requests

_TOKEN = os.environ['TOKEN']
_CHATID = os.environ['CHATID']

def formatin_date():
    # Создание подключения к базе данных SQLite
    engine = create_engine('sqlite:///data.sqlite')

    # Создание сессии для работы с базой данных
    Session = sessionmaker(bind=engine)
    session = Session()

    # Получение пользователя по идентификатору
    query = session.query(t_catalog_catalog).order_by(func.random()).first()

    article = {
        "AUTHOR": query[0],
        'TITLE': query[2],
        'DATE': query[3],
        'TECHNIQUE': query[4],
        'LOCATION': query[5],
        'URL': query[6]
    }
    return article


def get_image(link):
    q = re.sub('html','art',link,1)
    q2 = re.sub('html','jpg',q,1)
    print(q2)
    urllib.request.urlretrieve(q2, "image.jpg")


def send_image(image_caption):
    url = f"https://api.telegram.org/bot{_TOKEN}/sendPhoto";
    files = {'photo': open('./image.jpg', 'rb')}
    data = {'chat_id' :_CHATID,"caption":image_caption}
    r= requests.post(url, files=files, data=data)
    print(r.status_code, r.reason, r.content)


if __name__ == "__main__":
    try:
        data = formatin_date()
        image_caption = f"{data['AUTHOR']}\n{data['TITLE']}\n{data['DATE']}\n{data['TECHNIQUE']}\n{data['LOCATION']}"
        get_image(data['URL'])
        print(image_caption)
        print(send_image(image_caption))
    except Exception as e:
        print("The error is: ",e)


   