from flask import Flask,request,render_template
from test_server import Main

from config import host as ip

app = Flask(__name__)

#http://domain.ru/?argument=value.

ip = 'dhome.cmit42.com:1024'

value_arguments = 0
@app.route('/')
def index():
    return render_template('static/index.html')

@app.route('/authorization/')
#http://127.0.0.1:5000/authorization/?login=&password=&submit=
def authorization():
    login = request.args.get('login', '')
    pasword = request.args.get('password', '')
    if login =='admin' and pasword =='admin':
        print('добро пожаловать')
        Main('runcmd')
        return render_template('game.html', ip=ip)
    else:
        return render_template('authorization.html')



@app.route('/game/')
def game():
    left = request.args.get('left', '')
    right = request.args.get('right', '')

    if left == 'ok':
        #Main('left')
        print('left ' + left)
        left = 'no'

    if right == 'ok':
        #Main('right')
        print('right ' + right)
        right = 'no'



    return render_template('game.html',ip=ip)

if __name__ == '__main__':
    app.run(debug = True)


