## FASTAPI:

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.

```bash 
pip install fastapi
```
```bash
pip install uvicorn
``` 
Uvicorn is an ASGI web server implementation for Python.

```bash
pip install python-multipart
```
To receive uploaded files, first install python-multipart.
This is because uploaded files are sent as "form data".

### To run the python file:

```bash
uvicorn main:my_app
```
(main is the python filename)
(my_app is the fastAPI variable)

## Rendering docx:

This uses 2 major packages:
* python-docx for reading, writing and creating sub documents.
* jinja2 for managing tags inserted into the template docx.
python-docx-template is used for creating documents but not for modifying them.

### Install docxtpl using pip:

```bash
pip install docxtpl
```

* PIP is a package manager for Python packages, or modules.
* docxtpl is a inspiration from python libraries that does word document templating.

### For installing all of the python requirements

```bash
pip install -r requirements.txt
```