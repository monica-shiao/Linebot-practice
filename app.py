from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('gGzD5hmcpQTuBCn0vfLLppBHoXjCS9GLEU45CPx1cwa7pjeYUpUOjqYeA4IKNMR3LSt3diQgiJsuog6IJqzn8/6R1L+3TsK14rz1eXrWRp3kyxKSoW1TS4YAV38Ep0SAJ0oJc8DrtSODdVrldi9ZvgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('122d22d024f2cacd2e784d921bd247f2')

# 監聽所有來自 /callback 的 Post Request
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

    if event.message.text == "來張正妹照":
        message = ImageSendMessage(
            original_content_url='https://s9.rr.itc.cn/r/wapChange/20167_31_16/a6476f4427998223628.JPEG',
            preview_image_url='https://s9.rr.itc.cn/r/wapChange/20167_31_16/a6476f4427998223628.JPEG'
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0;
    
    elif event.message.text == "聊天吧":
        message = TextSendMessage(text="Hello~ 你好嗎？")
        line_bot_api.reply_message(event.reply_token, message)
        return 0;
    
    elif event.message.text == "出遊Go":
        message = LocationSendMessage(
            title='輔仁大學',
            address='242台灣新北市新莊區中正路510號',
            latitude=25.035430,
            longitude=121.432464
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0;
    
    elif event.message.text == "我的最愛":
        message = TextSendMessage(text="目前還沒有東西喔！")
        line_bot_api.reply_message(event.reply_token, message)
        return 0;
    
    elif event.message.text == "Shopping Time":
        #buttonTemplate
        buttons_template = TemplateSendMessage(
            alt_text="開始玩 template",
            template=ButtonsTemplate(
                title="想買什麼呢？",
                text="請選擇",
                thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxS0qyJldUrPDsnpJajgLuDzou6A6Uvl6pWsA7LBaY7t-Rcw-x',
                actions=[
                    MessageTemplateAction(
                        label="衣服",
                        text="衣服"
                    ),
                    MessageTemplateAction(
                        label="鞋子",
                        text="鞋子"
                    ),
                    URITemplateAction(
                        label='化妝品',
                        uri='https://shopee.tw/%E7%BE%8E%E5%A6%9D%E4%BF%9D%E5%81%A5-cat.67'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0;
        
    elif event.message.text == "是不是該念書了":
        #貼圖
        message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0;
    
    elif event.message.text == "衣服":
        carousel_template_message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://static.juksy.com/files/articles/49993/567a890fd11d4.jpg?m=widen&i=600&q=75',
                        title='男士專區',
                        text='男士專區',
                        actions=[
                            URITemplateAction(
                                label='襯衫',
                                uri='https://shopee.tw/%E8%A5%AF%E8%A1%AB-cat.63.1521'
                            ),
                            URITemplateAction(
                                label='外套',
                                uri='https://shopee.tw/%E5%A4%96%E5%A5%97-cat.63.1533'
                            ),
                            URITemplateAction(
                                label='運動服飾',
                                uri='https://shopee.tw/%E9%81%8B%E5%8B%95%E6%9C%8D%E9%A3%BE-cat.63.2171'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://previews.123rf.com/images/nataliashein/nataliashein1112/nataliashein111200004/11548737-women-shopping-Stock-Photo.jpg',
                        title='女人專區',
                        text='女人專區',
                        actions=[
                            URITemplateAction(
                                label='洋裝',
                                uri='https://shopee.tw/%E6%B4%8B%E8%A3%9D-cat.62.1485'
                            ),
                            URITemplateAction(
                                label='裙子',
                                uri='https://shopee.tw/%E8%A3%99%E5%AD%90-cat.62.1483'
                            ),
                            URITemplateAction(
                                label='套裝',
                                uri='https://shopee.tw/%E5%A5%97%E8%A3%9D-cat.62.1477'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTaYckGVjbI0XzgmqfEaSGx33-pYsrGrST2uC8QCpa-7HIjwyv-',
                        title='北鼻天地',
                        text='北鼻天地',
                        actions=[
                            URITemplateAction(
                                label='男童童裝',
                                uri='https://shopee.tw/search/?facet=%257B%2522100%2522%253A%255B12%252C2661%255D%257D&keyword=%E5%B0%8F%E5%AD%A9%E8%A1%A3%E6%9C%8D&page=0&pageType=2'
                            ),
                            URITemplateAction(
                                label='女童童裝',
                                uri='https://shopee.tw/search/?facet=%257B%2522100%2522%253A%255B12%252C2663%255D%257D&keyword=%E5%B0%8F%E5%AD%A9%E8%A1%A3%E6%9C%8D&page=0&pageType=2'
                            ),
                            URITemplateAction(
                                label='嬰兒周邊',
                                uri='https://shopee.tw/search/?facet=%257B%2522100%2522%253A%255B12%252C2196%255D%257D&keyword=%E5%B0%8F%E5%AD%A9%E8%A1%A3%E6%9C%8D&page=0&pageType=2'
                            )
                        ]
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, carousel_template_message)
        return 0;
        
    elif event.message.text == "鞋子":
        # ImageCarouselTemplate
        image_carousel_template_message = TemplateSendMessage(
            alt_text='ImageCarousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://img.yzcdn.cn/upload_files/2016/11/26/14801636167912092.jpg',
                        action=PostbackTemplateAction(
                            label='女鞋',
                            text='girlShose',
                            data='girlShose'      #data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://cdn.qdm.com.tw/q591edb4be0bd8/image/cache/data/2017/09/19/19a8743874f96d47ff1d4b64f01a5336-max-w-1024.jpg',
                        action=PostbackTemplateAction(
                            label='男鞋',
                            text='manShose',
                            data='manShose'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, image_carousel_template_message)
        return 0;
    
    
    else:
        message = TextSendMessage(text="Hello world!")
        line_bot_api.reply_message(event.reply_token, message)
        return 0;
    
@handler.add(PostbackEvent)
def handle_postback(event):
    if event.postback.data == 'girlShose':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='successful~~~~'))
     


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
