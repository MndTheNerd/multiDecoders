import base64

def decode_qr_code(string):
    """Decodes a QR code string.

    Args:
        string: The string to decode.

    Returns:
        A list of decoded data segments.
    """

    decoded_bytes = base64.b64decode(string)

    possible_encodings = ["utf-8", "latin-1", "ascii"]

    decoded_segments = []
    for encoding in possible_encodings:
        try:
            decoded_data = decoded_bytes.decode(encoding)
            parts = decoded_data.split("|") # incase it holds diffrent type of infromation and have | as split
            decoded_segments = [part.strip() for part in parts]
            break  # Stop decoding attempts if successful
        except UnicodeDecodeError:
            pass

    return decoded_segments
###############################################################################

def main():
    string = "String to Decode" # Enter the String you want to decode

###############################################################################
    decoded_data = decode_qr_code(string)

    if len(decoded_data) > 0:
        for i, segment in enumerate(decoded_data, start=1):
            print("Decoded Segment {}: {}".format(i, segment))
    else:
        print("No valid data segments found in the QR code")

if __name__ == "__main__":
    main()
