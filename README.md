# context-propagation-python

This middleware is used for support propagate context between micro services.

Supported framework for auto inject and extract:

* flask
* requests

## How to use

### Install

```shell
# pip
pip install git+https://github.com/AminoApps/context-propagation-python.git@v0.0.1

# pipenv
pipenv install git+https://github.com/AminoApps/context-propagation-python.git@v0.0.1#egg=context-propagation-python
```

### Operate data from context

```python
from context_propagation_python.util import get_value_from_context, set_value_to_context

set_value_to_context("my-key", "my-value")
get_value_from_context("my-key")
```

### Flask App

```python
from context_propagation_python.module.flask import register
from flask import Flask

app = Flask(__name__)

# `enable_auto_register` will auto patch `requests`, you can disable it and do it manually.
register(app, enable_auto_register=True)

@app.route('/')
def index():
    return 'hello world!'
```