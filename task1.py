import sys
def readFile(DFA):
	#sets up list variables
	states, alphabet, transition_function, final_states = [],[],[],[]
	#open the file to read it
	file = open(DFA,"r")
	all_lines = file.readlines()
	#work out number of states
	nO_states = int(all_lines[0])
	#adds all the states to a lsit
	i = 0
	for i in range(nO_states):
		states.append(all_lines[1][i*2])
	#records alphabet size
	alphabet_size = int(all_lines[2])
	#adds the alphabet to a list
	j = 0
	for j in range(alphabet_size):
		alphabet.append(all_lines[3][j*2])
	#records the transition functions
	k = 0
	l = 0
	for k in range(nO_states):
		for l in range(alphabet_size):
			if all_lines[4+k][l*2] != ' ':
				transition_function.append([states[k],alphabet[l],all_lines[4+k][l*2]])
	#records the start state	
	start_state = (all_lines[4+nO_states]).rstrip('\n')
	#records the number of final states
	nO_final_states = int(all_lines[5+nO_states])
	#records the final states to a list
	m = 0
	for m in range(nO_final_states):
		final_states.append(all_lines[6+nO_states][m*2])
	return nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states

def printDFA(nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states):
	#formats and prints a DFA to screen
	print(nO_states)
	print(*states)
	print(alphabet_size)
	print(*alphabet)

	i = 0
	j = 0
	k = 0
	#prints out the modified way I stored transition functions 
	for i in range(nO_states):
		temp_string = ' '
		for j in range(alphabet_size):
			check = False
			for k in range(len(transition_function)):
				if transition_function[k][0] == states[i] and transition_function[k][1] == alphabet[j]:
					check = True
					if j == 0:
						temp_string = str(transition_function[k][2])
					else:
						temp_string = temp_string + ' ' + str(transition_function[k][2])
			if check == False and j != 0:
				temp_string = temp_string + '   '
		print(temp_string)

	print(start_state)
	print(nO_final_states)
	print(*final_states)


def complementation(nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states):
	#works out the complement of a DFA
	final_states = list(set(states) - set(final_states))
	nO_final_states = len(final_states)
	return nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states	

if __name__ == '__main__':
	DFA = sys.argv[1]
	nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states = readFile(DFA)
	nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states = complementation(nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states)
	printDFA(nO_states,states,alphabet_size,alphabet,transition_function,start_state,nO_final_states,final_states)







