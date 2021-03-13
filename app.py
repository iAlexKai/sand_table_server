from flask import Flask, flash, redirect, render_template, request, url_for, jsonify
import serial

# port 串口号
port = 'COM17'
# baudrate 波特率
baudrate = 115200


# timeout 读取串口等待时间，超时则返回异常  0说明不等
timeout = 0
app = Flask(__name__)
app.secret_key = 'random string'


@app.route('/')
def home():
    return render_template('home.html')


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
    return render_template("car_view.html", message_to_show="欢迎使用车辆监控平台")


@app.route('/car_view/start_server')
def start_server():
    # encoding: utf-8
    # import socket
    # import time
    # print("服务端开启")
    # # 套接字接口
    # mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # # 设置IP和端口
    # host = '192.168.124.3'
    # port = 2222
    # # bind绑定该端口
    # mySocket.bind((host, port))
    # mySocket.listen(10)
    # print("Before return")
    # while True:
    #     # 接收客户端连接
    #     print("等待连接....")
    #     client, address = mySocket.accept()
    #     print("新连接")
    #     print("IP is %s" % address[0])
    #     print("port is %d\n" % address[1])
    #     while True:
    #         # 读取消息
    #         msg = client.recv(1024)
    #         # 把接收到的数据进行解码
    #         print(msg.decode("utf-8"))
    #         print("读取完成")
    #         if msg == b"hello":
    #             print("你好，老弟")
    #         if msg == b"qq":
    #             client.close()
    #             mySocket.close()
    #             print("程序结束\n")
    #             exit()

    return render_template("car_view.html")


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
    app.run(debug=True)
