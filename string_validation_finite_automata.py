def dfa(input, input_symbols, no_of_states, initial_state, accepting_states, transition_table):
    current_state = initial_state
    for symbol in input:
        if symbol not in input_symbols:
            return False
        current_state = transition_table[current_state][symbol]
        print(f"Current state: {current_state}")
    return current_state in accepting_states


# no_of_input_symbols = int(input("Enter the number of input symbols: "))
input_symbols = list(input("Enter the input symbols: "))
no_of_states = int(input("Enter the number of states: "))
initial_state = input("Enter the initial state: ")
no_of_accepting_states = int(input("Enter the number of accepting states: "))
accepting_states = list(input("Enter the accepting states: "))
#abbabab
transition_table = {
    '1': {'a': '2', 'b': '3'},
    '2': {'a': '1', 'b': '4'}, #final state
    '3': {'a': '4', 'b': '1'},
    '4': {'a': '3', 'b': '2'},
}
#0 followed by 11 only
transition_table = {
    'a': {'1': 'a', '0': 'b'},
    'b': {'1': 'c', '0': 'e'},
    'c': {'1': 'd', '0': 'e'},
    'd': {'1': 'd', '0': 'b'}, #final state
    'e': {'1': 'e', '0': 'e'},
}

#starts and ends with same character over abc
transition_table = {
    '1': {'a': '2', 'b': '3', 'c': '4'},
    '2': {'a': '5', 'b': '2', 'c': '2'},
    '3': {'a': '3', 'b': '6', 'c': '3'},
    '4': {'a': '4', 'b': '4', 'c': '7'},
    '5': {'a': '5', 'b': '2', 'c': '2'}, #final state
    '6': {'a': '3', 'b': '6', 'c': '3'}, #final state
    '7': {'a': '3', 'b': '3', 'c': '7'}, #final state
}
#start with lowercase also include digits(a-e and 0-3)
transition_table = {
    '1': {'a': '2', 'b': '2', 'c': '2', 'd': '2', 'e': '2', '0': '3', '1': '3', '2': '3', '3': '3'},
    '2': {'a': '2', 'b': '2', 'c': '2', 'd': '2', 'e': '2', '0': '2', '1': '2', '2': '2', '3': '2'}, #final state
    '3': {'a': '3', 'b': '3', 'c': '3', 'd': '3', 'e': '3', '0': '3', '1': '3', '2': '3', '3': '3'},
}
print(input_symbols)
print("Invalid input") if no_of_accepting_states != len(accepting_states) else print("Accepted" if dfa(input("Enter the input string: "),input_symbols,no_of_states, initial_state, accepting_states, transition_table) else "Rejected")

