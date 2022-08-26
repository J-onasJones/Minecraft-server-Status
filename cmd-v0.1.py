from mcstatus import JavaServer

# You can pass the same address you'd enter into the address field in minecraft into the 'lookup' function
from mcstatus import JavaServer

ip = input("Please Enter server IP: ")
port = input("Enter Port (press enter for default port 25565): ")

if port == "":
    port = "25565"

print(ip + ":" + port)

server = JavaServer.lookup(ip + ":" + port)


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
