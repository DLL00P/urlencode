# urlencode

## Usage
You can give it a positional argument for a single string, or you can pipe input to it from stdin.
```bash
$ urlencode 'example 1'
example%201

$ echo -n 'example 2'|urlencode
example%202
```
You can pass `-d` or `--decode` to decode the input.
```bash
$ urlencode -d 'example%201'
example 1

$ echo -e "example%201\nexample%202" | urlencode -d
example 1
example 2
```
