
import sys
import heapq

#import utils
sys.setrecursionlimit(10000)


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
		if state +1 <= self.N:
			result.append (( 'walk', state +1, self.weights['walk']))
		if state*2 <= self.N:
			result.append(('tram', state*2, self.weights['tram']))
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
# space complexity is O(D)
# worst case O(B^D)

#BFS , cost is the same on all the edges, Complexity is O(b^d)

#dynamic programming - cache[state] stores the results of sub trees
#cannot have cycles, as the orfer of finding futurecost(s) has to be known
def dynamicProgramming(problem):
	cache = {} # state->futureCost(state), action, newState, Cost
	def futureCost(state):
		# base case
		if problem.isEnd(state):
			return 0
		if state in cache:
			return cache[state][0]
		result = min((cost +futureCost(newState), action, newState, cost)\
				 for action, newState, cost in problem.succAndCost(state))
		cache[state] = result
		return result[0]

	state = problem.startState()
	totalCost = futureCost(state)

	history = []
	while not problem.isEnd(state):
		futurcost, action, newState, cost = cache[state]
		history.append((action, newState, cost))
		state = newState

	return (futureCost(problem.startState()), history)

def predict(N, weights):
	#f(x)
	#input (x): N (number of blocks)
	# output (y) : path (sequence of actions)
	Problem = TransportationProblem(N, weights)
	totalCost, history = dynamicProgramming(Problem)
	return [action for action, newState, cost in history]

def generateExamples():
	trueWeights = {'walk':1, 'tram':2}
	return [(N, predict(N, trueWeights)) for N in range(1,10)]


def structuredPerceptron(examples):
	weights = {'walk':0, 'tram':0}
	for t in range(100):
		numMistakes =0
		for N, trueActions in examples:
			#Make a prediction
			predActions = predict(N, weights)
			if predActions != trueActions:
				numMistakes +=1
			#update weights
			for action in trueActions:
				weights[action] -= 1
			for action in predActions:
				weights[action] +=1
		print('Iteration {}. numMistakes= {}, weights={}'.format(t, numMistakes, weights))
		if numMistakes == 0:
			break

class PriorityQueue:
	def __init__(self):
		self.DONE = -1000000
		self.heap = []
		self.priorities = {} #MAP from state to priority
	# Insert |state| into the heap with priority |newPriority| if
	# |state| isn't in the heap or |newPriority| is smaller than the existing
	# priority
	# Return whether priority queue was update
	def update(self, state, newPriority):
		oldPriority = self.priorities.get(state)
		if oldPriority == None or newPriority < oldPriority:
			self.priorities[state] = newPriority
			heapq.heappush(self.heap, (newPriority, state))
			return True
		return False

	def removeMin(self):
		while len(self.heap)>0:
			priority, state = heapq.heappop(self.heap)
			if self.priorities[state]== self.DONE: continue #Outdated priority, skip
			self.priorities[state]=self.DONE
			return (state, priority)
		return (None, None)


def uniformCostSearch(problem):
	frontier = PriorityQueue()
	frontier.update(problem.startState(),0)
	while True:
		#move from frontieir to explored
		state, pastCost = frontier.removeMin()
		if problem.isEnd(state):
			return (pastCost, [])

		for action, newState, cost in problem.succAndCost(state):
			frontier.update(newState, pastCost + cost)



#problem = TransportationProblem(N=456)
#print(problem.succAndCost(3))
#print(problem.succAndCost(9))0
#printSolution(backTrackingSearch(problem))
#print('Dynamic Programming')
#printSolution(dynamicProgramming(problem))
#print('Uniform Cost Search')
#printSolution(uniformCostSearch(problem))

examples = generateExamples()
print('Training datsaset :')

for example in examples:
	print(' ', example)

structuredPerceptron(examples)

