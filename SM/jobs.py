from SM import Handler
from SM import Machine


def first(machine:Machine, handler:Handler):
    nima = input("This is first machine state1 \n enter x:")
    if nima=='1':
        machine.goto('second')
    elif nima=='2':
        machine.goto('third')

def second(machine:Machine, handler:Handler):
    print('This is first machine state2')
    handler.run('second_machine')
    machine.goto('third')

def third(machine:Machine, handler:Handler):
    print('This is first machine state3')


def second_machine_first(machine:Machine, handler:Handler):
    print('This is second machine state 1')
    machine.goto('second')

def second_machine_second(machine:Machine, handler:Handler):
    print('This is second machine state 2')
    machine.goto('third')

def second_machine_third(machine:Machine, handler:Handler):
    print('This is second machine state 3')

