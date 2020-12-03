# Server python solution to Baltic Berry database

from flask import Flask, url_for, jsonify, session, make_response, request, abort, render_template, redirect
from BalticDao import balticDao

# Create the Flask app
app = Flask(__name__,
            static_url_path='',
            static_folder='templates')

@app.route('/')
def home():
    if not 'username' in session:
        return redirect(url_for('login'))

    return redirect(url_for('harvestData'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['uname'] != '' or request.form['psw'] != '':
            # Checking username and password in  DAO
            username = request.form['uname']
            password = request.form['psw']
            #For development process only! 
            #print("Username:" +username, "Password:" +password)
            foundUser = balticDao.checkUser(username, password)
            # if the user is not in the database, throw the error
            if not foundUser:
                error = 'Invalid Credentials. Please try again.'
            # if the user exists move to harvest data   
            else:
                session['username'] = username
                return redirect(url_for('harvestData'))
        else:
            print(error)
            return error
    return render_template('index.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)  
    return redirect(url_for('login'))

@app.route('/home')

def findById(id):
    if not 'username' in session:
        abort(401)

    return jsonify(balticDao.findById(id))

#curl "http://127.0.0.1:5000/harvests/101"

@app.route('/harvests', methods=['POST'])

def create():

    # Check that the request has JSON data (if not returns a 400 error)
    if not request.json:
        abort(400) 

    harvest={
        "id": request.json["id"],
        "employeeName": request.json["employeeName"],
        "fieldSection":request.json["fieldSection"],
        "variety":request.json["variety"],
        "quantity":request.json["quantity"]
    } #read the request object and create a new harvest

    return jsonify(balticDao.create(harvest))


# This is a put and it takes in the id from the url
@app.route('/harvests/<id>', methods =['PUT'])

def update(id):