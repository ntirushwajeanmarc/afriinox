from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


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

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
