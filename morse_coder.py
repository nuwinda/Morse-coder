# morse_decode.py 🔧

MORSE_CODE = {
    # Letters
    ".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F",
    "--.":"G","....":"H","..":"I",".---":"J","-.-":"K",".-..":"L",
    "--":"M","-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R",
    "...":"S","-":"T","..-":"U","...-":"V",".--":"W","-..-":"X",
    "-.--":"Y","--..":"Z",
    # Numbers
    "-----":"0",".----":"1","..---":"2","...--":"3","....-":"4",
    ".....":"5","-....":"6","--...":"7","---..":"8","----.":"9",
    # Common punctuation
    ".-.-.-":".","--..--":",","..--..":"?",".----.":"'",
    "-.-.--":"!","-..-.":"/","-.--.":"(","-.--.-":")",
    ".-...":"&",":---:":";", "-...-":"=",".-.-.":"+","-....-":"-",
    "..--.-":"_",".-..-.":'"',".--.-.":"@"
}

def decode_morse(morse: str) -> str:
    """
    Decode a Morse code string into uppercase text.
    - Letters separated by single spaces.
    - Words separated by 3 spaces OR by '/' (common alternative).
    Unknown sequences are replaced with '?'.
    """
    if not morse:
        return ""
    # Normalize word separators: accept '/' or 3+ spaces
    morse = morse.strip()
    morse = morse.replace(" / ", "   ")
    words = morse.split("   ")
    decoded_words = []
    for w in words:
        letters = w.split()
        decoded = "".join(MORSE_CODE.get(ch, "?") for ch in letters)
        decoded_words.append(decoded)
    return " ".join(decoded_words)


def main():
    """Simple CLI entry point for decoding Morse code."""
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Decode Morse code to text")
    parser.add_argument("morse", nargs="*", help="Morse code string (use '/' or 3 spaces for word separators)")
    parser.add_argument("-f", "--file", help="Read Morse code from a file")
    parser.add_argument("-l", "--lower", action="store_true", help="Output in lowercase")
    args = parser.parse_args()

    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as fh:
                morse = fh.read().strip()
        except Exception as e:
            print(f"Error reading file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        if not args.morse:
            parser.print_help()
            sys.exit(0)
        morse = " ".join(args.morse)

    out = decode_morse(morse)
    if args.lower:
        out = out.lower()
    print(out)


if __name__ == "__main__":
    main()