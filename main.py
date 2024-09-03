import sys, os
import requests

sys.dont_write_bytecode = True
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

from core import *
from core.zefoyomg.zefoy import zefoy
from core.plugins.log import *
from core.plugins.ui import *
from core.plugins.cmd import *
from core.plugins.cfg import *

# Replace this with your actual Discord webhook URL
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1280535287407050823/YdcJ0KjSc7YFRFMSUx_TjEQmshwiw19sJcMRpz58crEvwRjcb07-j0IS0xhOH6Fwm-tp'

def send_discord_message(content):
    """
    Sends a message to the specified Discord webhook URL.
    """
    data = {
        'content': content
    }
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=data)
        if response.status_code == 204:
            print('Message sent successfully to Discord.')
        else:
            print(f'Failed to send message to Discord. Status code: {response.status_code}, Response: {response.text}')
    except Exception as e:
        print(f'An error occurred while sending message to Discord: {e}')

def main():
    cmd.cls()
    UI.banner()
    print('\n')

    log.info('PROXY SCRAPER', 'Scraping proxies...')
    # Scrape proxies
    proxies = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&simplified=true').text
    with open('proxies.txt', 'w') as f:
        f.write(proxies.replace('\n', ''))
    log.info('PROXY SCRAPER', 'Scraping proxies completed.')

    while True:
        zef = zefoy(cfg().get())
        solve_success = False
        while not solve_success:
            zef.get_captcha()
            solve_success = zef.send_captcha()
        zef.parse_vid()
        zef.send_views()
        send_discord_message('**Sender 1000 views to m333lisa!**')
        send_discord_message('**--------------------------------------------**')

if __name__ == '__main__':
    main()
