from flask import Flask,render_template,redirect,url_for,request
from markupsafe import escape

app=Flask(__name__)

@app.route('/guest')
def guest():
    return 'hello'


@app.route('/home/<name>')
def get(name=None):
    return render_template('index.html',name=name)

@app.route('/Home/<name>')
def post(name):
    if name=='poornima':
        return redirect(url_for('guest'))
    else:
        return redirect(url_for('get',name=name))


# Http methods [post,get,Put,Delete]

def Home_page(name):
    return render_template('Home.html',name=name)

@app.route('/login',methods=['GET'])
def login():
    if  request.method=='GET':
        user=request.form['name']
        password=request.form['password']
        return redirect(url_for('Home_page',user))
    else:
        return render_template('login.html')


if __name__=='__main__':
    app.run( port=8000 ,debug=True)
