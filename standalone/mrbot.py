import requests
import json

token="1791911591:AAGJMfo7jnrr7Jtl1Xg8sYjMRKEQhkbqA3E"
base="https://api.telegram.org/bot{}/".format(token)



def get_updates(offset):
        url=base + "/getUpdates?timeout=100"
        if offset:
            url=url+"&offset={}".format(offset + 1) #increment offset plus one every time and update is sent to get the final message
            r=requests.get(url)
            return json.loads(r.content)
        
def send_message(msg,chat_id):
            url= base + "sendMessage?chat_id={}&text={}".format(chat_id,msg)
            if msg is not None:
                requests.get(url)
                
def make_reply(msg,name):
    #if msg is not None:
    reply="Hi"+name+",Please Cheslie will get to you soon"
    return reply

update_id =int('289438578')
while True:
    print (base)
    updates = get_updates(offset=update_id)
    print(updates)
    updates =updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message =item["message"]["text"]
            except:
                message =None

            from_= item["message"]["from"]["id"]
            name=item["message"]["from"]["last_name"]
            reply=make_reply(message,name)
            send_message(reply,from_)
