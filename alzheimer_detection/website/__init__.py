from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

import os
import torch

from efficientnet_pytorch import EfficientNet

MODEL_PATH = 'alzheimer_detection\website\static\eff_model_pred.pth'

try:
    # Load model
    model = EfficientNet.from_pretrained('efficientnet-b0', num_classes=4)
    model.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device('cpu')))
    model.eval()
    model_loaded = True
except FileNotFoundError:
    print('Error')
    model_loaded = False


'''
st.write('Please upload an MRI image.')

# Load image
uploaded_file = st.file_uploader("Choose an MRI image...", type=["jpg", "jpeg"])
if uploaded_file is not None and model_loaded:
    image = Image.open(uploaded_file).convert('RGB')  # Ensure image is RGB
    st.image(image, caption='Uploaded MRI.', use_column_width=True)
    st.write("Classifying...")
    preprocessed_image = preprocess(image)
    label = predict(preprocessed_image)
    labels = ['mild Alzheimer\'s Disease', 'moderate Alzheimer\'s Disease', 'non-demented', 'very mild Alzheimer\'s Disease']
    if label in range(len(labels)):
        st.write(f'The model predicts that this MRI image is from a {labels[label]} patient.')
    else:
        st.error('An error occurred during classification.')

'''
def create_app():
    global app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'xxxxx'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['UPLOAD_FOLDER'] = 'alzheimer_detection\website\static'


    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Result
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')