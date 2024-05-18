import subprocess
import sys
import os
import re
from vt_api_state import *
from vt_api_json_print import *
from vt_api_call import *
from vt_api_key import *

program_files_path = os.path.join(os.path.expanduser("~"), "vt_api_files/")
if not os.path.exists(program_files_path):
    os.makedirs(program_files_path)

def main():
    api_key = check_api_key(program_files_path)
    
    input_argv = sys.argv[1]

    if input_argv == "" or input_argv.lower() == "-h" or input_argv.lower() == "-help":
        print("Usage: python3 virustotal.py <md5sum_hash or file_path>")
        exit(0)

    hash_or_file = input_argv

    if len(hash_or_file) != 32 and bool(re.fullmatch(r'^[\w]*$', hash_or_file)) == False:
        if os.name == 'nt':
            print("Windows is not available yet!")
            exit(1)

            # temp_dir = "..."
            # output = subprocess.run(["powershell.exe", f'$(certutil -hashfile {input_argv} md5)[1] -replace " ",""'], shell=True, capture_output=True, text=True)
            # output = output.stdout
            # print(output)

        else:
            hash_filter = '{print $1}'
            
            try:
                hash_output = subprocess.getoutput(f'md5sum {hash_or_file} | awk \'{hash_filter}\'')

            except subprocess.CalledProcessError as err:
                print(f"Error: {err}")
                exit(1)
            
            print("File hash:", hash_output)
            hash_or_file = hash_output

    if len(hash_or_file) == 32:
        url = f'https://www.virustotal.com/api/v3/files/{hash_or_file}'

        call_vt_api(url, api_key, program_files_path)
        exit(0)

    else:
        print("MD5 hash only!")
        exit(1)

if __name__ == "__main__":
    main()
    exit(0)