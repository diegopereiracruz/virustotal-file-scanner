# VirusTotal API Interaction Script

A malware scanner program that obtains the file or hash of the file and returns the VirusTotal scan result directly to your terminal.

## Overview

The primary components of this project include:

- `vt_api_call.py`: Handles making API calls to VirusTotal and processing responses.
- `vt_api_json_print.py`: Contains functions for parsing and printing the JSON response from VirusTotal.
- `vt_api_key.py`: Manages the loading and saving of the VirusTotal API key.
- `vt_api_state.py`: Keeps track of the number of API calls made and ensures compliance with rate limits.

## Prerequisites

Ensure you have Python installed on your system. This project uses standard Python libraries such as `requests` and `json`.

## Installation

Clone the repository to your local machine:
```bash
git clone https://github.com/diegopereiracruz/virustotal-file-scanner.git 
cd virustotal-file-scanner
```

## Usage

Before running any script, ensure you have obtained a VirusTotal API key and saved it in the `~/vt_api_files/vt_api_key.txt` file. Create the folder in your home directory if you haven't run the script yet.

```bash
mkdir ~/vt_api_files
nano ~/vt_api_files/vt_api_key.txt
```

Just paste the API KEY to the file and save.

To run the main script, execute:

```bash
python3 virustotal.py <md5sum_hash or file_path>
```

Replace `<md5sum_hash or file_path>` with the MD5 hash or file path you wish to analyze.

###### Usage examples
```bash
python3 virustotal.py f4c3fa43b5bdfaa0205990d25ce51c5a
```
or
```bash
python3 virustotal.py path/to/file.ext
```

## Alias
```bash
vc() {
    python3 path/to/virustotal.py $1
}
```
vc = virus checker

## Contributing

Contributions are welcome Please feel free to submit a pull request or create an issue if you encounter any problems.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
