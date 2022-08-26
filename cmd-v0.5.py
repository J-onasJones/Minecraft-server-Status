from mcstatus import JavaServer
from time import sleep

ip = input("Please Enter server IP: ")
port = input("Enter Port (press enter for default port 25565, enter 0 if unknown): ")

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
        print("---------- " + ip + " ----------")
        print(f"version: v{status.version.name} (protocol {status.version.protocol})")
        print(f'description: "{status.description}"')

        print(f"host: {query.raw['hostip']}:{query.raw['hostport']}")
        print(f"software: v{query.software.version} {query.software.brand}")
        print(f"plugins: {query.software.plugins}")
        print(f"players: {status.players.online}/{status.players.max}")
        print(f"Players Online: {query.players.names}")
        print("\n")
        wait(3)

if port != "0":
    while True:
        status = server.status()
        query = server.query()
        print("---------- " + ip + ":" + port + " ----------")
        print(f"version: v{status.version.name} (protocol {status.version.protocol})")
        print(f'description: "{status.description}"')

        print(f"host: {query.raw['hostip']}:{query.raw['hostport']}")
        print(f"software: v{query.software.version} {query.software.brand}")
        print(f"plugins: {query.software.plugins}")
        print(f"players: {status.players.online}/{status.players.max}")
        print(f"Players Online: {query.players.names}")
        print("\n")
        wait(3)
