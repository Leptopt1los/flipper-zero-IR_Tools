from config import RAW_DATA_COMPARSION_LIMIT

class IR_Signal:
    def __init__(self, name=None, type=None, protocol=None, address=None, command=None, frequency=None, duty_cycle=None, data=None):
        self.name = None
        self.type = None
        self.protocol = None
        self.address = None
        self.command = None
        self.frequency = None
        self.duty_cycle = None
        self.data = None

        if name is not None:
            self.set_name(name)
        if type is not None:
            self.set_type(type)
        if protocol is not None:
            self.set_protocol(protocol)
        if address is not None:
            self.set_address(address)
        if command is not None:
            self.set_command(command)
        if frequency is not None:
            self.set_frequency(frequency)
        if duty_cycle is not None:
            self.set_duty_cycle(duty_cycle)
        if data is not None:
            self.set_data(data)

    def set_name(self, value):
        self.name = value

    def set_type(self, value):
        if value in ["raw", "parsed"]:
            self.type = value
        else:
            raise ValueError("Invalid type format")

    def set_protocol(self, value):
        self.protocol = value

    def set_address(self, value):
        self.address = int(value, 16)

    def set_command(self, value):
        self.command = int(value, 16)

    def set_frequency(self, value):
        self.frequency = int(value)

    def set_duty_cycle(self, value):
        self.duty_cycle = float(value)

    def set_data(self, value):
        self.data = [int(val) for val in value]

    def get_str_number(self):
        return self.str_number

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_protocol(self):
        return self.protocol

    def get_address(self):
        return self.address

    def get_command(self):
        return self.command

    def get_frequency(self):
        return self.frequency

    def get_duty_cycle(self):
        return self.duty_cycle

    def get_data(self):
        return self.data

    def compare_data(self, other_data):
        if len(self.data) != len(other_data):
            return False

        for i in range(len(self.data)):
            if abs(self.data[i] - other_data[i]) > RAW_DATA_COMPARSION_LIMIT:
                return False

        return True

    def __str__(self):
        protocol = "" if self.get_protocol() is None else "Protocol: "+str(self.get_protocol())+"\n"
        address = "" if self.get_address() is None else "Address: "+str(self.get_address())+"\n"
        command = "" if self.get_command() is None else "Command: "+str(self.get_command())+"\n"
        frequency = "" if self.get_frequency() is None else "Frequency: "+str(self.get_frequency())+"\n"
        duty_cycle = "" if self.get_duty_cycle is None else "Duty_cycle: "+str(self.get_duty_cycle())+"\n"
        data = "" if self.get_data() is None else "Data: "+str(self.get_data())+"\n"

        return f"Name: {self.name}\nType: {self.type}\n{protocol}{address}{command}{frequency}{duty_cycle}{data}"

def parse_ir_file(file_path):
    signals = []
    current_signal = IR_Signal()

    with open(file_path, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            parts = stripped_line.split(":")

            if len(parts) == 2:
                key, value = parts[0].strip(), parts[1].strip()
                if key == "name":
                    if current_signal.get_name() is not None:
                        signals.append(current_signal)
                        current_signal = IR_Signal()
                    current_signal.set_name(value)
                elif key == "type":
                    current_signal.set_type(value)
                elif key == "frequency":
                    current_signal.set_frequency(value)
                elif key == "duty_cycle":
                    current_signal.set_duty_cycle(value)
                elif key == "data":
                    current_signal.set_data(value.split())
                elif key == "protocol":
                    current_signal.set_protocol(value)
                elif key == "address":
                    current_signal.set_address(value)
                elif key == "command":
                    current_signal.set_command(value)

        signals.append(current_signal)

    return signals