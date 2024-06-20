from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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
    booking = {'email': emailx, 'name': name, 'message': message}
    bookings.append(booking)
    print(bookings)
  return render_template('form.html')


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
