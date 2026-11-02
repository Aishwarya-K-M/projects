from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Result
from . import db
import json
from torchvision import transforms
from . import torch,model,model_loaded
from . import app


views = Blueprint('views', __name__)

import os
import cv2
from PIL import Image

import numpy as np

def preprocess(image):
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    image = transform(image)
    image = image.unsqueeze(0)
    return image


# Predict
def predict(image):
    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)
    return predicted.item()

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/diagnostic',methods=['GET', 'POST'])
@login_required
def diagnostic():
    image = None
    result = None
    if request.method == 'POST':
        f = request.files['myImage'] 
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        #print(type(Image.open(os.path.join('alzheimer_detection\website\static', f.filename))))
        image = Image.open(os.path.join('alzheimer_detection\website\static', f.filename)).convert('RGB') 
        preprocessed_image = preprocess(image)
        label = predict(preprocessed_image)
        labels = ['mild Alzheimer\'s Disease', 'moderate Alzheimer\'s Disease', 'non-demented', 'very mild Alzheimer\'s Disease']
        if label in range(len(labels)):
            result = labels[label]
            res = Result(result=result, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(res) #adding the note to the database 
            db.session.commit()
            flash('Classification done!', category='success')
        else: 
            result = 'error'
            flash('Image upload has error', category='error')
    return render_template("diagnostic.html", user=current_user,image=image,result=result)

@views.route('/results', methods=['GET'])
def result():  
    return render_template("results.html", user=current_user)