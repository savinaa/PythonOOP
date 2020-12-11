from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class Hardware:
    def __init__(self, name, type, capacity, memory):
        self._name = name
        self._type = type
        self._capacity = capacity
        self._memory = memory
        self._software_components=[]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value

    @property
    def memory(self):
        return self._memory

    @memory.setter
    def memory(self, value):
        self._memory = value

    @property
    def software_components(self):
        return self._software_components

    @software_components.setter
    def software_components(self, value):
        self._software_components=value

    def install(self, software:Software):
        if software.capacity_consumption<=self.capacity and software.memory_consumption<=self.memory:
            self.software_components.append(software)
            #self.capacity-=software.capacity_consumption
            #self.memory-=software.memory_consumption
        else:
            raise Exception('Software cannot be installed')

    def uninstall(self,software:Software):
        self.software_components.remove(software)
       # self.capacity+=software.capacity_consumption
        #self.memory+=software.memory_consumption

    def __str__(self):
        exp_soft_count=0
        light_soft_count=0
        memory_usage=0
        capacity_usage=0
        text=""
        for s in self.software_components:
            if isinstance(s,ExpressSoftware):
                exp_soft_count+=1
            elif isinstance(s,LightSoftware):
                light_soft_count+=1
            memory_usage+=s.memory_consumption
            capacity_usage+=s.capacity_consumption
        if self.software_components:
            text+=', '.join([s.name for s in self.software_components])
        else:
            text+='None'


        output=''
        output+=f'Hardware Component - {self.name}\nExpress Software Components: {exp_soft_count}\n' \
                f'Light Software Components: {light_soft_count}\nMemory Usage: {int(memory_usage)} / {int(self.memory)}\n'\
                f'Capacity Usage: {int(capacity_usage )} / {int(self.capacity)}\nType: {self.type}\n' \
                f'Software Components: {text}'
        return output
