from sys import stdout
from makeup_artist import Makeup_artist
import logging
from flask import Flask, request, url_for, redirect, render_template, Response, session, flash
from flask_socketio import SocketIO, emit, send
from camera import Camera, decode_img, img_to_txt
from utils import *
from werkzeug.utils import secure_filename
from flask import send_from_directory

import os
import time
from io import BytesIO
from PIL import Image
import base64
from random import randint
import cv2
import numpy as np
from flask_session import Session
import boto3
import io
import pymysql


UPLOAD_FOLDER = '/static/images/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(stdout))
app.secret_key = 'secret!'
# app.config['SESSION_TYPE'] = 'filesystem'
app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['HOST'] = '0.0.0.0'
# Session(app)
socketio = SocketIO(app)
camera = Camera(Makeup_artist())

access_key_id='AKIA3SLO3MAN7CIUHAY6'
secret_access_key='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'



def uploadImage(filename, key):
    s3 = boto3.client('s3',
                          aws_access_key_id=access_key_id,
                          aws_secret_access_key=secret_access_key,
                          region_name='us-east-2'
                          )
    with open(filename, 'rb') as f:
        s3.upload_fileobj(f, 'webapplogin', key )


def mysqlcon(query):
    conn = pymysql.connect( 
        host='localhost', 
        user='SiemGHM',  
        password = "$iemGH12", 
        db='flasklogin',
        autocommit=True 
        )

    cur = conn.cursor() 
    cur.execute(query) 
    output = cur.fetchall() 
    # conn.commit()
    # conn.close()
    return output 
      
    # To close the connection 
    conn.commit()
    conn.close()
    
def signupdb(fname, lname, username, email, password):
    query = "insert into users2 (email, username, passwrd, LastName, FirstName) values ('{}', '{}', '{}', '{}', '{}')".format(email, username, password, lname, fname)
    ex = mysqlcon(query)
    uID = mysqlcon("select UserID from users2 where username='{}'".format(username))
    print(uID, "JLKJLKJLJLKJLKJL", ex)
    # query = "insert into Customers (UserID, fname, lname, lvl) values ({},'{}','{}', '{}')".format(int(uID[0][0]),name, lname, level)
    # ex = mysqlcon(query)
    
    return uID


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def image_to_byte_array(image:Image):
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, format=image.format)
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr


def add_faces_to_collection(bucket, photo, collection_id):
    client = boto3.client('rekognition',
                            aws_access_key_id=access_key_id,
                            aws_secret_access_key=secret_access_key,
                            region_name='us-east-2'
                            )

    response = client.index_faces(CollectionId=collection_id,
                                    Image={'S3Object': {
                                        'Bucket': bucket,'Name': photo}},
                                    ExternalImageId=photo,
                                    MaxFaces=1,
                                    QualityFilter="AUTO",
                                    DetectionAttributes=['ALL'])

    print('Results for ' + photo)
    print('Faces indexed:')
    if response['FaceRecords']:
        print("Face Successfully added")
        for faceRecord in response['FaceRecords']:
            print('  Face ID: ' + faceRecord['Face']['FaceId'])
            print('  Location: {}'.format(
                faceRecord['Face']['BoundingBox']))
            # update the list of users avilable at the user end
            # self.list_faces_in_collection()
    else:
        print('Face not detected, Please provide clear photo!')
        print('Face not detected, Please provide clear photo!')
        for unindexedFace in response['UnindexedFaces']:
            print(' Location: {}'.format(
                unindexedFace['FaceDetail']['BoundingBox']))
            print(' Reasons:')
            for reason in unindexedFace['Reasons']:
                print('   ' + reason)
    return len(response['FaceRecords'])

def recognizeFace():
    photo= 'result.jpg'

    # client access for rekognition
    client=boto3.client('rekognition',
                        aws_access_key_id = access_key_id,
                        aws_secret_access_key=secret_access_key,
                        region_name='us-east-2')


    # encode the image and get a response
    with open(photo, 'rb') as source_image:
        source_bytes= source_image.read()

    # #  to use phot from the aws s3 storage, apply this code
    response= client.search_faces_by_image(
        CollectionId='webappcollection',
        Image={'Bytes': source_bytes}
    )

    # since response is a dictionary, we can loop it
    #print(response)
    return response


