import requests
import hashlib

uuid = hashlib.md5(domain.encode('utf-8')).hexdigest()

domain = 'espn.com/nhl/statistics/player/_/stat/timeonice/league/east/qualified/false/position/forwards'

results = requests.get('http://' + domain)
ssl_results = requests.get('https://' + domain)

if ssl_results.status_code == 200:
    uses_ssl = True
else:
    uses_ssl=False

if(results.text.find('<link rel="stylesheet"')>-1):
    uses_css = True
else:
    uses_css=False

uses_js = (results.text.find('<script language ="JavaScript"')>-1)


profile = {'uuid':uuid, 'name': domain, 'uses_ssl': uses_ssl, 'uses_css': uses_css, 'uses_js': uses_js}

print(profile)
