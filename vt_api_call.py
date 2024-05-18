import json
import requests
from vt_api_json_print import *
from vt_api_state import *

def call_vt_api(url, api_key, program_files_path):
    state = load_state(program_files_path)

    call_state(state, program_files_path)

    api_json_response_path = os.path.join(program_files_path, "vt_response.json")

    headers = {
        "x-apikey": api_key,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        dados = response.json()

        with open(api_json_response_path, 'w') as file:
            json.dump(dados, file, indent=4)
        
        print_json(api_json_response_path)

    else:
        print(f"Error code: {response.status_code}")
        dados = response.json()

        with open(api_json_response_path, 'w') as file:
            json.dump(dados, file, indent=4)

        with open(api_json_response_path, 'r', encoding='utf8') as file:
            jsonString = file.read()
            if not jsonString:
                print("Arquivo vazio")
                exit()

            data = json.loads(jsonString)

            print(data['error']['message'])
    
    print("\nJSON file saved to: {}".format(api_json_response_path))

    #print(state)
    save_state(state, program_files_path)