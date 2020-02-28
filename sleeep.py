import time
import urllib.request
import urllib.error

def uptime_bot(url):
    while True:
        try:
            conn = urllib.request.urlopen(url)
        except urllib.error.HTTPError as e:
            print(f'HTTPError: {e.code} for {url}')
        except urllib.error.URLError as e:
            print(f'URLError: {e.code} for {url}')
        else:
            print(f'{url} is up')
        time.sleep(60)

if __name__ == '__main__':
    url = 'http://www.google.com/py'
    uptime_bot(url)

