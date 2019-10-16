import csv


class Firewall:

    def __init__(self, file):
        # create input dictionary
        self.input_data = {"inbound": {}, "outbound": {}}
        self.input_data["inbound"]["tcp"] = {}
        self.input_data["inbound"]["udp"] = {}
        self.input_data["outbound"]["tcp"] = {}
        self.input_data["outbound"]["udp"] = {}

        # read the data
        with open(file) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                direction, protocol, port, ip = row
                all_valid_ports = self.input_data[direction][protocol]
                # append ip address to port if already exists else create one
                if port in all_valid_ports:
                    self.input_data[direction][protocol][port] += [ip]
                else:
                    self.input_data[direction][protocol][port] = [ip]

    # check if packet should be accepted or not.
    def accept_packet(self, input_direction, input_protocol, input_port, input_ip):
        port = self.input_data[input_direction][input_protocol]
        for current_ports, current_ips in port.items():
            if self.validate_port(input_port, current_ports):
                for ip in current_ips:
                    if self.validate_ip(input_ip, ip):
                        return True
        return False

    # check if port is accepted or not
    def validate_port(self, port_value, firewall_port):
        # find '-' to check whether input is range or not
        hyphen_index = firewall_port.find("-")
        # 'find' returns index of '-' if present else returns -1

        # check value of hyphen_index
        if hyphen_index == -1:  # means '-' not present i.e. single valued
            return port_value == int(firewall_port)
        else:
            # splits range into lower and upper bound at hyphen index
            lower_bound = int(firewall_port[:hyphen_index])
            upper_bound = int(firewall_port[hyphen_index + 1:])
            return (upper_bound >= port_value) and (port_value >= lower_bound)

    # check if ip is accepted or not
    def validate_ip(self, ip_value, firewall_ip):
        # find '-' to check whether input is range or not
        hyphen_index = firewall_ip.find("-")
        # 'find' returns index of '-' if present else returns -1

        # check value of hyphen_index
        if hyphen_index == -1:  # means '-' not present i.e. single valued
            return ip_value == firewall_ip
        else:
            # splits range into lower and upper bound at hyphen index
            lower_bound = int(firewall_ip[:hyphen_index].replace(".", ""))
            upper_bound = int(firewall_ip[hyphen_index + 1:].replace(".", ""))
            ip_value = int(ip_value.replace(".", ""))
            return (upper_bound >= ip_value) and (ip_value >= lower_bound)
