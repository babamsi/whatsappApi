from heyoo import WhatsApp
from flask import Flask, jsonify
from flask import request
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import time
import os
import pathlib
from pathlib import Path
import requests
import json
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv() 
UPLOAD_FOLDER = './data/'

mytoken = os.getenv("TOKEN")

app = Flask(__name__)


client = MongoClient('mongodb+srv://bamsi:Alcuduur40@cluster0.vtlehsn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)

messenger = WhatsApp(token=mytoken,  phone_number_id='256226997571281');


@app.route('/')
def test():
    
    db = client["probot0"]
    contacts = db['contacts']
    # contact_dict = {
    #      "name": "Veera Pedapati",
    #      "mobile": "918121285872",
    #      "avatar": "https://media.istockphoto.com/id/1337144146/vector/default-avatar-profile-icon-vector.jpg?s=612x612&w=0&k=20&c=BIbFwuv7FxTWvh5S3vB6bkT0Qv8Vn8N5Ffseq84ClGI="
    # }

    # contacts.insert_one(contact_dict)
    users = contacts.find()
    users_list = []
    for item in users:
        users_dict = {
            "name": item["name"],
            "mobile": item["mobile"],
            "avatar": item["avatar"]
        }
    users_list.append(users_dict)
    # print(users_list)


    return "working...."


@app.route('/getContacts')
def getContacts():
    db = client["probot0"]
    contacts = db['contacts']
    
    users = contacts.find()
    users_list = []
    for item in users:
        users_dict = {
            "name": item["name"],
            "mobile": item["mobile"],
            "avatar": item["avatar"]
        }
        users_list.append(users_dict)
    # print(users_list)
    return jsonify(users_list)


@app.route("/createContact", methods=["POST"])
@cross_origin()
def createContact():
     incoming_msg = request.get_json();
     db = client["probot0"]
     contacts = db['contacts']
     users = contacts.find();
     name = incoming_msg["name"]
     number = incoming_msg["mobile"]
     for i in users:
          if i["name"] == name or i["mobile"] == number:
               return "this contact name or number already been there"
    
     contact_dict = {
          "name": incoming_msg['name'],
          "mobile": incoming_msg["mobile"],
          "avatar": "https://media.istockphoto.com/id/1337144146/vector/default-avatar-profile-icon-vector.jpg?s=612x612&w=0&k=20&c=BIbFwuv7FxTWvh5S3vB6bkT0Qv8Vn8N5Ffseq84ClGI="
     }
     contacts.insert_one(contact_dict)
     return "saved"


@app.route('/deleteContact', methods=["POST"])
@cross_origin()
def deleteContact():
     incoming_msg = request.get_json();
    #  print(incoming_msg)
     db = client["probot0"]
     contacts = db['contacts']
     for i in incoming_msg["body"]:
        contacts.delete_many({'name': i})

     return "deleted"

@app.route('/send', methods=["POST"])
@cross_origin()
def send():
    incoming_msg = request.get_json();
    print(incoming_msg["body"])
    for i in incoming_msg["body"]:
         messenger.send_message(incoming_msg["txt"], i["mobile"])
    # print(incoming_msg["txt"])
    # n = ["918121285872", "916363617779"]
    try:
        
    #     for i in n:
    #         media_id = messenger.upload_media(
    #         media='./bb.jpeg')['id']
    #         messenger.send_image(
    #         image=media_id,
    #         recipient_id=i,
    #         caption="This is a sample message",
    #         link=False
    # )
            # print(type(incoming_msg))
        for i in incoming_msg["body"]:
            #  messenger.send_message(incoming_msg["txt"], i["mobile"])
            #  print(incoming_msg["txt"], i["mobile"])
            #  print(i)
             return "sent"
            # print(i["mobile"])
        #     for j in incoming_msg[i]:
                    # messenger.send_message('hello, this is a one to many message', j["mobile"])
                    # print(incoming_msg[i])
            # return "done...."
    except Exception as e:
        return e
    
    return incoming_msg


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/file', methods=["POST"])
@cross_origin()
def file():
    incoming_msg = request.form.get('text')
    mob = request.form.getlist("mobile")

    # print(mob)
    # print(incoming_msg)
    if 'file' not in request.files:
            print("no file part")
            return "no file detected"
    file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
    if file.filename == '':
            print('No selected file')
            return "not selected file...."
    if file and allowed_file(file.filename):
            
            from sendImage import send
            
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("file downloaded")
            time.sleep(1);
            send(fileName=filename, txt=incoming_msg, mobile=mob);
            # f = open(f'{di}/rr.png', "x")
            # print(os.path.join(app.config['UPLOAD_FOLDER'], 'coll.jpeg'))
            # print(os.path.join(UPLOAD_FOLDER, '/co'))
            # print(di)   # to get the current working directory
            return "file downloaded"
    return "ok"
   

@app.route('/templates', methods=["GET"])
@cross_origin()
def getTemplates():
    url = " https://graph.facebook.com/v19.0/256551524204351/message_templates"
    headers = {
        'Authorization': f'Bearer EAAFaFIJHIucBOZCcRvGMbnYZAEpC2vAB4qUZClHTBhHHrniKTZAgUWjChs3F1NN1NM3VWSoE0bimT8IqB3ZCSSC4nzuOGjEMm6mzvIGB5MZALl2yi9IHxBxYXbAZCAbq8unQmgyJZAby8vBhDmq3DaPTht9FtbMZBC3TX9TorHcXWfnIvziatKoAdcdqmkFqGzwfF8Q2XF297Jfyj5ZAfaZB0oZD',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    # print(response.text)
    return response.text

@app.route('/sendTemplate', methods=["POST"])
@cross_origin()
def sendTemplate():
     incoming_msg = request.get_json();

     url = 'https://graph.facebook.com/v18.0/256226997571281/messages'
     headers = {
        'Authorization': f'Bearer EAAFaFIJHIucBOyPNrGuUwVQTI3CtlSHMzAI2of1HMG8ueenb04z1J3fBpb9rHQ2arruvsnOyLyCklhZBIBnkWFvddGD27MOZB5d7zQOpbevHFmaSUbi2IpzdUyStPaycJtKev0sHRtwSCXp3sc5klnWHBjEoWrFxPuNG9eYfFOcFd2tMjR0gsxJCKZByDbe7ZCTMlSaZAgOX3Lydb6DcZD',
        'Content-Type': 'application/json'
    }
    #  print(incoming_msg["body"])
     for i in incoming_msg["body"]:
        # print(incoming_msg["txt"])
        payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": i["mobile"],
        "type": "template",
        "template": {
            "name": str(incoming_msg["txt"]),
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
        return response.text
     return "ok"

@app.route('/sendLocation', methods=["POST"])
@cross_origin()
def sendLocation():
    incoming_msg = request.get_json();
    url = 'https://graph.facebook.com/v18.0/256226997571281/messages'
    headers = {
        'Authorization': f'Bearer {mytoken}',
        'Content-Type': 'application/json'
    }
    for i in incoming_msg["body"]:
        payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": i["mobile"],
        "type": "location",
        "location": {
            "latitude": incoming_msg["lat"],
            "longitude": incoming_msg["long"]
        }
    }
        # print(messenger.send_location(lat=, long=, recipient_id="917710285988"))
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        return response.text








# mediaId = messenger.upload_media(media='./sim.mp4')['id']
# print(mediaId)

# messenger.send_video(
#         video=mediaId,
#         recipient_id="917710285988",
#         link=False
#     )

if __name__ == '__main__':
    app.run()