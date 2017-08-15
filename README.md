# ReadTelegramText

Pyhton-script to read text from telegram app and to send reply with custom text.

### Changes before you run.
  "< TOKEN >" in url replace with the token you got from telegram.

### Functions:

  1. get_updates_json(request)
          Function to get all the received requests in past 24 hours.

  2. last_update(data)
          Returns the last/latest received data from past 24 hours.

  3. get_chat_id(update)
          Fetch out Chat Id from the message. We will need chat Id while reply.

  4. send_mess(chat, text)
          Function to send message.

  5. get_last_message(last_update)
          Fetch out just text from last latest received.

  6. main Function:
          Receives a text from user, displays it on console and sends a custom replay to the user.
          Will check every text, if text says "Stop", it will stop the script at that moment and will inform the user too with some custom text. 
