# Use "web_server\Scripts\activate" to enter virtual enviroment
# Use "set FLASK_APP=server.py" to set Path
# Use "set FLASK_ENV=development" to enable debug mode
# Use "flask run" to start webserver

from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)   # use flask class to intiatinate app
print(__name__)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/')
# decorator. When browser requeste route(home) directory
# <username> means name passed in browser to url can be used in function
def my_home():
    return render_template('index.html')


@app.route('/<path:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'],)   # use with <form action="/submit_form" method="post" class="reveal-content"> in HTML
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            email = data['email']
            return redirect(url_for("thankyou", email=email))
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong. Try again'


@app.route('/thankyou.html<string:email>')
def thankyou(email):
    return render_template("thankyou.html", email=email, subject='mice')
