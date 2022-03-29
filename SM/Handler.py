from SM.Machine import Machine


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]



class Handler(metaclass=SingletonMeta):
    __machine_list = dict()
    __initial_machine = None

    def add_machine(self, name, initial=False):
        machine = Machine()
        self.__machine_list[name] = machine
        if initial:
            self.__initial_machine = name
        return machine

    def run(self, name=False):
        if not name:
            return self.__machine_list[self.__initial_machine].run()
        else:
            return self.__machine_list[name].run()
