from flask import Blueprint, render_template, request, flash, jsonify,redirect,url_for
from flask_login import login_required, current_user
from .models import HeartData
from . import db
import json
import joblib
import pandas as pd

views = Blueprint('views', __name__)
model = joblib.load('heart_dis/stroke_prediction_model.pkl')

@views.route('/', methods=['GET'])
@login_required
def home():
    return render_template('diagnostics.html',user=current_user)

@views.route('/give-details',methods=['GET','POST'])
@login_required
def give_details():
    if request.method=='POST':
        cp = request.form.get('cp')
        trestbps = request.form.get('trestbps')
        chol = request.form.get('chol')
        fbs	= request.form.get('fbs')
        restecg	=request.form.get('restecg')
        thalach	= request.form.get('thalach')
        exang = request.form.get('exang')
        oldpeak	= request.form.get('oldpeak')
        slope = request.form.get('slope')
        ca = request.form.get('ca')
        thal = request.form.get('thal')
        target = model.predict(pd.DataFrame.from_dict([{
    'age': int(current_user.age),
    'sex': int(current_user.sex == 'F'),  # Assuming 'F' is encoded as 1
    'cp': int(cp),
    'trestbps': int(trestbps),
    'chol': int(chol),
    'fbs': int(fbs),
    'restecg': int(restecg),
    'thalach': int(thalach),
    'exang': int(exang),
    'oldpeak': float(oldpeak),
    'slope': int(slope),
    'ca': int(ca),
    'thal': int(thal)  # Ensure this feature is included
}]))
        new_data = HeartData(cp=int(cp), trestbps = int(trestbps), chol=float(chol),	fbs=int(fbs), restecg=int(restecg), thalach=int(thalach), exang=int(exang), oldpeak=float(oldpeak), slope=float(slope), ca=int(ca), thal=int(thal), target=int(target),user_id=current_user.id)  
        db.session.add(new_data) #adding the note to the database 
        db.session.commit()
        return render_template('result.html',user=current_user,result=target)
    return render_template('detail.html',user=current_user)



