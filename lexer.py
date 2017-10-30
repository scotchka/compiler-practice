from errors import LexerError
from constants import SYMBOLS, INTEGER, EOF, RESERVED_KEYWORDS, ID, ASSIGN, SEMI, DOT


class Token(object):
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
        # print type_, value

    def __repr__(self):
        return '< Token {type_}: {value} >'.format(type_=self.type, value=self.value)


class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = self.text[self.pos]

    @staticmethod
    def error():
        raise LexerError('Invalid character')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        digits = []
        while self.current_char is not None and self.current_char.isdigit():
            digits.append(self.current_char)
            self.advance()
        return int(''.join(digits))

    def _id(self):
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()

        result = result.upper()

        if result in RESERVED_KEYWORDS:
            return Token(result, result)

        return Token(ID, result)

    def get_next_token(self):

        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char in SYMBOLS:
                current_char = self.current_char
                self.advance()
                return Token(SYMBOLS[current_char], current_char)

            if self.current_char.isalpha():
                return self._id()

            if self.current_char == ':' and self.peek() == '=':
                self.advance()
                self.advance()
                return Token(ASSIGN, ':=')

            if self.current_char == ';':
                self.advance()
                return Token(SEMI, ';')

            if self.current_char == '.':
                self.advance()
                return Token(DOT, '.')

            self.error()

        return Token(EOF, None)

    def peek(self):
        peek_pos = self.pos + 1
        if peek_pos > len(self.text) - 1:
            return None
        return self.text[peek_pos]
