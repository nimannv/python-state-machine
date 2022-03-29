from SM.Handler import Handler
import SM.jobs as jobs



first_machine = Handler().add_machine('first_machine', initial=True)

first_machine.add_state('first', jobs.first, initial=True)
first_machine.add_state('second', jobs.second)
first_machine.add_state('third', jobs.third)

second_machine = Handler().add_machine('second_machine')
second_machine.add_state('first', jobs.second_machine_first, initial=True)
second_machine.add_state('second', jobs.second_machine_second)
second_machine.add_state('third', jobs.second_machine_third)

Handler().run()