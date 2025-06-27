import requests, hashlib, os
from twilio.rest import Client

URL = 'https://www.mumresults.in/'

ACCOUNT_SID = os.getenv("TWILIO_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH")
FROM_WHATSAPP = 'whatsapp:+14155238886'
TO_WHATSAPP = os.getenv("TO_WHATSAPP")

HASH_FILE = 'hash.txt'

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def get_hash():
    res = requests.get(URL)
    return hashlib.md5(res.text.encode()).hexdigest()

def send_alert(msg):
    client.messages.create(
        body=msg,
        from_=FROM_WHATSAPP,
        to=TO_WHATSAPP
    )

try:
    with open(HASH_FILE) as f:
        old = f.read().strip()
except FileNotFoundError:
    old = ''

new = get_hash()

if new != old:
    send_alert("🆕 MumResults.in has been updated!")
    with open(HASH_FILE, 'w') as f:
        f.write(new)
