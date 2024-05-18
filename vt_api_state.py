import json
import os
import time

def load_state(home_path):
    json_path = os.path.join(home_path, 'api_state.json')

    try:
        with open(json_path, 'r') as file:
            state = json.load(file)
            return state
    except FileNotFoundError:
        return {'calls_made': 0, 'last_call_time': 0, 'max_calls_per_minute': 4}

def save_state(state, home_path):
    json_path = os.path.join(home_path, 'api_state.json')

    try:
        with open(json_path, 'w') as file:
            json.dump(state, file)
    
    except Exception as err:
        print(f"Error saving state: {err}")

def call_state(state, home_path):
    current_time = time.time()
    
    if state['calls_made'] >= state['max_calls_per_minute'] and current_time - state['last_call_time'] < 60:
        print("Too many calls!")
        print("Only four calls per minute are allowed!")
        print("\nWaiting for 1 minute...")
        print("Current time:", int(current_time - state['last_call_time']), "seconds.")

        save_state(state, home_path)
        exit(1)

    elif state['calls_made'] >= state['max_calls_per_minute'] and current_time - state['last_call_time'] >= 60:
        state['calls_made'] = 0
    
    state['calls_made'] += 1
    remaining_calls = state['max_calls_per_minute'] - state['calls_made']
    print(f"Remaining calls in this minute: {remaining_calls}")

    state['last_call_time'] = current_time