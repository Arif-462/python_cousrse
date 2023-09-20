# inheritance vs composition

class CPU:
    def __init__(self, core) -> None:
        self.core = core


class RAM:
    def __init__(self, size) -> None:
        self.size = size

class HardDrive:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        # print(f'the sise {capacity}')


# computer has a cpu
# computer has a ram
# computer has a hard drive

class Computer:
    def __init__(self, core, ram_size, hd_capacity) -> None:
        self.cpu = CPU(core)
        self.ram = RAM(ram_size)
        self.hard_disc = HardDrive(hd_capacity)

mac = Computer(8, 16, 512)
print(mac.cpu)