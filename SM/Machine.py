class Machine:
    
    def __init__(self, handler):
        self.__state_list = dict()
        self.__initial_state = None
        self.__handler = handler

    def add_state(self, name, job, initial=False):
        if not name in self.__state_list:
            self.__state_list[name] = job
        if initial:
            self.__initial_state = name

    def run(self):
        if self.__initial_state == None:
            print("Initial state doesn't specified !")
        else:
            job = self.__state_list[self.__initial_state]
            return job(self, self.__handler)
    
    def goto(self, name):
        job = self.__state_list[name]
        return job(self, self.__handler)

