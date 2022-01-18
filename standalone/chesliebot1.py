import requests
import json

get_update_method="https://api.telegram.org/bot1791911591:AAGJMfo7jnrr7Jtl1Xg8sYjMRKEQhkbqA3E/getUpdates"
pooling ="https://api.telegram.org/bot1791911591:AAGJMfo7jnrr7Jtl1Xg8sYjMRKEQhkbqA3E/getUpdates?offset=289438570&timeout=100"
send="https://api.telegram.org/bot1791911591:AAGJMfo7jnrr7Jtl1Xg8sYjMRKEQhkbqA3E/sendMessage?chat_id=-543210920&text='This is a text message'"

token="1791911591:AAGJMfo7jnrr7Jtl1Xg8sYjMRKEQhkbqA3E"
base="https://api.telegram.org/bot{}/".format(token)
class telegram_chatbot():
    def __init__()
        token="1791911591:AAGJMfo7jnrr7Jtl1Xg8sYjMRKEQhkbqA3E"
        base="https://api.telegram.org/bot{}/".format(self.token)

    def get_updates(offset=None):
        url=base + "/getUpdates?timeout=100"
        if offset:
            url=url+"&offset={}".format(offset + 1) #increment offset plus one every time and update is sent to get the final message
            r=requests.get(url)
            return json.loads(r.content)

        def send_message(msg,chat_id):
            url= base + "sendMessage?chat_id={}&text={}".format(chat_id,msg)
            if msg is not None:
                requests.get(url)

        
def get_updates(offset=None):
        url=base + "/getUpdates?timeout=100"
        if offset:
            url=url+"&offset={}".format(offset + 1) #increment offset plus one every time and update is sent to get the final message
            r=requests.get(url)
            return json.loads(r.content)
