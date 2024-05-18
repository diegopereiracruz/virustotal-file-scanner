import os

def check_api_key(program_files_path):
    api_key_file_path = os.path.join(program_files_path, 'vt_api_key.txt')

    if os.path.exists(api_key_file_path):
        api_key = load_key(api_key_file_path)
    
    else:
        with open(api_key_file_path, 'w') as file:
            file.write("")

        print("Please, insert your VirusTotal API key to the \"vt_api_key.txt\" file.")
        print("\nAccess: https://www.virustotal.com/gui/sign-in")
        print("and copy and paste your API key to this file:", api_key_file_path)
        exit(1)

    if len(api_key) != 64:
        print("Invalid API key!")
        
        print("\nAccess: https://www.virustotal.com/gui/sign-in")
        print("and copy and paste your API key to this file:", api_key_file_path)
        exit(1)
    
    return api_key

def load_key(key_path):
    try:
        with open(key_path, 'r') as file:
            api_key = file.read().strip()
            return api_key

    except FileNotFoundError:
        return None