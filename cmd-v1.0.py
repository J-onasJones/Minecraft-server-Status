from mcstatus import JavaServer
from time import sleep

ip = input("Please Enter server IP: ")
port = input("Enter Port (press enter for default port 25565, enter * if unknown): ")
delay = input("How many seconds do you want in between status updates?: ")

if delay == "":
    delay = "0"

delay_int = int(delay)

if port == "":
    port = "25565"

if port == "*":
    server = JavaServer.lookup(ip)
else:
    server = JavaServer.lookup(ip + ":" + port)


if port == "*":
    while True:
        status = server.status()
        query = server.query()
        ping = server.ping()
        print("---------- " + ip + ":" + f"{query.raw['hostport']}" + " ----------")
        print(f"Version: v{status.version.name} (protocol {status.version.protocol})")
        print(f'Description: "{status.description}"')

        print(f"Host: {query.raw['hostip']}:{query.raw['hostport']}")
        print(f"Software: v{query.software.version} {query.software.brand}")
        print(f"Plugins: {query.software.plugins}")
        print(f"Ping: {ping} ms")
        print(f"Players: {status.players.online}/{status.players.max}")
        print(f"Players Online: {query.players.names}")
        print("\n")
        sleep(delay_int)

if port != "*":
    while True:
        status = server.status()
        query = server.query()
        ping = server.ping()
        print("---------- " + ip + ":" + port + " ----------")
        print(f"Version: v{status.version.name} (protocol {status.version.protocol})")
        print(f'Description: "{status.description}"')

        print(f"Host: {query.raw['hostip']}:{query.raw['hostport']}")
        print(f"Software: v{query.software.version} {query.software.brand}")
        print(f"Plugins: {query.software.plugins}")
        print(f"Ping: {ping} ms")
        print(f"Players: {status.players.online}/{status.players.max}")
        print(f"Players Online: {query.players.names}")
        print("\n")
        sleep(delay_int)

