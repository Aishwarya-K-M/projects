from flask import Blueprint, render_template, request, flash
from website import model,vectorizer
import emoji
import stanza


nlp = stanza.Pipeline(lang='hi', processors='tokenize')

display = Blueprint('display', __name__)


def unicode_escape(chars, data_dict):
    return ' '+chars.encode('unicode-escape').decode()+' '

@display.route('/')
def home():
    return render_template('home.html')


@display.route('/bullying_detection', methods=['GET', 'POST'])
def bullying_detection():
    prediction = None
    if request.method == 'POST':
        user_input = request.form['text']
        emoji.replace_emoji(user_input, replace=unicode_escape)
        transformed_input = vectorizer.fit_transform([user_input])
        prediction = model.predict(transformed_input)[0]
        if(prediction==1):
            flash("That's kind of rude. Please refrain from saying that...Have a great day!",category='error')
        else:
            flash("That's a pleasant thing to say...Have a great day",category='message')
    
    return render_template('base.html', prediction=prediction)



@display.route('/about')
def about():
    return render_template('about.html')

