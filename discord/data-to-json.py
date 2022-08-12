import json, sys
datas = open(sys.argv[1], "r").read().splitlines()

idk = json.dumps([{"email": i.split(":")[0], "password": i.split(":")[1], "username": i.split(":")[2], "token": i.split(":")[3]} for i in datas], indent=4)

u = open(f'{sys.argv[1].split(".")[0]}.json', 'w')
u.write("".join(idk))
u.close()