@app.route('/signupres', methods=['GET', 'POST'])
def upload_file():
    uploaded_file = request.files['file']
    email = request.form['email']
    password = request.form['password']
    username = request.form['username']
    fname = request.form['fname']
    lname = request.form['lname']
    
    uid = signupdb(fname, lname, username, email, password)
    print(uid)
    uid = uid[0][0]
    print(uid)
    

    if uploaded_file.filename != '':
        uploaded_file.save("{}.jpg".format(uid))
        # upload_file()
    print("step1")
    uploadImage("{}.jpg".format(str(uid)), str(uid))
    print("step2")
    fn = add_faces_to_collection("webapplogin", "{}".format(uid), "webappcollection")
    print(fn, "fn")
    return "Done" #redirect(url_for('index'))


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)




    


@socketio.on('input image', namespace='/test')
def test_message(input):
    input = input.split(",")[1]
    camera.enqueue_input(input)
    # camera.process_one()
    image_data = input # Do your magical Image processing here!!
    # image_data.encode()
    # image_data.decode('utf-8')
    # image_data.decode('utf-8')
    # image = decode_img(image_data)
    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$398759843759832475983274985$")
    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$398759843759832475983274985$")
    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$398759843759832475983274985$")
    
    # # print(image_data)
    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    img = image_data
    iterr = randint(1,100000)

    im = Image.open(BytesIO(base64.b64decode(img)))
    # im.show()
    # im.convert('1')
    # im.show()
    # im = im.save("image{}.jpg".format(iterr))

    face_cascade = cv2.CascadeClassifier('face.xml')

    # #Convert to grayscale
    grayor = cv2.cvtColor(np.float32(im), cv2.COLOR_BGR2GRAY)

    gray = np.array(grayor, dtype='uint8')
    

    #Look for faces in the image using the loaded cascade file
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    

    iterr+=1

    if len(faces) > 0:
        print("Found "+str(len(faces))+" face(s)")
        
        im = im.save("result.jpg")
        print("""########
        
        
        
        
        
        
        
        $$$$$$$$$$$$$$$$$
        
        
        
        
        
        
        
        %%%%%%%%%%
        
        
        
        
        
        
        
        
        %%%%%%%%%%%%""")
        resp = recognizeFace()
        # print(resp)
        # user = "user{}".format(randint(1, 10000000000000))
        # session["user"] = user
        # print(user)
        # imagebytes = image_to_byte_array(im)
        # res = add_faces_to_collection('webapplogin', imagebytes, 'webappcoll', 'asdhjk')
        # print(res)
        if resp['FaceMatches'] != []:
            id = resp['FaceMatches'][0]['Face']['ExternalImageId']
            print(id)
            query = "select username, firstname from users2 where userid ={}".format(int(id))
            uf = mysqlcon(query)
            username, fname = uf[0][0], uf[0][1]

            # login(username, fname)
            emit('redirect', {'url': url_for('login', username=username)})
        # emit('redirect', {'url': url_for('index')})

    
    while True:
        time.sleep(30)
        
    


    # image_data.show()
    # image_data.convert('1')
    # image_data.show()
    image_data = "data:image/jpeg;base64," + image_data
    # print("OUTPUT " + image_data)

    emit('out-image-event', {'image_data': image_data}, namespace='/test')
    #camera.enqueue_input(base64_to_pil_image(input))


@socketio.on('connect', namespace='/test')
def test_connect():
    app.logger.info("client connected")





@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/signup')
def signup():
    
    return render_template('signup.html')


@app.route('/loginn')
def loginn():
    """Video streaming home page."""
    return render_template('login.html')



def gen():
    """Video streaming generator function."""

    app.logger.info("starting to generate frames!")
    while True:
        frame = camera.get_frame() #pil_image_to_base64(camera.get_frame())
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/lo')
def logout():
    p=session.pop('user')
    return redirect(url_for('index'))


@app.route('/lsakdfkjh0sdifkhg29748fdg51924/<string:username>')
def login(username):
    print("I am here with {}".format(username))
    # fname = fname
    session["user"]=username
    return redirect(url_for('li'))



@app.route('/loggedin')
def li():
    
    if "user" not in session:
        return redirect(url_for('index'))

    user = session['user']
    print(session['user'], "userrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
    return render_template('li.html', user=user)


if __name__ == "__main__":
    # socketio.run(app,host='0.0.0.0')
    app.run(host='0.0.0.0')