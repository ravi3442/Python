
import sys
sys.setrecursionlimit(10000)

#modeling the problem
class TransportationProblem(object):
	def __init__(self, N):
		# N = number of blocks
		self.N =N
	def startState(self):
		return 1 
	def isEnd(self, state):
		return state == self.N 
	def succAndCost(self, state):
		#retrun list of (action, newState, Cost) triples
		result = []
		if state +1 <=self.N:
			result.append (( 'walk', state +1, 1))
		if state*2<=self.N:
			result.append(('tram', state*2, 2))
		return result

def printSolution(solution):
	totalCost, history = solution
	print('totalCost: {}'.format(totalCost))
	for item in history:
		print(item)

#Algorithm- going over all the possibilities - brute force
# if B is the branching factor and D is your depth, the overall complexity is O(B^D)
# space complexity is O(D)
def backTrackingSearch(problem):
	#dictionary - to keep track of the best solution so far
	best={
		'cost': float('+inf'),
		'history ': None
	}
	def recurse(state, history, totalCost):
		#At state, having undergone history accumulated and totalcost
		#Exploore the rest of the subtree under state
		if problem.isEnd(state):
			#update the best solution so far
			# TODO
			if totalCost<best['cost']:
				best['cost']= totalCost
				best['history'] = history
			return
		#recures on children if not
		for action, newState, cost in problem.succAndCost(state):
			recurse(newState, history+[(action, newState, cost)], totalCost + cost)
	recurse (problem.startState(), history=[], totalCost=0)
	return(best['cost'], best['history'])

# depth first search, cost of the edges has to be zero




problem = TransportationProblem(N=1000)
#print(problem.succAndCost(3))
#print(problem.succAndCost(9))
printSolution(backTrackingSearch(problem))

