import argparse
import validators
import yaml
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from bs4 import Comment

parser = argparse.ArgumentParser(description='The Achilles HTML Vulnerability Analyzer V 1.0')

parser.add_argument('-v', '--version', action = 'version', version='%(prog)s 1.0')
parser.add_argument('url', type=str, help="The URL of the HTML to analyze")
parser.add_argument('--config', help="Path to configuration file")
parser.add_argument('-o', '--output', help="Path to the output file for the report")

args=parser.parse_args()
config = {'forms':True, 'comments':True, 'password_inputs': True}
if(args.config):
    print('Using config file: '+args.config)
    config_file = open(args.config, 'r')
    config_from_file = yaml.load(config_file)
    if(config_from_file):
        config=config_from_file
        config = {**config, **config_from_file}
report=''
url = args.url

if(validators.url(url)):
    results = requests.get(url).text
    parsed_results = BeautifulSoup(results, 'html.parser')
    forms = (parsed_results.find_all('form'))
    comments = parsed_results.find_all(string=lambda text:isinstance(text,Comment))
    password_inputs =   parsed_results.find_all('input', {'name' : 'password'})
    if(config['forms']):
        for form in forms:
            if ((form.get('action').find('https')<0) and (urlparse(url).scheme != 'https')):
                form_is_secure = False
                report+='Form Issue: Insecure ' + form.get('action')+ ' found in document \n\n'
    if(config['comments']):
        for comment in comments:
            if(comment.find('key: ')>-1):
                report+='Comment Issue: Key is found in the HTML comments, please remove\n\n'
    if(config['password_inputs']):
        for password_input in password_inputs:
            if(password_input.get('type') != 'password'):
                report += 'Input Issue: Plain text password input found, please change to password type \n'
else:
    print('Please input a valid URL. Please include the scheme of the URL')

if(report == ''):
    report+='HTML Document is secure'
else:
    header='Vulnerabilities found:\n'+'==============================\n\n'

    report=header+report


if(args.output):
    file=open(args.output, 'w')
    file.write(report)
    file.close
    print("File saved Successfully")
