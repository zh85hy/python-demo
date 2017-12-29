# coding: utf-8
import urllib3

download_url = 'https://www.python.org/ftp/python/3.6.4/python-3.6.4-macosx10.6.pkg'
download_file = 'python-3.6.4-macosx10.6.pkg'

if __name__ == '__main__':
    urllib3.disable_warnings()
    http_client = urllib3.PoolManager()
    response = http_client.request('GET', download_url)
    if response.status == 200:
        with open(download_file, 'wb') as f:
            f.write(response.data)
