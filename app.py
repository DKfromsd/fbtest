import os
import sys
import json

import credentials, requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must
    # return the 'hub.challenge' value in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            # os.environ.get("VERIFY_TOKEN", "default_verify_token")

            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200

@app.route('/', methods=['POST'])
def webhook():
    # endpoint for processing incoming messaging events
    data = request.get_json()
    log(data)  # you may not want to log every incoming message in production, but it's good for testing

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent us a message

                    sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                    recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                    message_text = messaging_event["message"]["text"]  # the message's text
                    # message_text = messaging_event["message"].get("text", "")
                    
                    # Test for Finance search result
					# https://finance.yahoo.com/quote/GLD?p=GLD&.tsrc=fin-srch-v1
                    yahoofinance="https://finance.yahoo.com/quote/"
                    inter3="?p="
                    inter4="&.tsrc=fin-srch-v1"
                    consult="https://www.stockconsultant.com/consultnow/basicplus.cgi?symbol="
                    seeking_alpha="https://seekingalpha.com/symbol/"
                    marketbeat="https://www.marketbeat.com/stocks/NYSE/"
                    inter2="?s="
                    space="\n\n"
                    quote_consult=consult+message_text                    
                    quote_sa=seeking_alpha+message_text+inter2+message_text
                    quote_yahoo=yahoofinance+message_text+inter3+message_text+inter4
                    quote_marketbeat=marketbeat+message_text
                    quote=quote_consult+space+quote_sa+space+quote_yahoo+space+quote_marketbeat+space
                    send_message(sender_id,quote)
                if messaging_event.get("delivery"):  # delivery confirmation
                    pass
                if messaging_event.get("optin"):  # optin confirmation
                    pass
                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                    pass
    return "ok", 200

def send_message(recipient_id, message_text):
    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))
    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
        # os.environ.get("PAGE_ACCESS_TOKEN", "default_page_access_token")

    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v12.0/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        #log(r.status_code)
        log(f"Error sending message: {r.status_code}")
        log(r.text)


def log(message):  # simple wrapper for logging to stdout on heroku
    print (str(message))
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)
