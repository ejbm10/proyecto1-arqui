# decoder.py

import re
from control_unit import get_control_signals

# Expresiones regulares según tus patrones
patterns = [
    re.compile(r"^(GET|SAVE|ASSIGN)\s+(R\d+)\s+(\d+)\s*$", re.IGNORECASE),
    re.compile(r"^(SUM|DIFF|PROD|SPLT|ALL|ANY|XANY|RDISPLACE|LDISPLACE)\s+(R\d+)\s+(R\d+)\s+(R\d+)\s*$", re.IGNORECASE),
    re.compile(r"^(EX|EXQ|EXN|EXG|EXL|EXGE|EXLE)\s+([a-zA-Z_]\w*)\s*$", re.IGNORECASE),
    re.compile(r"^(GENFIRM|SUPGENFIRM)\s*$", re.IGNORECASE),
    re.compile(r"^([a-zA-Z_]\w*):\s*$", re.IGNORECASE)
]

def decode_line(line):
    line = line.strip()
    for pattern in patterns:
        match = pattern.match(line)
        if match:
            instr = match.group(1).upper()
            operands = match.groups()[1:]
            signals = get_control_signals(instr)
            return {"instr": instr, "operands": operands, "control": signals}
    return {"error": "Invalid syntax", "line": line}

if __name__ == "__main__":
    with open("prueba.txt") as f:
        for line in f:
            decoded = decode_line(line)
            print(decoded)
