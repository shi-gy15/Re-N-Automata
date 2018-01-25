
class State:
    _seqno_ = 0

    def __init__(self, acc=False):
        self.seqno = State._seqno_
        State._seqno_+=1
        self.trans = {}
        self.acc = acc

    def add(self, alpha, q):
        if type(alpha) == list:
            for item in alpha:
                self.trans[item] = q
        else:
            self.trans[alpha] = q

class Automata:

    def __init__(self, begin, alphabet=r'01'):
        self.begin = begin
        self.alphabet = alphabet

    def parse(self, str):
        length = len(str)
        curq = self.begin
        if not curq:
            raise Exception('Automata undefined.')
            return False
        for i in range(length):
            if str[i] not in self.alphabet:
                raise Exception('Wrong letter.')
                return False
            if str[i] not in curq.trans:
                return False
            curq = curq.trans[str[i]]
        return curq.acc

def isNone(cond):
    if cond:
        raise Exception('Wrong expression.')

def notNone(cond):
    if cond is None:
        raise Exception('Wrong expression.')

class Regex:
    # supported grammar:
    # a*
    # a+
    # [abcd]

    def __init__(self, expr, alphabet=r'01'):

        funcs = r'*+[]'
        single = None
        stack = None
        length = len(expr)
        for i in range(length):
            if expr[i] in alphabet:
                if stack is not None:
                    isNone(single)
                    if expr[i] in stack:
                        raise Exception('Wrong expression.')
                    stack.append(expr[i])
                elif single:
                    # add(single, automata)
                    single = expr[i]
                else:
                    single = expr[i]
            elif expr[i] in funcs:
                if expr[i] == '*' or expr[i] == '+':
                    isNone(stack)
                    notNone(single)
                    # add(single, expr[i], automata)
                    single = None
                elif expr[i] == '[':
                    isNone(stack)
                    if single:
                        # add(single, automata)
                        single = None
                    stack = []
                elif expr[i] == ']':
                    isNone(single)
                    if stack == []:
                        raise Exception('Wrong expression.')
                    single = ''.join(stack)
                    stack = None
                else:
                    raise Exception('Wrong expression.')
            else:
                raise Exception('Wrong expression.')




q0 = State()
q1 = State()
q2 = State(True)
q3 = State()

q0.add('0', q1)
q1.add('0', q1)
q1.add('1', q2)
q2.add('0', q3)
q2.add('1', q3)

aut = Automata(begin=q0)

reg = Regex(r'0*1*0001[01]+00+0')