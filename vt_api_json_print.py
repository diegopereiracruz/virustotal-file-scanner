import datetime
import json


def format_size(bytes, si=False, dp=1):
    thresh = 1024 if not si else 1000
    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'] if si else ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
    u = -1
    r = 10 ** dp

    while abs(bytes) >= thresh and u < len(units) - 1:
        bytes /= thresh
        u += 1

    return f"{bytes:.{dp}f} {units[u]}"

def file_info(json_file):
    file_extension = ""

    try:
        file_extension = json_file['data']['attributes']['detectiteasy']['filetype']

    except KeyError:
        file_extension = json_file['data']['attributes']['type_extension']

    except:
        print(f"Extension not found!")

    if file_extension == "deb":
        deb_info = json_file['data']['attributes']['deb_info']['control_metadata']
        print("Source: ", deb_info['Source'])
        print("Website: ", deb_info['Homepage'])
        print("Description: ", deb_info['Description'])

    else:
        type_tags = json_file['data']['attributes']['type_tags']
        for tag in type_tags:
            print(tag)

def print_json(json_file_path):
    try:
        with open(json_file_path, 'r', encoding='utf8') as file:
            jsonString = file.read()
            if not jsonString:
                print("Arquivo vazio")
                return

            data = json.loads(jsonString)

            print("\nPACKAGE INFO")
            print("Name: " + data['data']['attributes']['meaningful_name'])
            print("Size: " + format_size(data['data']['attributes']['size'], True))

            file_info(data)

            print("\nSCAN DETAILS")
            print("Times Submitted:", data['data']['attributes']['times_submitted'])
            last_date = data['data']['attributes']['last_submission_date']
            print("Last submission:", datetime.datetime.fromtimestamp(last_date).strftime("%m-%d-%Y - %H:%M:%S"))

            analysis = data['data']['attributes']['last_analysis_stats']
            for key, value in analysis.items():
                if value!= 0:
                    print(key + ": " + str(value))

            print("\nSCAN RESULT")

            if data['data']['attributes']['total_votes']['harmless']!= 0:
                print("Harmless: ", data['data']['attributes']['total_votes']['harmless'])
            elif data['data']['attributes']['total_votes']['malicious']!= 0:
                print("Malicious: ", data['data']['attributes']['total_votes']['malicious'])
            else:
                print("Not defined yet!")

            print("Reputation:", data['data']['attributes']['reputation'])

            if 'popular_threat_classification' in data['data']['attributes']:
                print("\nThreat label:", data['data']['attributes']['popular_threat_classification']['suggested_threat_label'])

    except Exception as err:
        print('Erro ao analisar o JSON:', err)