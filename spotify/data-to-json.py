import json, sys

u = open(f'{sys.argv[1].split(".")[0]}.json', 'w')
u.write("".join(json.dumps([{"nickname": i.split(":")[0], "username": i.split(":")[1], "email": i.split(":")[2], "password": i.split(":")[3]} for i in open(sys.argv[1], "r").read().splitlines()], indent=4)))
u.close()
