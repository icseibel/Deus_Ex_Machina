#!/usr/bin/env python3
from numpy import array
import random

class DeusExMachina():
    """
      FSM - Finite State Machine
      | Actual state  | Input   | Next state |
      |---------------|---------|------------|
      | stopped       | start   | started    |
      | started       | collect | collecting |
      | started       | stop    | stopped    |
      | collecting    | process | processing |
      | collecting    | stop    | stopped    |
      | processing    | stop    | stopped    |
    """
    statusDict = {'start' : 'started', 'stop' : 'stopped', 'collect' : 'collecting', 'process' : 'processing'}

    def __init__(self):
        self.current_state = 'stopped'
        self.previous_state = ''
        self.matrix = array([[[0,0,0],[0,0,0],[0,0,0]]])

#getPreviousState, getCurrentState and setCurrentState.    
    def getPreviousState(self):
        return self.previous_state

    def getCurrentState(self):
        return self.current_state

    def setCurrentState(self, newinput):
        try:
          newstate = DeusExMachina.statusDict[newinput]
        except:
            print('Please enter a valid Input!')
            return
        if self.current_state == newstate:
            print('Machine is already in state:'+self.current_state)
        elif self.current_state == 'stopped' and newstate != 'started':
            print('The machine is stopped you need to start it first!')
        elif self.current_state == 'started' and newstate not in ('collecting','stopped'):
            print('Invalid Input is started. Valid inputs are collect and stop at this moment!')
        elif self.current_state == 'collecting' and newstate not in ('processing','stopped'):
            print('The machine is currently collecting...valid inputs at this moment are stop or process')
        elif self.current_state == 'processing' and newstate != 'stopped':
            print('Machine is processing...The valid input at this moment is stop')
        else:
            self.previous_state = self.current_state
            self.current_state = newstate
            self.processCurrentState()

    #collectData and processData
    def collectData(self):
        self.matrix = array([[random.randint(0,9),random.randint(0,9),random.randint(0,9)],[random.randint(0,9),random.randint(0,9),random.randint(0,9)],[random.randint(0,9),random.randint(0,9),random.randint(0,9)]])
        return self.matrix

    def processData(self):
        self.matrix = array(self.matrix, dtype=int)*5
        self.matrix = self.matrix.transpose()
        print('transposed matrix multiplied by scalar 5!')
        print(self.matrix)
    
    def processCurrentState(self):
        if self.current_state == 'collecting':
            matrix = self.collectData()
            print('original matrix collected:')
            print(matrix)
            self.setCurrentState('process')
        elif self.current_state == 'processing':
            self.processData()
            self.previous_state = self.current_state
            self.current_state = 'collecting'
        else:
            pass

print('Welcome to DeusExMachina!')    
machine = DeusExMachina()
while True:
    print('\nCurrent sate of DeusExMachina is:'+machine.getCurrentState())
    newinput = input('Please give the proper input: ')
    if newinput == 'exit':
        machine.setCurrentState('stop')
        break
    else:
        machine.setCurrentState(newinput)
