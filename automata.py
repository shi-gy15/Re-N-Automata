
class State:
    _seqno_ = 0

    def __init__(self, acc=False):
        self.seqno = State._seqno_
        State._seqno_+=1
        self.trans = {}
        self.acc = acc

    def add(self, alpha, q):
        for item in alpha:
            if item in self.trans:
                self.trans[item].append(q)
            else:
                self.trans[item] = [q]

class Automata:

    def __init__(self, begin, alphabet='01'):
        self.begin = begin
        self.alphabet = alphabet

    def parse(self, string, curq=None):
        if curq is None:
            curq = self.begin

        if not curq:
            raise Exception('Automata undefined.')
            return False

        # if string ends here
        if string == '':
            return curq.acc

        # wrong letter
        if string[0] not in self.alphabet:
            raise Exception('Wrong letter.')
            return False

        # if epsilon trans exists
        if '~' in curq.trans:
            if self.parse(string[1:], curq.trans['~'][0]):
                return True
        
        # no trans
        if string[0] not in curq.trans:
            return False

        # trans iteration
        for tr in curq.trans[string[0]]:
            if self.parse(string[1:], tr):
                return True
        return False

def isNone(cond):
    if cond:
        raise Exception('Wrong expression.')

def notNone(cond):
    if cond is None:
        raise Exception('Wrong expression.')

def add(string, q, func=None):
    q.acc = False
    qf = State(True)
    if func == None:
        q.add(string, qf)
    else:
        if func == '*':
            q.add('~', qf)
            qf.add(string, qf)
        elif func == '+':
            q.add(string, qf)
            qf.add(string, qf)
    return qf

class Regex:
    # supported grammar:
    # a*
    # a+
    # [abcd]

    def __init__(self, expr, alphabet=r'01'):
        # create automata
        q0 = State(True)
        qf = q0
        self.automata = Automata(q0, alphabet)

        funcs = r'*+[]'
        end = '#'
        single = None
        stack = None
        expr += end
        length = len(expr)

        for i in range(length):
            if expr[i] == end:
                isNone(stack)
                if single:
                    qf = add(single, qf)
                break
            if expr[i] in alphabet:
                if stack is not None:
                    isNone(single)
                    if expr[i] in stack:
                        raise Exception('Wrong expression.')
                    stack.append(expr[i])
                elif single:
                    qf = add(single, qf)
                    single = expr[i]
                else:
                    single = expr[i]
            elif expr[i] in funcs:
                if expr[i] == '*' or expr[i] == '+':
                    isNone(stack)
                    notNone(single)
                    qf = add(single, qf, expr[i])
                    single = None
                elif expr[i] == '[':
                    isNone(stack)
                    if single:
                        qf = add(single, qf)
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

    def match(self, string):
        return self.automata.parse(string)

# automata test
q00 = State()
q11 = State()
q22 = State()
q33 = State(True)
q00.add('xy', q11)
q11.add('xy', q11)
q11.add('~', q22)
q22.add('xz', q22)
q22.add('z', q33)
a2 = Automata(q00, 'xyzv')
# print(a2.parse('xyxyxyxyxyyxyxxyxxyxxx'))

reg = Regex(r'0*1*0001[01]+00+0', '01')

print(reg.match('0001111000110110100101100'))

r2 = Regex('1+00+0', '01')
print(r2.match('100'))