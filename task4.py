import sys
from task3 import *

def dfs(visited_nodes, graph, node, final_states, word):
	#a depth first search recursive algorithm
	if node not in visited_nodes:
		visited_nodes.add(node)
		for i in graph[node]:
			word = word+i[0]
			if i[1] not in final_states:
				dfs(visited_nodes, graph, i[1], final_states, word)
			else:
				return word
	return False


def non_empty(nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states):
	#reformating the transition function into a dictionary
	nodes = {}
	i = 0
	for i in transition_function:
		if i[0] not in nodes:
			nodes[i[0]] = [[i[1],i[2]]]
		else:
			nodes[i[0]].append([i[1],i[2]])
	#works out the result of the DFS
	visited_nodes = set()
	word = ''
	#checks to see if the empty string is accepted
	if start_state in final_states:
		return 'language non-empty - e accepted'
	else:
		result = dfs(visited_nodes, nodes, start_state, final_states, word)

	if result == False:
		return 'language empty'
	else:
		return 'language non-empty - '+word+' accepted'


if __name__ == '__main__':
	DFA = sys.argv[1]
	nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states = readFile(DFA)
	print(non_empty(nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states))

