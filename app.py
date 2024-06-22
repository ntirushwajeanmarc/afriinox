from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

app.secret_key = 'fc62fd5d-8247-4c1d-9496-f75a929001f9'
bookings = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/services')
def services():
    return render_template('ourservices.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/getinvolved', methods=['POST', 'GET'])
def book():
    if request.method == 'POST':

        emailx = request.form.get('email')
        name = request.form.get('name')
        message = request.form.get('message')
        contact = request.form.get('contact')

        if not emailx:
            return "Email is required", 400

        booking = {
            'email': emailx,
            'name': name,
            'message': message,
            'contact': contact
        }
        bookings.append(booking)
        print(bookings)

        try:
            msg = Message(subject='Thank you for getting involved!',
                          sender='info@afriiinnox.com',
                          recipients=[emailx, 'afriinnox@gmail.com'])

            msg.body = f"Hello {name},\n\n with {contact} thank you for reaching out!"
            mail.send(msg)
        except Exception as e:
            print(f"Failed to send email: {e}")
            return "Failed to send email", 500

        return redirect(url_for('thank_you'))

    return render_template('form.html')


@app.route('/thankyou')
def thank_you():
    return "Thank you for getting involved! We've sent you a confirmation email."


@app.route('/invented')
def invented():
    return render_template('invented.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
