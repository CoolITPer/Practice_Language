import  socket

udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_socket.bind(('', 8888))


while True:
    recv_data,recv_address=udp_socket.recvfrom(4096)
    print("收到来自%s的数据：%s,"%(recv_address,recv_data.decode()))

    udp_socket.sendto(recv_data,recv_address)