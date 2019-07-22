from context_propagation_python.constants import THREAD_LOCAL_CONTEXT


def set_context(carrier):
    THREAD_LOCAL_CONTEXT.context = carrier


def get_context():
    if hasattr(THREAD_LOCAL_CONTEXT, 'context'):
        return {k: v for k, v in THREAD_LOCAL_CONTEXT.context.items()}
    else:
        return dict()
