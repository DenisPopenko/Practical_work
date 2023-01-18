server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for i, j in server_data.items():
    print(i + ':')
    for k in j.items():
        print('\t', *k)
        # или
    # for k, h in j.items():
    #     print("\t" + k + ": " + h)