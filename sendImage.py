from heyoo import WhatsApp

def send(fileName, txt, mobile):
    # print(mobile)
    messenger = WhatsApp(token='EAAFaFIJHIucBOwjSccj3rEgLzDs7cGv2B6A7XaSIblpGK8NGsv9BG2fJATTpaROv5S3CJCL9RFvZASxu6k8gOZCZAl4mUCfEAEkLk536a0goBs34BObDVFZB6vIQAC2x1C8sIUJqBXJN2m1ZCs9nWHMqB4GRJFb47OQH6jDNs35dUw7S8fXebP1VlaiALZAr8AGJ5z3Auw4z7I7XssCO4r',  phone_number_id='256226997571281');
    media_id = messenger.upload_media(media=f"./data/{fileName}",)["id"]
    for i in mobile:
        messenger.send_image(image=media_id, recipient_id=i, link=False, caption=txt)
    # 