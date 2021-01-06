import sys
from task2 import *
from itertools import product

def union(nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states,nO_states1,states1,alphabet_size1,alphabet1,transition_function1,start_state1,nO_final_states1,final_states1):
	#works out the union of 2 DFA's, very similar to intersection just changes final states.
	new_states = list(product(states,states1))

	new_nO_states = len(new_states)

	new_start_state = start_state+start_state1

	new_final_states = []
	j = 0
	for j in range(new_nO_states):
		if new_states[j][0] in final_states or new_states[j][1] in final_states1:
			new_final_states.append(''.join(new_states[j]))

	new_nO_final_states = len(new_final_states)

	i=0
	for i in range(new_nO_states):
		new_states[i] = ''.join(new_states[i])

	k = 0
	l = 0
	new_transition_function = []
	for i in range(len(transition_function)):
		for j in range(len(transition_function1)):
			if transition_function[i][1] == transition_function1[j][1]:
				new_transition_function.append([str(transition_function[i][0])+str(transition_function1[j][0]),transition_function[i][1],str(transition_function[i][2])+str(transition_function1[j][2])])

	return new_nO_states,new_states,alphabet_size,alphabet,new_transition_function,new_start_state,new_nO_final_states,new_final_states

def symmetric_difference(nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states,nO_states1,states1,alphabet_size1,alphabet1,transition_function1,start_state1,nO_final_states1,final_states1):
	#works out the symmetirc_difference of 2 DFA's using Comlementaion, intersection and union.
	nO_states_comp,states_comp,alphabet_size_comp,alphabet_comp,transition_function_comp,start_state_comp,nO_final_states_comp,final_states_comp = complementation(nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states)
	nO_states_comp1,states_comp1,alphabet_size_comp1,alphabet_comp1,transition_function_comp1,start_state_comp1,nO_final_states_comp1,final_states_comp1 = complementation(nO_states1,states1,alphabet_size1,alphabet1,transition_function1,start_state1,nO_final_states1,final_states1)
	nO_states_inter,states_inter,alphabet_size_inter,alphabet_inter,transition_function_inter,start_state_inter,nO_final_states_inter,final_states_inter = intersection(nO_states_comp,states_comp,alphabet_size_comp,alphabet_comp,transition_function_comp,start_state_comp,nO_final_states_comp,final_states_comp,nO_states1,states1,alphabet_size1,alphabet1,transition_function1,start_state1,nO_final_states1,final_states1)
	nO_states_inter1,states_inter1,alphabet_size_inter1,alphabet_inter1,transition_function_inter1,start_state_inter1,nO_final_states_inter1,final_states_inter1 = intersection(nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states,nO_states_comp1,states_comp1,alphabet_size_comp1,alphabet_comp1,transition_function_comp1,start_state_comp1,nO_final_states_comp1,final_states_comp1)
	nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states = union(nO_states_inter,states_inter,alphabet_size_inter,alphabet_inter,transition_function_inter,start_state_inter,nO_final_states_inter,final_states_inter,nO_states_inter1,states_inter1,alphabet_size_inter1,alphabet_inter1,transition_function_inter1,start_state_inter1,nO_final_states_inter1,final_states_inter1)
	return nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states


if __name__ == "__main__":
	DFA = sys.argv[1]
	DFA1 = sys.argv[2]
	nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states = readFile(DFA)
	nO_states1,states1,alphabet_size1,alphabet1,transition_function1,start_state1,nO_final_states1,final_states1 = readFile(DFA1)

	nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states = symmetric_difference(nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states,nO_states1,states1,alphabet_size1,alphabet1,transition_function1,start_state1,nO_final_states1,final_states1)
	printDFA(nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states)

