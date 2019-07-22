from typing import Dict

from context_propagation_python.constants import BAGGAGE_PREFIX


def extract(carrier):
    # type: (Dict[str,str]) -> Dict[str,str]

    result = dict()

    for k, v in carrier.items():
        k = k.lower()
        if k.startswith(BAGGAGE_PREFIX):
            result[k[len(BAGGAGE_PREFIX):]] = v

    return result
