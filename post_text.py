import slackweb
import basicAPIKey
from config import config

def make_text(datas,my_name = '名無しさん'):
    string = "Yutoは"
    for i in range(len(datas)):
        string += str(datas[i]['name']) + "を" + str(datas[i]['percent']) + "%"
        if i != len(datas) - 1:
            string += ","
    string += "書きました."
    # print(string)
    return string


def post_text():
    slack = slackweb.Slack(url = config['slack_url'])
    data = basicAPIKey.languages_request()
    text = make_text(data, my_name ='Yuto')
    print(text)
    # slack.notify(text = text)

if __name__ == '__main__':
    post_text()
