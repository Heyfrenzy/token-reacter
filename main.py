from base64 import b64encode
from threading import Thread
import tls_client, json, os, ctypes, time

os.system("cls" if os.name == "nt" else "clear")

__useragent__ = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"  #requests.get('https://discord-user-api.cf/api/v1/properties/web').json()['chrome_user_agent']
build_number = 165486  #int(requests.get('https://discord-user-api.cf/api/v1/properties/web').json()['client_build_number'])
cv = "108.0.0.0"
__properties__ = b64encode(
  json.dumps(
    {
      "os": "Windows",
      "browser": "Chrome",
      "device": "PC",
      "system_locale": "en-GB",
      "browser_user_agent": __useragent__,
      "browser_version": cv,
      "os_version": "10",
      "referrer": "https://discord.com/channels/@me",
      "referring_domain": "discord.com",
      "referrer_current": "",
      "referring_domain_current": "",
      "release_channel": "stable",
      "client_build_number": build_number,
      "client_event_source": None
    },
    separators=(',', ':')).encode()).decode()


def get_headers(token, channel):
  headers = {
    "Authorization": token,
    "Origin": "https://discord.com",
    "Accept": "*/*",
    "X-Discord-Locale": "en-GB",
    "X-Super-Properties": __properties__,
    "User-Agent": __useragent__,
    "Referer": f"https://discord.com/channels/{channel}",
    "X-Debug-Options": "bugReporterEnabled",
    "Content-Type": "application/json"
  }
  return headers

reacted = 0 
def title():
    ctypes.windll.kernel32.SetConsoleTitleW("[Exploit Reactor] | Reacted: %s" % (reacted))

def add_reaction(tk, channel, message, emoji, emoji_name):
    global reacted
    headers = get_headers(tk, channel)
    # headers={'Authorization': tk,'accept': '*/*','accept-language': 'en-US','connection': 'keep-alive','cookie': f'__cfduid = {rc(43)}; __dcfduid={rc(32)}; __sdcfduid={rc(96)}; locale=en-US','DNT': '1','origin': 'https://discord.com','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','referer': 'https://discord.com/channels/@me','TE': 'Trailers','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36','X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTYuMC40NjY0LjQ1Iiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vZGlzY29yZC5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiZGlzY29yZC5jb20iLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMDg5MjQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',}

    # r = requests.patch('https://discord.com/api/v9/users/@me', headers=headers, json={"avatar":f'data:image/png;base64,{b64encode(img).decode("ascii")}'})
    client = tls_client.Session(client_identifier="firefox_102")
    client.headers.update(headers)
    r = client.get("https://discord.com/api/v9/users/@me")
    if r.status_code in (200, 201, 204):
        # r2 = client.put(f"https://discord.com/api/v10/channels/{channel}/messages/{message}/reactions/{emoji}/@me")
        r2 = client.put(f"https://discord.com/api/v9/channels/{channel}/messages/{message}/reactions/{emoji}/%40me?location=Message&burst=false")
        # print(r2.status_code)
        if r2.status_code in (200, 201, 204):
            reacted += 1
            title()
            print(f"[+] Successfully reacted to message {message} in channel {channel} with emoji {emoji_name} with token {tk[:30]}")
        else:
            print(f"[-] Failed to react ", r2.text)
        # print(r2.text)




def url_encode(string1):
    return string1.replace(":", "%3A").replace("/", "%2F").replace("<", "").replace(">", "")
print("Hey! Any Questions or Issues? Contact me on Discord! .gg/michitools")
emoji1 = input("[!] Emoji: ")
emoji = url_encode(emoji1)
try:
  emoji_name = emoji1.split(":")[0]
except:
  emoji_name = emoji1
# emoji = "%F0%9F%8E%89"
# emoji = "%E2%9C%85"
# emoji_name = "check"
channel = input("[!] Channel id : ")
message = input("[!] message id : ")
amount = int(input("[!] amount : "))
amount = amount + 1
f = open("tokens.txt", "r").readlines()

print("[!] Starting....")
time.sleep(3)
os.system("cls" if os.name == "nt" else "clear")
count = 0 
for token in f:
    token = token.strip()
    # token = token.split(":")[2]
    count += 1
    if count > amount:
        break
    time.sleep(0.02)
    Thread(target=add_reaction, args=(token, channel, message, emoji,emoji_name,)).start()
