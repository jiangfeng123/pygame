"""
TCP服务端
1、导入模块
2、创建套接字
3、设置地址重用
4、绑定端口
5、设置监听，让套接字由主动变为被动接收
6、接受客户端连接 定义函数 request_handler()
7、接收客户端浏览器发送的请求协议
8、判断协议是否为空
9、拼接响应的报文
10、发送响应报文
11、关闭操作

"""
import socket
# 导入模块
from application import app
import sys


#  ws = WebServer()
#  ws.start()

class WebServer(object):

    # 初始化方法
    def __init__(self, port):
        # 1、导入模块
        # 2、创建套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 3、设置地址重用
        #                                 当前套接字            地址重用         值True
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 4、绑定端口
        tcp_server_socket.bind(("", port))
        # 5、设置监听，让套接字由主动变为被动接收
        tcp_server_socket.listen(128)

        # 定义实例属性，保存套接字对象
        self.tcp_server_socket = tcp_server_socket

    def start(self):
        """启动Web服务器"""
        print("Web服务器已经启动...等待客户端连接中....")
        # 6、接受客户端连接 定义函数 request_handler()
        while True:
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            print("新客户来了:", ip_port)
            # 调用功能函数处理请求并且响应
            self.request_handler(new_client_socket, ip_port)

    def request_handler(self, new_client_socket, ip_port):
        """接收信息，并且做出响应"""
        # 7、接收客户端浏览器发送的请求协议
        request_data = new_client_socket.recv(1024)
        # print(request_data)
        # 8、判断协议是否为空
        if not request_data:
            print("%s客户端已经下线!" % str(ip_port))
            new_client_socket.close()
            return

        # 使用 application文件夹 app 模块的 application() 函数处理
        response_data = app.application("static", request_data, ip_port)

        # 10、发送响应报文
        new_client_socket.send(response_data)

        # 11、关闭当前连接
        new_client_socket.close()


def main():
    """主函数"""

    """
    1、导入sys 模块
    2、获取系统传递到程序的参数
    3、判断参数格式是否正确
    4、判断端口号是否是一个数字
    5、获取端口号
    6、在启动Web服务器的时候，使用指定的端口
    """
    # 2、获取系统传递到程序的参数['09-简单Web服务器_命令行启动.py', '8888', 'aaa', 'bbb', 'xxxx', '123']
    # ['09-简单Web服务器_命令行启动.py', '8888', 'aaa', 'bbb', 'xxxx', '123']
    params_list = sys.argv
    # print(params_list)
    # 3、判断参数格式是否正确
    if len(sys.argv) != 2:
        print("启动失败，参数格式错误!正确格式:python3 xxx.py 端口号")
        return
    # 4、判断端口号是否是一个数字
    #             0                     1
    # ['09-简单Web服务器_命令行启动.py', '8888']
    if not sys.argv[1].isdigit():
        print("启动失败，端口号不是一个纯数字!")
        return

    # 5、获取端口号
    port = int(sys.argv[1])
    # 6、在启动Web服务器的时候，使用指定的端口

    # 创建WebServer类的对象
    ws = WebServer(port)
    # 对象.start() 启动Web服务器
    ws.start()


if __name__ == '__main__':

    main()