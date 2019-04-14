import socket
# import threading

# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# retrieve local hostname
local_hostname = socket.gethostname()

# get fully qualified hostname
local_fqdn = socket.getfqdn()

# get the according IP address
ip_address = socket.gethostbyname(local_hostname)

# output hostname, domain name and IP address
print(f"working on {local_hostname} ({local_fqdn}) with {ip_address}")

# bind the socket to the port 23456
server_address = (ip_address, 23456)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

# listen for incoming connections (server mode) with one connection at a time
sock.listen(1)

while True:
    # wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        # show who connected to us
        print ('connection from', client_address)

        # receive the data in small chunks and print it
        while True:
            data = connection.recv(64)
            if data:
                # output received data
                print ("Data: %s" % data)
            else:
                # no more data -- quit the loop
                print ("no more data.")
                break
    finally:
        # Clean up the connection
        connection.close()


# TCP Server
# bind_ip = "0.0.0.0"
# bind_port = 9999

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#
#
# server.bind((bind_ip, bind_port))
#
# server.listen(5)
#
# print(f"[*] Listening on {bind_ip}:{bind_port}")
#
#
# # this is our client-handling thread
# def handle_client(client_socket):
#     # print out what the client sends
#     request = client_socket.recv(1024)
#     print(f"[*] Received: {request}")
#
#     # send back a packet
#     client_socket.send("ACK!")
#     client_socket.close()
#
#
# while True:
#     client, addr = server.accept()
#     print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")
#
#     # spin up client to handle incoming data
#     client_handler = threading.Thread(target=handle_client, args=(client,))
#     client_handler.start()

