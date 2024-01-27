import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está disponível para acesso')
else:
    print('O site pudim está disponível para acesso')
    print(site.read())