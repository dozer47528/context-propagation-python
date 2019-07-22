import logging

logger = logging.getLogger("context_propagation_python.module")


def auto_register():
    try:
        from context_propagation_python.module.requests import register
        register()
    except Exception as e:
        logger.debug("Register requests failed! %s" % str(e))
