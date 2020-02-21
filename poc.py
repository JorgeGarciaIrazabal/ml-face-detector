import urllib.request

print('Beginning file download with urllib2...')

if __name__ == '__main__':
    url = 'https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml'
    urllib.request.urlretrieve(url, 'haarcascade_eye.xml')