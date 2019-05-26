
import socket
import threading
def recv_msg( udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)
def send_msg(udp_socket, dest_port,dest_ip):
    '''发送数据'''
    while True :
        send_data = input("输入发送的数据： ")
        udp_socket.sendto(send_data.encode('utf-8'), (dest_ip,dest_port))
def main():
    #创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #绑定本地信息
    udp_socket.bind("", 78900)
    #获取对方ip
    dest_ip = input("请输入对方IP： ")
    dest_port = int(input("请输入对方port： "))
    #接受数据
    #创建线程执行接受发送功能
    t_recv = threading.Thread(target=recv_msg(), args=(udp_socket, ))
    t_send = threading.Thread(target=send_msg(), args=(udp_socket, dest_port,dest_ip))


if __name__ == '__main__':
    main()