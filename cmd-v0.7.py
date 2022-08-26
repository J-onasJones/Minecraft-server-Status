from mcstatus import JavaServer
from time import sleep

ip = input("Please Enter server IP: ")
port = input("Enter Port (press enter for default port 25565, enter 0 if unknown): ")
delay = input("How many seconds do you want in between status updates?: ")

if delay == "":
    delay_int = 0

delay_int = int(delay)

if port == "":
    port = "25565"

if port == "0":
    server = JavaServer.lookup(ip)
else:
    server = JavaServer.lookup(ip + ":" + port)

if port == "0":
    while True:
        status = server.status()
        query = server.query()
        ping = server.ping()
        print("---------- " + ip + " ----------")
        print(f"version: v{status.version.name} (protocol {status.version.protocol})")
        print(f'description: "{status.description}"')

        print(f"host: {query.raw['hostip']}:{query.raw['hostport']}")
        print(f"software: v{query.software.version} {query.software.brand}")
        print(f"plugins: {query.software.plugins}")
        print(f"ping: {ping} ms")
        print(f"players: {status.players.online}/{status.players.max}")
        print(f"Players Online: {query.players.names}")
        print("\n")
        sleep(delay_int)

if port != "0":
    while True:
        status = server.status()
        query = server.query()
        ping = server.ping()
        print("---------- " + ip + ":" + port + " ----------")
        print(f"version: v{status.version.name} (protocol {status.version.protocol})")
        print(f'description: "{status.description}"')

        print(f"host: {query.raw['hostip']}:{query.raw['hostport']}")
        print(f"software: v{query.software.version} {query.software.brand}")
        print(f"plugins: {query.software.plugins}")
        print(f"ping: {ping} ms")
        print(f"players: {status.players.online}/{status.players.max}")
        print(f"Players Online: {query.players.names}")
        print("\n")
        sleep(delay_int)
