# DumbCopyPaste
Retypes all text from file. Made to copy whole base64 encoded file to a VM that was only accessible through browser.
Currently supports only uper and lower case letters and simple characters: `~!@#$%^&*()_+{}|:"<>?`
Works for copy pasting URLs.

`pip install pynput` - that's the only dependency

Example usage:
`python typer.py -s 7 -l 0.1 fileWithText` - run after 7 seconds with 0.1 second per each typed letter
