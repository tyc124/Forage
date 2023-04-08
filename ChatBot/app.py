from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask()

#channel access token
line_bot_api = LineBotApi('oqSZujtvn6QbsOrP+V7a/lQrwgtBckYopZIhECmHyvNJxTcYRl3J9teGFB1iLDq6zbdhF17xI9ougthaU9Lj1wLfsmfedZmi4Cs9beFcDK4Pn+5+l9Ait8V6l0ITq8GFxToYYq6AsI1oTXj0QZNnbwdB04t89/1O/w1cDnyilFU=')
#channel secret
handler = WebhookHandler('fae3c19c8c89cc2b34312b5196cd28bf')

line_bot_api.push_message('U0b4f1c92f1e01d48d02ca4628c69e9e9', TextSendMessage(text='WeatherBot is now activated. Please enter the city to check the weather.'))

import weather

#take the response to handler
@app.route("/callback", methods=['POST']) 
def callback():     
    # get X-Line-Signature header value     
    signature = request.headers['X-Line-Signature']
    # get request body as text     
    body = request.get_data(as_text=True)     
    app.logger.info("Request body: " + body)      
    # handle webhook body     
    try:         
        handler.handle(body, signature)     
    except InvalidSignatureError:         
        abort(400)      
    return 'OK'

@handler.add(MessageEvent, message=TextMessage) 
def handle_message(event):     
    message = event.message.text
    reply = weather.main(f'{message}')
    line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))