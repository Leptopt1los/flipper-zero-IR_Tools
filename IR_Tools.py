from config import RAW_DATA_COMPARSION_LIMIT

class IR_Signal:
    def __init__(self, name:str=None, type:str=None, protocol:str=None, address:str=None, command:str=None, frequency:str=None, duty_cycle:str=None, data:list=None):
        self.__name__ = None
        self.__type__ = None
        self.__protocol__ = None
        self.__address__ = None
        self.__command__ = None
        self.__frequency__ = None
        self.__duty_cycle__ = None
        self.__data__ = None

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

    def set_name(self, value:str):
        self.__name__ = value

    def set_type(self, value:str):
        if value in ["raw", "parsed"]:
            self.__type__ = value
        else:
            raise ValueError("Invalid type format")

    def set_protocol(self, value:str):
        self.__protocol__ = value

    def set_address(self, value:str):
        self.__address__ = value

    def set_command(self, value:str):
        self.__command__ = value

    def set_frequency(self, value:str):
        self.__frequency__ = int(value)

    def set_duty_cycle(self, value:str):
        self.__duty_cycle__ = float(value)

    def set_data(self, value:list):
        self.__data__ = [int(val) for val in value]

    def get_name(self):
        return self.__name__

    def get_type(self):
        return self.__type__

    def get_protocol(self):
        return self.__protocol__

    def get_address(self):
        return self.__address__

    def get_command(self):
        return self.__command__

    def get_frequency(self):
        return self.__frequency__

    def get_duty_cycle(self):
        return self.__duty_cycle__

    def get_data(self):
        return self.__data__

    def compare_data(self, other_data) -> bool:
        if len(self.__data__) != len(other_data):
            return False

        for i in range(len(self.__data__)):
            if abs(self.__data__[i] - other_data[i]) > RAW_DATA_COMPARSION_LIMIT:
                return False

        return True
    
    def compare(self, other_signal:'IR_Signal') -> bool:
        if self.get_type() != other_signal.get_type():
            return False

        if self.get_type() == "raw":
            return self.compare_data(other_signal.get_data())
        else:
            return (self.get_protocol() == other_signal.get_protocol()) and (self.get_address() == other_signal.get_address()) and (self.get_command() == other_signal.get_command())

    def __str__(self):
        protocol = "" if self.get_protocol() is None else "protocol: "+str(self.get_protocol())+"\n"
        address = "" if self.get_address() is None else "address: "+str(self.get_address())+"\n"
        command = "" if self.get_command() is None else "command: "+str(self.get_command())+"\n"
        frequency = "" if self.get_frequency() is None else "frequency: "+str(self.get_frequency())+"\n"
        duty_cycle = "" if self.get_duty_cycle() is None else "duty_cycle: "+str(self.get_duty_cycle())+"\n"
        data = "" if self.get_data() is None else "data: "+str(self.get_data())+"\n"

        return f"Name: {self.__name__}\nType: {self.__type__}\n{protocol}{address}{command}{frequency}{duty_cycle}{data}"

def parse_ir_file(file_path:str) -> list:
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