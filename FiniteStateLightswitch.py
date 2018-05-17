#Laura Davis 26 June 2017

#Lesson and source code from YouTube user Trevor Payne
#This program demonstrates a finite-state machine (FSM) which is often
#used in AI. Its purpose is to organize and structuralize program logic
#for use in AI and in conjunction with machine learning algorithms.
#Typical construction follows this order:
#1.States 2.Transitions 3.FSM 4.Character class 5.Main code 

from random import randint
from time import clock

##===================================================================
#Name states

State = type("State", (object,), {})

class LightOn(State):
	def Execute(self):
		print "Light is ON"
		
class LightOff(State):
	def Execute(self):
		print "Light is OFF"
		
##===================================================================
#Ties constructors to states and initiates

class Transition(object):
	def __init__(self, toState):
		self.toState = toState
		
	def Execute(self):
		print "Transitioning..."
		
##===================================================================
#The main code for the FSM

class SimpleFSM(object):
	def __init__(self, char):
		self.char = char
		self.states = {}
		self.transitions = {}
		self.curState = None
		self.trans = None
		
	def SetState(self, stateName):
		self.curState = self.states[stateName]
		
	def Transition(self, transName):
		self.trans = self.transitions[transName]
		
	def Execute(self):
		if (self.trans):
			self.trans.Execute()
			self.SetState(self.trans.toState)
			self.trans = None
		self.curState.Execute()
		
##===================================================================

#Creation of FSM instance
class Char(object):
	def __init__(self):
		self.FSM = SimpleFSM(self)
		self.LightOn = True

##===================================================================

#The meat of the program

if __name__=="__main__":
	light = Char()
	
	light.FSM.states["On"] = LightOn()
	light.FSM.states["Off"] = LightOff()
	light.FSM.transitions["toOn"] = Transition("On")
	light.FSM.transitions["toOff"] = Transition("Off")
	
	light.FSM.SetState("On")
	
	for i in range(20):
		startTime = clock()
		timeInterval = 1
		while (startTime + timeInterval > clock()):
			pass
		if (randint(0, 2)):
			if (light.LightOn):
				light.FSM.Transition("toOff")
				light.LightOn = False
			else:
				light.FSM.Transition("toOn")
				light.LightOn = True
		
		light.FSM.Execute()
