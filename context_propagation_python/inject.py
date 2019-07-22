from typing import Dict

from context_propagation_python.constants import BAGGAGE_PREFIX


def inject(carrier):
    # type: (Dict[str,str]) -> Dict[str,str]

    return {BAGGAGE_PREFIX + k: v for k, v in carrier.items()}
