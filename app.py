from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    msg = Message('New Contact Form Submission',
                  sender='your_email@example.com',
                  recipients=['your_email@example.com'])
    msg.body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
    
    try:
        mail.send(msg)
        return 'Message sent successfully!'
    except Exception as e:
        return f'Error: {e}'

@app.route('/subscribe', methods=['POST'])
def subscribe():
    subscribe_email = request.form['subscribe-email']
    
    msg = Message('Newsletter Subscription',
                  sender='your_email@example.com',
                  recipients=[subscribe_email])
    msg.body = 'Thank you for subscribing to our newsletter!'
    
    try:
        mail.send(msg)
        return 'Subscription successful!'
    except Exception as e:
        return f'Error: {e}'

if __name__ == '__main__':
    app.run(debug=True)
