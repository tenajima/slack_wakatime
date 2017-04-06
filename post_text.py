import slackweb
import basicAPIKey
from config import config

def make_text(data):
    string = config['name'] + "の過去7日間の総コーディング時間は"
    string += data['data']['human_readable_total'] + 'で,内訳は,'
    languages = data['data']['languages']
    for i in range(len(languages)):
        string += str(languages[i]['name']) + "を" + str(languages[i]['percent']) + "%"
        if i != len(languages) - 1:
            string += ","
    string += "書きました."
    return string


def post_text():
    slack = slackweb.Slack(url = config['slack_url'])
    data = basicAPIKey.languages_request()
    text = make_text(data)
    print(text)
    slack.notify(text = text)

if __name__ == '__main__':
    post_text()
