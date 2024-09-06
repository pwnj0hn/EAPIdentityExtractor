import pyshark
import argparse
import os
import sys

def extract_eap_identity(pcap_file):
    # Try to open and process the pcap file
    try:
        capture = pyshark.FileCapture(pcap_file, display_filter='eap')
    except Exception as e:
        print(f"Error reading pcap file: {e}")
        sys.exit(1)
    
    identities = []

    # Iterate through each packet in the capture
    try:
        for packet in capture:
            if hasattr(packet, 'eap'):
                # Check if the packet contains an EAP Identity field
                if hasattr(packet.eap, 'identity'):
                    identity = packet.eap.identity
                    identities.append(identity)
    except Exception as e:
        print(f"Error processing packets: {e}")
        sys.exit(1)
    finally:
        capture.close()

    return identities

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Extract EAP identity fields from a pcap file.")
    parser.add_argument('-f', '--file', required=True, help='Path to the pcap file')

    # Parse arguments
    args = parser.parse_args()

    # Check if file exists
    if not os.path.exists(args.file):
        print(f"Error: The file '{args.file}' does not exist.")
        sys.exit(1)

    # Call the function to extract EAP identities
    eap_identities = extract_eap_identity(args.file)

    if eap_identities:
        print("Extracted EAP Identities:")
        for identity in eap_identities:
            print(identity)
    else:
        print("No EAP Identities found in the pcap file.")

if __name__ == "__main__":
    main()
