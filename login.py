from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)

@app.route('/login', methods = ['POST','GET'])
def loginpage():
    if request.method=='POST':
        return redirect(url_for(('home')) ) 
    return render_template('login.html')
    
@app.route('/home')
def home():  
    return render_template('home.html')    
if __name__ == '__main__':
    app.run(debug=True)