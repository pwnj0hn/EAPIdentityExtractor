# EAP Identity Extractor
EAP Identity Extractor is a Python script that parses a PCAP file to extract and display the Extensible Authentication Protocol (EAP) identity fields. This can be useful for network security analysts, penetration testers, and engineers who work with wireless networks and authentication protocols.

## Features
* Extract EAP Identity Fields: Filters through PCAP files and extracts the EAP identity responses.
* Command-Line Interface: Easy-to-use interface with options to specify input files and get help.
* Error Handling: Includes error handling for missing files, invalid PCAP formats, and corrupted data.
* Lightweight: Uses pyshark to parse PCAP files efficiently.

## Usage
To run the script, simply use:
```console
python eap_identity_extractor.py -f <your_pcap_file.pcap>
```

## Arguments:
* -f, --file: Path to the input PCAP file to analyze.
* -h, --help: Displays usage information and options.

## Example:
```console
python eap_identity_extractor.py -f sample.pcap
```

## Prerequisites
You'll need Python and the pyshark library. To install the dependencies:
```console
pip install pyshark
```
## Error Handling
If the file does not exist or is not a valid PCAP file, the script will print an error message and gracefully exit.
Handles exceptions during packet processing and ensures the program terminates without crashing.

## Contributions
Feel free to contribute! If you'd like to improve the script or add features, open an issue or create a pull request.
