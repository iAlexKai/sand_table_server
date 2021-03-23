from flask import Flask, flash, redirect, render_template, request, url_for, session
from flask_socketio import SocketIO, emit, disconnect
import serial
from threading import Lock

# port 串口号
port = 'COM17'
# baudrate 波特率
baudrate = 115200


# timeout 读取串口等待时间，超时则返回异常  0说明不等
timeout = 0
async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket_ = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()


@app.route('/')
def home():
    # return render_template('socket.html', async_mode=socket_.async_mode)
    return render_template('home.html')


####################################################
#### socket
####################################################


@socket_.on('start_server', namespace='/test')
def start_socket_to_raspberry():
    # encoding: utf-8
    import socket
    import time
    # 套接字接口
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置IP和端口
    host = '10.28.191.87'
    port = 2222
    # bind绑定该端口
    mySocket.bind((host, port))
    mySocket.listen(10)

    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response', {'data': 'Server started!', 'count': session['receive_count']})

    while True:
        # 接收客户端连接
        print("等待连接....")
        client, address = mySocket.accept()
        session['receive_count'] = session.get('receive_count', 0) + 1

        message_to_send = "新连接，IP地址为：{}，端口为：{}".format(address[0], address[1])
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response', {'data': message_to_send, 'count': session['receive_count']})

        print("新连接")
        print("IP is %s" % address[0])
        print("port is %d\n" % address[1])
        while True:
            # 读取消息
            msg = client.recv(1024)
            # 把接收到的数据进行解码
            print(msg.decode("utf-8"))

            message_to_send = "收到新消息：{}".format(msg.decode("utf-8"))
            session['receive_count'] = session.get('receive_count', 0) + 1
            emit('my_response', {'data': message_to_send, 'count': session['receive_count']})

            if msg == b"qq":
                message_to_send = "传输结束，当前socket连接断开，请点击\"Start Server\"以接受新的连接"
                session['receive_count'] = session.get('receive_count', 0) + 1
                emit('my_response', {'data': message_to_send, 'count': session['receive_count']})
                client.close()
                mySocket.close()
                print("程序结束\n")
                exit()


####################################################
#### login
####################################################
@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('car_control'))

    return render_template('login.html', error=error)


@app.route('/home_control/', methods=['GET', 'POST'])
def home_control():
    input_addr = request.args.get('addr')
    return redirect(url_for(input_addr))


@app.route('/car_view/', methods=['GET', 'POST'])
def car_view():
    # 给前端页面展示的数据只能传到html文件中，而不能直接传到script中
    return render_template('socket.html', async_mode=socket_.async_mode)


@app.route('/car_control/', methods=['GET', 'POST'])
def car_control():
    return render_template("car_control.html")


@app.route('/car_control/fire_high', methods=['GET', 'POST'])
def fire_high():

    print("Python script send command: fire_high")
    # # 这里写串口命令 FC1234
    # ser = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
    # # 发送16进制命令
    # ser.write(bytes([0xAA, 0xFB, 0x00, 0x6F, 0x01]))
    return render_template('car_control.html')


@app.route('/car_control/fire_low', methods=['GET', 'POST'])
def fire_low():

    print("Python script send command: fire_low")
    # 这里写串口命令 FC1234
    # ser = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
    # # 发送16进制命令
    # ser.write(bytes([0xAA, 0xFB, 0x00, 0x6F, 0x02]))
    return render_template('car_control.html')


@app.route('/car_control/fire_stop', methods=['GET', 'POST'])
def fire_stop():

    print("Python script send command: fire_stop")
    # 这里写串口命令 FC1234
    # ser = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
    # # 发送16进制命令
    # ser.write(bytes([0xAA, 0xFB, 0x00, 0x6F, 0x03]))
    return render_template('car_control.html')


@app.route('/car_control/amb_high', methods=['GET', 'POST'])
def amb_high():

    print("Python script send command: amb_high")
    # # 这里写串口命令 FC1234
    # ser = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
    # # 发送16进制命令
    # ser.write(bytes([0xAA, 0xFB, 0x00, 0xCB, 0x01]))
    return render_template('car_control.html')


@app.route('/car_control/amb_low', methods=['GET', 'POST'])
def amb_low():

    print("Python script send command: amb_low")
    # # 这里写串口命令 FC1234
    # ser = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
    # # 发送16进制命令
    # ser.write(bytes([0xAA, 0xFB, 0x00, 0xCB, 0x02]))
    return render_template('car_control.html')


@app.route('/car_control/amb_stop', methods=['GET', 'POST'])
def amb_stop():

    print("Python script send command: amb_stop")
    # # 这里写串口命令 FC1234
    # ser = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
    # # 发送16进制命令
    # ser.write(bytes([0xAA, 0xFB, 0x00, 0xCB, 0x03]))
    return render_template('car_control.html')


@app.route('/car_control/bus_high', methods=['GET', 'POST'])
def bus_high():

    print("Python script send command: bus_high")
    # # 这里写串口命令 FC1234
    # ser = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
    # # 发送16进制命令
    # ser.write(bytes([0xAA, 0xFB, 0x00, 0xEE, 0x01]))
    return render_template('car_control.html')


@app.route('/car_control/bus_low', methods=['GET', 'POST'])
def bus_low():

    print("Python script send command: bus_low")
    # # 这里写串口命令 FC1234
    # ser = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
    # # 发送16进制命令
    # ser.write(bytes([0xAA, 0xFB, 0x00, 0xEE, 0x02]))
    return render_template('car_control.html')


@app.route('/car_control/bus_stop', methods=['GET', 'POST'])
def bus_stop():

    print("Python script send command: bus_stop")
    # # 这里写串口命令 FC1234
    # ser = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
    # # 发送16进制命令
    # ser.write(bytes([0xAA, 0xFB, 0x00, 0xEE, 0x03]))
    return render_template('car_control.html')


if __name__ == "__main__":
    # app.run(debug=True)
    socket_.run(app, debug=True)