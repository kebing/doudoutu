# -*-coding:utf-8-*-

# ip格式转换
import struct
import socket

# ipv4用一个整数表示
def ipv4_to_string(ipv4):
    ipv4_n = socket.htonl(ipv4)
    data = struct.pack('I', ipv4_n)
    ipv4_string = socket.inet_ntop(socket.AF_INET, data)
    return ipv4_string
def ipv4_from_string(ipv4_string):
    data = socket.inet_pton(socket.AF_INET, ipv4_string)
    ipv4_n = struct.unpack('I', data)
    ipv4 = socket.ntohl(ipv4_n[0])
    return ipv4
def ipv4_readable2int(ipv4):
    return int(ipv4)
def ipv4_int2readable(ipv4):
    return str(ipv4)

# ipv6用四个整数(tuple或用,分开的字符串)表示
def ipv6_to_string(ipv6):
    ipv6_n = (socket.htonl(ipv6[0]),
              socket.htonl(ipv6[1]),
              socket.htonl(ipv6[2]),
              socket.htonl(ipv6[3]))
    data = struct.pack('IIII', ipv6_n[0], ipv6_n[1], ipv6_n[2], ipv6_n[3])
    ipv6_string = socket.inet_ntop(socket.AF_INET6, data)
    return ipv6_string
def ipv6_from_string(ipv6_string):
    data = socket.inet_pton(socket.AF_INET6, ipv6_string)
    ipv6_n = struct.unpack('IIII', data)
    ipv6 = (socket.ntohl(ipv6_n[0]),
            socket.ntohl(ipv6_n[1]),
            socket.ntohl(ipv6_n[2]),
            socket.ntohl(ipv6_n[3]))
    return ipv6
def ipv6_tuple2readable(ipv6):
    return str(ipv6[0]) + ',' + str(ipv6[1]) + ',' + str(ipv6[2]) + ',' + str(ipv6[3])
def ipv6_readable2tuple(ipv6):
    return tuple(ipv6.split(','))
