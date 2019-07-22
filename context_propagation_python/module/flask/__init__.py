from flask import signals, request

from context_propagation_python import extract
from context_propagation_python.context import set_context
from context_propagation_python.module import auto_register


def register(app, enable_auto_register=True):
    signals.request_started.connect(request_started, sender=app)
    if enable_auto_register:
        auto_register()


def request_started(app):
    set_context(extract.extract(request.headers))