from base64 import b64encode
from threading import Thread
import tls_client, json, os, ctypes, time

os.system("cls" if os.name == "nt" else "clear")

__useragent__ = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"  #requests.get('https://discord-user-api.cf/api/v1/properties/web').json()['chrome_user_agent']
build_number = 165486  #int(requests.get('https://discord-user-api.cf/api/v1/properties/web').json()['client_build_number'])
cv = "108.0.0.0"
__properties__ = b64encode(
  json.dumps(
    {
      "os": "Windows",
      "browser": "Chrome",
      "device": "PC",
      "system_locale": "en-GB",
      "browser_user_agent": __useragent__,
      "browser_version": cv,
      "os_version": "10",
      "referrer": "https://discord.com/channels/@me",
      "referring_domain": "discord.com",
      "referrer_current": "",
      "referring_domain_current": "",
      "release_channel": "stable",
      "client_build_number": build_number,
      "client_event_source": None
    },
    separators=(',', ':')).encode()).decode()


def get_headers(token, channel):
  headers = {
    "Authorization": token,
    "Origin": "https://discord.com",
    "Accept": "*/*",
    "X-Discord-Locale": "en-GB",
    "X-Super-Properties": __properties__,
    "User-Agent": __useragent__,
    "Referer": f"https://discord.com/channels/{channel}",
    "X-Debug-Options": "bugReporterEnabled",
    "Content-Type": "application/json"
  }
  return headers

reacted = 0 
def title():
    ctypes.windll.kernel32.SetConsoleTitleW("[Exploit Reactor] | Reacted: %s" % (reacted))

def add_reaction(tk, channel, message, emoji, emoji_name):
    global reacted
    headers = get_headers(tk, channel)
    # headers={'Authorization': tk,'accept': '*/*','accept-language': 'en-US','connection': 'keep-alive','cookie': f'__cfduid = {rc(43)}; __dcfduid={rc(32)}; __sdcfduid={rc(96)}; locale=en-US','DNT': '1','origin': 'https://discord.com','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','referer': 'https://discord.com/channels/@me','TE': 'Trailers','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36','X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTYuMC40NjY0LjQ1Iiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vZGlzY29yZC5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiZGlzY29yZC5jb20iLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMDg5MjQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',}

    # r = requests.patch('https://discord.com/api/v9/users/@me', headers=headers, json={"avatar":f'data:image/png;base64,{b64encode(img).decode("ascii")}'})
    client = tls_client.Session(client_identifier="firefox_102")
    client.headers.update(headers)
    r = client.get("https://discord.com/api/v9/users/@me")
    if r.status_code in (200, 201, 204):
        # r2 = client.put(f"https://discord.com/api/v10/channels/{channel}/messages/{message}/reactions/{emoji}/@me")
        r2 = client.put(f"https://discord.com/api/v9/channels/{channel}/messages/{message}/reactions/{emoji}/%40me?location=Message&burst=false")
        # print(r2.status_code)
        if r2.status_code in (200, 201, 204):
            reacted += 1
            title()
            print(f"[+] Successfully reacted to message {message} in channel {channel} with emoji {emoji_name} with token {tk[:30]}")
        else:
            print(f"[-] Failed to react ", r2.text)
        # print(r2.text)




def url_encode(string1):
    return string1.replace(":", "%3A").replace("/", "%2F").replace("<", "").replace(">", "")

emoji1 = input("[!] Emoji: ")
emoji = url_encode(emoji1)
try:
  emoji_name = emoji1.split(":")[0]
except:
  emoji_name = emoji1
# emoji = "%F0%9F%8E%89"
# emoji = "%E2%9C%85"
# emoji_name = "check"
channel = input("[!] Channel: ")
message = input("[!] Message: ")
amount = int(input("[!] Amount: "))
amount = amount + 1
f = open("tokens.txt", "r").readlines()

print("[!] Starting....")
time.sleep(3)
os.system("cls" if os.name == "nt" else "clear")
count = 0 
for token in f:
    token = token.strip()
    # token = token.split(":")[2]
    count += 1
    if count > amount:
        break
    time.sleep(0.02)
    Thread(target=add_reaction, args=(token, channel, message, emoji,emoji_name,)).start()
