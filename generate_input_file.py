import csv
from random import randint, choice


input_count = 100
count = 0

with open("input.csv", "w") as outf:
    outfile = csv.writer(outf)
    while count != input_count:
        direction = choice(['inbound', 'outbound'])
        protocol = choice(['tcp', 'udp'])

        type_port = randint(1, 2)
        if type_port == 1:
            port = str(randint(1, 65535))
        else:
            min_port = randint(1, 65530)
            max_port = randint(min_port + 1, 65535)
            port = str(min_port) + '-' + str(max_port)

        type_ip = randint(1, 2)
        if type_ip == 1:
            ip = str(randint(0, 255)) + '.' + str(randint(0, 255)) + '.' + str(randint(0, 255)) \
                 + '.' + str(randint(0, 255))
        else:
            ip1 = str(randint(0, 255)) + '.' + str(randint(0, 255)) + '.' + str(randint(0, 255)) \
                  + '.' + str(randint(0, 255))
            ip2 = str(randint(0, 255)) + '.' + str(randint(0, 255)) + '.' + str(randint(0, 255)) \
                  + '.' + str(randint(0, 255))
            ip = ip1 + '-' + ip2

        outfile.writerow((direction, protocol, port, ip))
        count += 1

