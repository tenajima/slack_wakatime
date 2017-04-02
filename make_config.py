def make_config_file():
    f = open('config.py','w')
    f.write('config = {\'slack_url\': \'XXXX\', \'api_key\': \'XXXX\'}')
    f.close()
    print('prease enter slack_url from webhook and api key from wakatime in config file')
