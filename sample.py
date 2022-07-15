#modeling the problem
class TransportationProblem(object):
	def __init__(self, N, weights):
		# N = number of blocks
		# weights = weights of different actions
		self.N =N
		self.weights = weights
	def startState(self):
		return 1 
	def isEnd(self, state):
		return state == self.N 
	def succAndCost(self, state):
		#retrun list of (action, newState, Cost) triples
		result = []
		if state +1 <=self.N:
			result.append (( 'walk', state +1, self.weights['walk']))
		if state*2<=self.N:
			result.append(('tram', state*2, self.weights['tram']))
		return result


cache={'walk', }