# control_unit.py

control_signals = {
    "GET":      {"type": "LOAD",     "alu_op": "NOP",   "reg_write": 1, "mem_read": 1, "mem_write": 0},
    "SAVE":     {"type": "STORE",    "alu_op": "NOP",   "reg_write": 0, "mem_read": 0, "mem_write": 1},
    "ASSIGN":   {"type": "MOV",      "alu_op": "NOP",   "reg_write": 1, "mem_read": 0, "mem_write": 0},
    "SUM":      {"type": "ALU",      "alu_op": "ADD",   "reg_write": 1, "mem_read": 0, "mem_write": 0},
    "DIFF":     {"type": "ALU",      "alu_op": "SUB",   "reg_write": 1, "mem_read": 0, "mem_write": 0},
    "PROD":     {"type": "ALU",      "alu_op": "MUL",   "reg_write": 1, "mem_read": 0, "mem_write": 0},
    "SPLT":     {"type": "ALU",      "alu_op": "DIV",   "reg_write": 1, "mem_read": 0, "mem_write": 0},
    "ALL":      {"type": "ALU",      "alu_op": "AND",   "reg_write": 1, "mem_read": 0, "mem_write": 0},
    "ANY":      {"type": "ALU",      "alu_op": "OR",    "reg_write": 1, "mem_read": 0, "mem_write": 0},
    "XANY":     {"type": "ALU",      "alu_op": "XOR",   "reg_write": 1, "mem_read": 0, "mem_write": 0},
    "RDISPLACE":{"type": "ALU",      "alu_op": "SHIFTR","reg_write": 1, "mem_read": 0, "mem_write": 0},
    "LDISPLACE":{"type": "ALU",      "alu_op": "SHIFTL","reg_write": 1, "mem_read": 0, "mem_write": 0},
    "EX":       {"type": "BRANCH",   "cond": "ALWAYS",  "reg_write": 0},
    "EXQ":      {"type": "BRANCH",   "cond": "EQ",      "reg_write": 0},
    "EXN":      {"type": "BRANCH",   "cond": "NEQ",     "reg_write": 0},
    "EXG":      {"type": "BRANCH",   "cond": "GT",      "reg_write": 0},
    "EXL":      {"type": "BRANCH",   "cond": "LT",      "reg_write": 0},
    "EXGE":     {"type": "BRANCH",   "cond": "GE",      "reg_write": 0},
    "EXLE":     {"type": "BRANCH",   "cond": "LE",      "reg_write": 0},
    "GENFIRM":  {"type": "SUP",      "operation": "GENFIRM", "reg_write": 0}
}

def get_control_signals(instruction):
    """Recibe un string de instrucción y devuelve las señales de control correspondientes"""
    opcode = instruction.split()[0].upper()
    return control_signals.get(opcode, None)
