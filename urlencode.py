#!/usr/bin/env python3
import sys
import urllib.parse

def url_encode(text: str, safe_chars: str = "") -> str:
    return urllib.parse.quote(text, safe=safe_chars)

def url_decode(text: str) -> str:
    return urllib.parse.unquote(text)

def main():
    if sys.stdin.isatty() and len(sys.argv) == 1:
        print("\nEXAMPLES:")
        print("\n -- > urlencode 'string'")
        print("\n -- > urlencode [-d] 'string'")
        print("\n -- > urlencode [-n] 'string'")
        print(" \n -- > echo -n '1' | base64 | urlencode")
        sys.exit(0)

    decode_mode = False
    safe_chars = ""
    args = sys.argv[1:]

    # Review -d and -n options
    while len(args) > 0:
        if args[0] == "-d":
            decode_mode = True
            args = args[1:]
        elif args[0] == "-n":
            if len(args) < 2:
                print("Error: -n requires an argument with the characters to keep unencoded")
                sys.exit(1)
            safe_chars = args[1]
            args = args[2:]
        else:
            break

    # Read from pipe if there is
    if not sys.stdin.isatty():
        text = sys.stdin.read().rstrip("\n")
    elif args:
        text = " ".join(args)
    else:
        print("Error: No text provided to encode/decode.")
        sys.exit(1)

    # Execute
    if decode_mode:
        result = url_decode(text)
    else:
        result = url_encode(text, safe_chars)

    print(result)

if __name__ == "__main__":
    main()
