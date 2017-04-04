from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route('/contacts/create')
def create_contact():
    return 'Coming soon...'

@app.route('/contacts/')
def list_contacts():
    return 'Coming soon...'

if __name__ == "__main__":
    app.run()