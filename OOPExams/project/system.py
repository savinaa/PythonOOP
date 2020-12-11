from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System():
    _hardware=[]
    _software=[]

    @staticmethod
    def register_power_hardware(name:str, capacity:int, memory:int):
        pow_hard=PowerHardware(name,capacity,memory)
        System._hardware.append(pow_hard)

    @staticmethod
    def register_heavy_hardware( name: str, capacity: int, memory: int):
        heavy_hard = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hard)

    @staticmethod
    def register_express_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        for h in System._hardware:
            if h.name==hardware_name:
                exp_soft=ExpressSoftware(name,capacity_consumption,memory_consumption)
                try:
                    h.install(exp_soft)
                    System._software.append(exp_soft)
                    break
                except Exception as e:
                    return str(e)
        else:
            return f"Hardware does not exist"


    @staticmethod
    def register_light_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        for h in System._hardware:
            if h.name==hardware_name:
                light_soft=LightSoftware(name,capacity_consumption,memory_consumption)
                try:
                    h.install(light_soft)
                    System._software.append(light_soft)
                    break
                except Exception as e:
                    return str(e)
        else:
            return f"Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        searched_hardware = [h for h in System._hardware if h.name == hardware_name]
        searched_software = [s for s in System._software if s.name == software_name]
        if (not searched_hardware) or (not searched_software):
            return "Some of the components do not exist"
        hardware = searched_hardware[0]
        software = searched_software[0]
        hardware.uninstall(software)
        System._software.remove(software)  # !!!!!!!!!!!!

    @staticmethod
    def analyze():
        total_used_memory=0
        for h in System._hardware:
            for s in h.software_components:
                total_used_memory+=s.memory_consumption
        total_memory=sum( [h.memory for h in System._hardware])
        total_used_space = 0
        for h in System._hardware:
            for s in h.software_components:
                total_used_space+=s.capacity_consumption
        total_capacity= sum([h.capacity for h in System._hardware])
        output=f"System Analysis\nHardware Components: {len(System._hardware)}\nSoftware Components: {len(System._software)}\nTotal Operational Memory: {int(total_used_memory)} / {int(total_memory)}\nTotal Capacity Taken: {int(total_used_space)} / {int(total_capacity)}"
        return output



    @staticmethod
    def system_split():
        output=""
        for h in __class__._hardware:
            output+=f'{h.__str__()}'
        return output

