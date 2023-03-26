import requests
import time
import bs4

def send_message(message):
    data = {
        'embeds': [{
            'description': message,
            'color': 0x993399
        }]
    }
    response = requests.post(webhook_url, json=data)

webhook_url = 'https://discord.com/api/webhooks/1089602522110513243/CadQy8EIp51pqqDIWxljbub7J6VGczLNDn5WBTk2TCrESvqybtVK4QtO_A596sRH_DJk'

latest_ban = ""

if __name__ == '__main__':
    while True:
        url = "https://pika-network.net/bans/"
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        bans = soup.find_all('div', class_="row")
        for ban in bans:
            #only get the first 5 bans
            if bans.index(ban) < 1:
                info = ban.text
                username = info.split(' ')[0]
                reason = info.split(' ')[1]
                clean_reason = reason.replace('Reason:', '')
                clean_username = username.replace('Username:', '')
                clean_reason = clean_reason.replace('\n', '')
                clean_username = clean_username.replace('\n', '')
                print(f"{clean_username} {clean_reason}")
                if clean_username != latest_ban:
                    send_message(f"{clean_username} {clean_reason}")
                    latest_ban = clean_username

        time.sleep(10)
