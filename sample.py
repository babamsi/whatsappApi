import requests
import json

from heyoo import WhatsApp
from dotenv import load_dotenv

import os

load_dotenv()
mytoken = os.getenv("TOKEN")
# numberId = os.getenv("PHONE_NUMBERID")
#system use token {	EAAFaFIJHIucBO5CMGJJJiiy8aiWxvpYJKjmn680AS4SNWf73YsUjOD6t26Tdg4GjCbE9h7E3jv2vWTSSVowdoPrhaG1mdl5hQcIbXDTDZBarevQSRYakN4ZCnyJRisQfVpNdytAZBrzg0mEBYdhaElySf51lHARiz1fAE0PcCyOytiOVsQNOgllhjOYjdo6dLTyTAuT2e7JZCkvodRIIuf4ZCCKrfGHbug3akNxAZD}


messanger = WhatsApp(token="EAAFaFIJHIucBO8lkTxgeVYZBCVk9ys2Dp9rxYQJjq9pNzmq3mPM7prXh1OKQEtNcB6k1CPr9rp3pua7YfZCKlqdlxhLIEUNNhaTxJi059QRZC8SG4EDwnZAGcBHFjychw0ZBMCqe9VVSCWAWELBZCEtt2TZAGFEHQ84ZBSgnGgKpFSdyNiZA9pz7lRSNnIEN8RtAhBEXFRTHsc71zhjKEVWnj", phone_number_id='256226997571281')

def createTemplate():
    url = 'https://graph.facebook.com/v18.0/256551524204351/message_templates'
    headers = {
        'Authorization': 'Bearer EAAFaFIJHIucBO8lkTxgeVYZBCVk9ys2Dp9rxYQJjq9pNzmq3mPM7prXh1OKQEtNcB6k1CPr9rp3pua7YfZCKlqdlxhLIEUNNhaTxJi059QRZC8SG4EDwnZAGcBHFjychw0ZBMCqe9VVSCWAWELBZCEtt2TZAGFEHQ84ZBSgnGgKpFSdyNiZA9pz7lRSNnIEN8RtAhBEXFRTHsc71zhjKEVWnj',
        'Content-Type': 'application/json'
    }
    payload = {
    "name": "bamci",
    "category": "MARKETING",
    "language": "en",
    "components": [{
        "type": "BODY",
        "text": "this is a simple template message that I have created from the backend without parameters",
        
    }]
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload)) #376685715237639 thats the ID of the template I created (bamsi)
    print(response.text)

def getTemplates():
    url = " https://graph.facebook.com/v19.0/256551524204351/message_templates"
    headers = {
        'Authorization': 'Bearer EAAFaFIJHIucBO8lkTxgeVYZBCVk9ys2Dp9rxYQJjq9pNzmq3mPM7prXh1OKQEtNcB6k1CPr9rp3pua7YfZCKlqdlxhLIEUNNhaTxJi059QRZC8SG4EDwnZAGcBHFjychw0ZBMCqe9VVSCWAWELBZCEtt2TZAGFEHQ84ZBSgnGgKpFSdyNiZA9pz7lRSNnIEN8RtAhBEXFRTHsc71zhjKEVWnj',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    print(response.text)

def getTemplate():
    url = "https://graph.facebook.com/v18.0/1185900442381488?access_token=EAAFaFIJHIucBO8lkTxgeVYZBCVk9ys2Dp9rxYQJjq9pNzmq3mPM7prXh1OKQEtNcB6k1CPr9rp3pua7YfZCKlqdlxhLIEUNNhaTxJi059QRZC8SG4EDwnZAGcBHFjychw0ZBMCqe9VVSCWAWELBZCEtt2TZAGFEHQ84ZBSgnGgKpFSdyNiZA9pz7lRSNnIEN8RtAhBEXFRTHsc71zhjKEVWnj"
    response = requests.get(url)
    print(response.text)

def sendTemplate():
    url = "https://graph.facebook.com/v18.0/256226997571281/messages"
    headers = {
        'Authorization': f'Bearer EAAFaFIJHIucBOzWktAMLZBJ0cyap8B45MCD0G1kPBmlhMU9slYjggDrE6DDUt4SNhn4fUuyOGvVMGJdIn8bPFVFnzVFAHOb98Dngf81lyxqWw9NzhCNdUQn6ObAMVjC7kfRZA1APOoriLrh0XHU8AST6UDR8zdzkcmx8A9chgPhQrRJMa58UteLeHQ9nfE6Q3Sccrcilxu46dHsk8ZD',
        'Content-Type': 'application/json'
    }
    payload = {
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": "917710285988",
    "type": "template",
    "template": {
        "name": "bamci",
        "language": {
            "code": "en"
        },
        "components": [
            {
                "type": "body"
            }
        ]
    }
}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(response.text)


# sendTemplate()

def createNumber():
    url  = 'https://graph.facebook.com/v18.0/256551524204351/phone_numbers'
    headers = {
        'Authorization': 'Bearer EAAFaFIJHIucBO3sM2Fl2F4uOy4qgYC0Rd1pqdRN7UUlLYT3s8FRufgaaZBMsOfzo9rbBEWtr5DSttTbJZAamjPzU3BArsUhDgNONOoRWxVWO97RDJ0EjGzCG5jUiZC8Ff2hVnUhe9oVrXHP3cmVms7wmaQbj7I6lftZBjSfqFLWRnjzDKyJB92TJgy2wD0xykjvCuhwxvDFPvG1VKokZD',
        'Content-Type': 'application/json'
    }
    payload = {
    "cc": "91",
    "phone_number": "7981395086",
    "verified_name": "BamsiProbot"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(response.text)


createNumber()


