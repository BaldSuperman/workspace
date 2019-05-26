import urllib.request
import gevent
from gevent import monkey
import random
monkey.patch_all()
def downloader(img_name, imag_url):
    req = urllib.request.urlopen(imag_url)
    img_content = req.read()
    with open("D:/"+ img_name, "wb") as f:
        f.write(img_content)

def main():
    gevent.joinall([
        gevent.spawn(downloader, '1.jpg', 'https://rpic.douyucdn.cn/live-cover/appCovers/2019/05/15/1853869_20190515000244_small.jpg'),  # spawn(函数名，参数)
        gevent.spawn(downloader, '2.jpg', 'https://rpic.douyucdn.cn/live-cover/appCovers/2019/05/04/6893293_20190504200419_small.jpg'),

    ])
if __name__ == '__main__':
    main()
