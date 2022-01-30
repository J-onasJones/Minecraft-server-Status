from mcstatus import MinecraftServer
from time import sleep

ip = input("Please Enter server IP: ")
port = input("Enter Port (press enter for default port 25565): ")

if port == "":
    port = "25565"

server = MinecraftServer.lookup(ip + ":" + port)


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
