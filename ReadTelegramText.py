import requests ##Requests allows you to send organic, grass-fed HTTP/1.1 requests, without the need for manual labor.
import time

url = "https://api.telegram.org/bot<TOKEN>/"

def get_updates_json(request):
    """
        Function to get all the received requests in past 24 hours.
    """
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()

def last_update(data):
    """
        Returns the last message or request.
    """
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    """
        Fetch out Chat Id from the message. We will need chat Id to reply our text.
    """
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    """
        Function to send message.
    """
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def get_last_message(last_update):
    """
        Fetch out last message received.
    """
    last_text = last_update['message']['text']
    return last_text

def main():
    chat_id = get_chat_id(last_update(get_updates_json(url)))
    update_id = last_update(get_updates_json(url))['update_id']

    while True:

        if update_id == last_update(get_updates_json(url))['update_id']:
            last_message = get_last_message(last_update(get_updates_json(url)))

            if last_message.lower() == "stop":
                print("Going to quit.")
                send_mess(chat_id, "Bye, I need to go.")
                break

            print("New Message Received: ", last_message)
            send_mess(chat_id, "Received your text.")
            update_id += 1

    time.sleep(1)

if __name__ == '__main__':
    main()
