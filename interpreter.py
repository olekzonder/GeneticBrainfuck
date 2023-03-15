import constants

def analyzeSyntax(program):

    bracketStack = []
    for i in program:
        if i == '[':
            bracketStack.append(i)
        if i == ']':
            if len(bracketStack) == 0:
                raise SyntaxError
            bracketStack.pop()
    
    if len(bracketStack) != 0:
        raise SyntaxError


def countBrackets(program):
    c = 0
    for i in program:
        if i == '[' or i == ']':
            c+=1
    return c
       
def interpret(program):
    program = str(program)
    analyzeSyntax(program)
    i = 0
    n = 0
    pos = 0
    cycle = 0
    buf = {0: 0}
    res = ''
    while i < len(program):
        if program[i] == '>':
            pos += 1
            buf.setdefault(pos,0)

        elif program[i]  == '<':
            if pos == 0:
                raise RuntimeError
            pos -= 1

        elif program[i] == '+':
            if buf[pos] == 255:
                raise OverflowError
            buf[pos] += 1

        elif program[i]  == '-':
            if buf[pos] == 0:
                raise OverflowError
            buf[pos] -= 1

        elif program[i] == '.':
            res += chr(buf[pos])

        elif program[i]  == '[':
            if buf[pos] == 0:
                while program[i] != ']':
                    i += 1
        elif program[i] == ']':
            if buf[pos] != 0:
                while program[i] != '[':
                    i -= 1

        i += 1
        n += 1
        if n >= constants.maxCycle:
            raise RecursionError

    if len(res) != 0:
        return res
    return False

def run(program):
    print(interpret(program))