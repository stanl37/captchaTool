import json
import datetime
import time

def log():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S.%f')[:-3]
    stformatted = "[" + st + "] "
    return(stformatted)

def fileLen(fname):
    i = 0
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def loadConfig(configname):
    with open(configname) as jsondata:
        config = json.load(jsondata)
        return config

def formatEmail(configEmail):
    if "@gmail.com" in configEmail:
        email = configEmail[:-10]
        return email
    elif "@gmail.com" not in configEmail:
        email = configEmail
        return email
    else:
        if verboseStatus == True: print(tools.log() + "Email was wrong, you can enter it with or without the gmail.")
        if verboseStatus == True: print(tools.log() + "VALID EXAMPLE: stanley123@gmail.com")
        if verboseStatus == True: print(tools.log() + "VALID EXAMPLE: stanley123")
    if verboseStatus == True: print(tools.log() + "Using email: " + email)

#2captcha system
"""
token = 'RESPONSE_TOKEN_HERE'
key = config["twocapKey"]

params = {
    'key':key,
    'method':'userrecaptcha',
    'googlekey':'6LdhYxYUAAAAAAcorjMQeKmZb6W48bqb0ZEDRPCl',
    'pageurl':'https://app.viralsweep.com/vrlswp/widget/897b48-45762?framed=1',
    'json':1
}

r = requests.post('http://2captcha.com/in.php', params=params)
jsonA = json.loads(r.text)
id = jsonA['request']
print(Fore.RED + log() + "2CAP Solve ID: " + id)

getParams = {
    'key':key,
    'action':'get',
    'id':id,
    'json':1
}

status = 0
while status == 0:
    time.sleep(5)
    r = requests.get('http://2captcha.com/res.php', params=getParams)
    jsonB = json.loads(r.text)
    status = jsonB['status']
    token = jsonB['request']
    if "ERROR" in token:
        print(Fore.RED + log() + "Captcha unsolvable. This entry will fail.")
        break
    if "ERROR" not in token:
        print(Fore.RED + log() + token)

print(Fore.CYAN + log() + "Captcha found from 2CAP.")
"""

#2cap failsafe system
"""
failParams = {
    'key':key,
    'action':'reportbad',
    'id':id
}

if token.lower() != success:
    r = requests.get('http://2captcha.com/res.php', params=failParams)
    print(r.text)
"""
