import  socket
''''
1.创建套接字 socket.socket(socket.AF_INET,socket.SOCK_STREAM)
2.绑定端口号 tcp_sev_socket.bind(('',9999))
3.监听 tcp_sev_socket.listen(128)
4.拿到客户端的套接字和地址  cli_socket,cli_address=tcp_sev_socket.accept()
5.用客户端的套接字和地址进行收发数据     cli_socket.send(send_data.encode('gbk'))
'''

# 创建套接字
tcp_sev_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定端口号
tcp_sev_socket.bind(('',9999))
# 监听。默认套接字都输主动的，要接收别人的请求必须将套接字变为被动
tcp_sev_socket.listen(128)

while True:
    cli_socket,cli_address=tcp_sev_socket.accept()
    print("接收到来自%s 的连接请求" % str(cli_address))

    recv_data=cli_socket.recv(4096)
    print("接收客户端的数据：%s"%(recv_data.decode('gbk')))
    send_data=input("请输入需要发送的数据：")
    cli_socket.send(send_data.encode('gbk'))

    # 挂掉分机
    cli_socket.close()

# 挂掉总机
tcp_sev_socket.close()