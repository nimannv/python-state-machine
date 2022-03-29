from setuptools import Command
from SM.Handler import Handler
from SM import Machine


def first(machine:Machine):
    command = input("This is first machine state1 \n enter x:")
    if command=='1':
        machine.goto('second')
    elif command=='2':
        machine.goto('third')

def second(machine:Machine):
    print('This is first machine state2')
    Handler().run('second_machine')
    machine.goto('third')

def third(machine:Machine):
    print('This is first machine state3')


def second_machine_first(machine:Machine):
    print('This is second machine state 1')
    machine.goto('second')

def second_machine_second(machine:Machine):
    print('This is second machine state 2')
    machine.goto('third')

def second_machine_third(machine:Machine):
    print('This is second machine state 3')

