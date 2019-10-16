import csv
from random import choice, randint


input_count = 10000
count = 0

with open("test_case.csv", "w") as outf:
    outfile = csv.writer(outf)
    while count != input_count:
        direction = choice(['inbound', 'outbound'])
        protocol = choice(['tcp', 'udp'])

        port = randint(1, 65535)

        ip = str(randint(0, 255)) + '.' + str(randint(0, 255)) + '.' + str(randint(0, 255)) \
                 + '.' + str(randint(0, 255))

        outfile.writerow((direction, protocol, port, ip))
        count += 1
