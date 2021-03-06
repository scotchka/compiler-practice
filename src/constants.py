import operator
from .token import Token

# token types

INTEGER = "INTEGER"
REAL = "REAL"
PLUS = "PLUS"
MINUS = "MINUS"
MULTIPLY = "MULTIPLY"
INTEGER_DIV = "INTEGER_DIV"
FLOAT_DIV = "FLOAT_DIV"
EOF = "EOF"
LPARENS = "LPARENS"
RPARENS = "RPARENS"
BEGIN = "BEGIN"
END = "END"
SEMI = "SEMI"
DOT = "DOT"
ID = "ID"
ASSIGN = "ASSIGN"
COLON = "COLON"
COMMA = "COMMA"
INTEGER_CONST = "INTEGER_CONST"
REAL_CONST = "REAL_CONST"
VAR = "VAR"
PROGRAM = "PROGRAM"
PROCEDURE = "PROCEDURE"

OPS = {
    PLUS: operator.add,
    MINUS: operator.sub,
    MULTIPLY: operator.mul,
    INTEGER_DIV: operator.floordiv,
    FLOAT_DIV: operator.truediv,
}

SYMBOLS = {
    "+": PLUS,
    "-": MINUS,
    "*": MULTIPLY,
    "/": FLOAT_DIV,
    "(": LPARENS,
    ")": RPARENS,
}

RESERVED_KEYWORDS = {
    "BEGIN": Token("BEGIN", "BEGIN"),
    "END": Token("END", "END"),
    "DIV": Token("INTEGER_DIV", "DIV"),
    "PROGRAM": Token("PROGRAM", "PROGRAM"),
    "VAR": Token("VAR", "VAR"),
    "INTEGER": Token("INTEGER", "INTEGER"),
    "REAL": Token("REAL", "REAL"),
    "PROCEDURE": Token("PROCEDURE", "PROCEDURE"),
}
