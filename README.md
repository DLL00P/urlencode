# urlencode
A tool developed in Python to facilitate URL-encoding and decoding of strings  
## Usage
You can provide a string directly as an argument, or pass input through a pipe.
```bash
$ urlencode 'example 1'
example%201

$ echo -n 'example 2'|urlencode
example%202
```
You can pass `-d` to decode the input.
```bash
$ urlencode -d 'example%201'
example 1

$ echo -e "example%201\nexample%202" | urlencode -d
example 1
example 2
```
You can keep a character unencoded with `-n`.
```bash
$ echo -n "'http://example.com'"|urlencode -n "'"
'http%3A%2F%2Fexample.com'

$ echo -n "'http://example.com'"|urlencode -n "/"
%27http%3A//example.com%27
```
## Installation
```bash
git clone https://github.com/DLL00P/urlencode
cd urlencode
chmod +x urlencode.py
sudo mv urlencode.py /usr/bin/urlencode
```

## References
- https://github.com/dead10ck/urlencode

- https://manpages.debian.org/stretch/gridsite-clients/urlencode.1.en.html
