def dfa(input, input_symbols, no_of_states, initial_state, no_of_accepting_states, accepting_states, transition_table):
    current_state = initial_state
    for symbol in input:
        current_state = transition_table[current_state][symbol]
        print(f"Current state: {current_state}")
        return current_state in accepting_states


# no_of_input_symbols = int(input("Enter the number of input symbols: "))
input_symbols = input("Enter the input symbols: ").split()
no_of_states = int(input("Enter the number of states: "))
initial_state = input("Enter the initial state: ")
no_of_accepting_states = int(input("Enter the number of accepting states: "))
accepting_states = input("Enter the accepting states: ").split()
transition_table = {
    '1': {'a': '2', 'b': '3'},
    '2': {'a': '1', 'b': '4'},
    '3': {'a': '4', 'b': '1'},
    '4': {'a': '3', 'b': '2'},
}
print(input_symbols)
print("Accepted" if dfa(input("Enter the input string: "),input_symbols,no_of_states, initial_state, no_of_accepting_states, accepting_states, transition_table) else "Rejected")

