class Software:
    def __init__(self, name, type, capacity_consumption, memory_consumption):
        self._name = name
        self._type = type
        self._capacity_consumption = capacity_consumption
        self._memory_consumption = memory_consumption

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name=value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type=value

    @property
    def capacity_consumption(self):
        return self._capacity_consumption

    @capacity_consumption.setter
    def capacity_consumption(self, value):
        self._capacity_consumption=value

    @property
    def memory_consumption(self):
        return self._memory_consumption

    @memory_consumption.setter
    def memory_consumption(self, value):
        self._memory_consumption=value
