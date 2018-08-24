import requests
import os
from hashlib import md5
from urllib.parse import urlencode
from multiprocessing.pool import Pool

headers = {
    'accept': 'application/json, text/javascript',
    'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'accept': 'application/json, text/javascript'
}


def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '美女',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)

    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

def get_url(json):
    if json.get('data'):
        for item in json.get('data'):
                title = item.get('title')
                images = item.get('image_list')
                if title is not None:
                    for image in images:
                        yield {
                            'image': 'http:' + image.get('url').replace('list', 'origin'),
                            'title': title
                        }


def save_image(item):
    if not os.path.exists(os.path.join("D:\jiepai", item.get('title'))):
        os.mkdir(os.path.join("D:\jiepai", item.get('title')))
    try:
        response = requests.get(item.get('image'),headers=headers)
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(os.path.join("D:\jiepai",file_path)):
                with open(os.path.join("D:\jiepai",file_path), 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


def main(offset):
    items = get_url(get_page(offset))
    for item in items:
        save_image(item)


if __name__ == '__main__':
    pool = Pool()#线程池
    groups = ([x * 20 for x in range(1, 21)])
    pool.map(main, groups)
    pool.close()
    pool.join()
    # for index in groups:
    #     main(index)