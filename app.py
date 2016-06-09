from flask import Flask, jsonify
from flask import request
import socket
app = Flask(__name__)

#http://domain.ru/?argument=value.
def Main(message):
    host = '172.27.240.70'
    port = 5001

    mySocket = socket.socket()
    mySocket.connect((host, port))

    while message != 'q':
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()

        return (data)


    mySocket.close()


@app.route('/')
def index():
   value_arguments = request.args.get('argument', '')
   if value_arguments == 'q':
       return Main('q')
   else:
       return Main(value_arguments)
 
@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug = True)


