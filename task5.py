import sys
from task4 import *

def equivalence(nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states,nO_states1,states1,alphabet_size1,alphabet1,transition_function1,start_state1,nO_final_states1,final_states1):
	#works out the symmetric difference of two DFA's and then checks if it has an empty language.
	nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states = symmetric_difference(nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states,nO_states1,states1,alphabet_size1,alphabet1,transition_function1,start_state1,nO_final_states1,final_states1)
	result = non_empty(nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states)
	#shows if a language is equivalent or not
	if result == 'language empty':
		return 'not equivalent'
	else:
		return 'equivalent'

if __name__ == "__main__":
	DFA = sys.argv[1]
	DFA1 = sys.argv[2]
	nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states = readFile(DFA)
	nO_states1,states1,alphabet_size1,alphabet1,transition_function1,start_state1,nO_final_states1,final_states1 = readFile(DFA1)

	print(equivalence(nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states,nO_states1,states1,alphabet_size1,alphabet1,transition_function1,start_state1,nO_final_states1,final_states1))