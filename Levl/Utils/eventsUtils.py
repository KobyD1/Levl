import random


class utils():

    def __init__(self, pre_mac):
        self.pre_mac = pre_mac

# method for create  stream with random MAC exept the MAC in index = position
    def mac_stream_builder(self, mac, position, len):
        assert position < len, "Tested MAC define at lower position VS tested list length"
        mac_stream = []

        for i in range(len):

            if (i == position):
                mac_stream.append(mac)
                continue

            random_mac = self.random_mac_builder()
            mac_stream.append(random_mac)

        return mac_stream

# method for create MAC with random digits
    def random_mac_builder(self):
        random_mac = ""

        for i in range(6):
            hex_num = hex(random.randint(0, 255))[2:]
            if (len(hex_num) == 1):
                hex_num = hex_num + '0'

            hex_as_string = str(hex_num) + ":"
            random_mac = random_mac + hex_as_string

        random_mac = random_mac[:-1]
        return random_mac

    def validateHex(s):

        for ch in s:

            if ((ch < '0' or ch > '9') and
                    (ch < 'A' or ch > 'F')):
                print("No")
                return

# method for validate if MAC is valid
    def mac_validator(self, mac):
        assert len(mac) == 17, "Corrupted MAC address found - length is not as expected"
        assert mac.count(':'), "Corrupted MAC address found - invalid amount of ':' "

        mac = mac.replace(":", "")
        for index in range(0, len(mac)):
            digit = int(mac[index],16)   # casting from HEX to INT
            if (digit not in range(0, 15)):
                assert digit not in range(0, 15), "Corrupted MAC address found - not in range (0-15) digit "

#   method for validate if stream is valid

    def stream_validator(self, stream):
        for mac in stream:
            index = stream.index(mac)
            print('Try to analyze MAC at position# ', index, 'MAC = ', mac)

            if ((index % 10 == 0) & (index > 0)):
                assert mac != self.pre_mac, "MAC adress at multiple 10 position is not as expected"

            self.mac_validator(mac)
