from flask import Flask, render_template, request 
app = Flask(__name__) 
@app.route('/') 
def home(): 
    return ''' 
    <h2><center>Hello</center></h2> 
    <center> 
        <a href="/register">Go to Registration Page</a> 
    </center> 
    ''' 
@app.route('/register') 
def register(): 
    return render_template('register.html') 
@app.route('/success', methods=['POST']) 
def success(): 
    name = request.form['name'] 
    email = request.form['email'] 
    return render_template('success.html', name=name, email=email) 
if __name__ == '__main__':
    app.run(debug=True)