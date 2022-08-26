from mcstatus import JavaServer
from time import sleep

ip = input("Please Enter server IP: ")

    server = JavaServer.lookup(ip)

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
        sleep(5)
