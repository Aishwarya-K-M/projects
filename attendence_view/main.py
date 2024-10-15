from website import create_app
from flask import url_for


app = create_app()

if __name__=='__main__':
    
    app.run(debug=True)
    try:
        app.add_url_rule('/favicon.ico',
                 redirect_to=url_for('static', filename='favicon.ico'))
    except:
        pass