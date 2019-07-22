from context_propagation_python.context import get_context, set_context


def get_value_from_context(key):
    return get_context().get(key)


def set_value_to_context(key, val):
    ctx = get_context()
    ctx[key] = val
    set_context(ctx)
