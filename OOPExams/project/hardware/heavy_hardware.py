from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super(HeavyHardware, self).__init__(name, "Heavy",capacity*2,memory*0.75)