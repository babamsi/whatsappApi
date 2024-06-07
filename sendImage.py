from heyoo import WhatsApp

def send(fileName, txt, mobile):
    # print(mobile)
    messenger = WhatsApp(token='EAAFaFIJHIucBO5CMGJJJiiy8aiWxvpYJKjmn680AS4SNWf73YsUjOD6t26Tdg4GjCbE9h7E3jv2vWTSSVowdoPrhaG1mdl5hQcIbXDTDZBarevQSRYakN4ZCnyJRisQfVpNdytAZBrzg0mEBYdhaElySf51lHARiz1fAE0PcCyOytiOVsQNOgllhjOYjdo6dLTyTAuT2e7JZCkvodRIIuf4ZCCKrfGHbug3akNxAZD',  phone_number_id='256226997571281');
    media_id = messenger.upload_media(media=f"./data/{fileName}",)["id"]
    for i in mobile:
        messenger.send_image(image=media_id, recipient_id=i, link=False, caption=txt)
    # 