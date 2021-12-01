# AST2000 Interactive Lecture Notes
This repository contains the interactive lectures notes for the course AST2000 taught at the University of Oslo.

Additionally the script `main.py` can be used to convert these notes from latex into a static html page.
## Dependencies
The only required dependency for running the script `main.py` is Pandoc. See [the official docs](https://pandoc.org/installing.html) for a guide on downloading Pandoc.

## Usage
```python
python main.py
```
Running the script `main.py` converts `.tex` documents found in the folders given by `1A/`, `1B/`, ... into static html and exports this into the a generated `output/` directory. This directory can then be hosted locally, for instance by using the built-in python http server.
```python
python -m http.server
```
This will use the port 8000 by default, which can then be accessed at http://localhost:8000/output/ to interact with the website. Remember to run this command in the same directory where `output/` lives.