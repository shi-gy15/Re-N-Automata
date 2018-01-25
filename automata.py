
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

q0 = State()
q1 = State()
q2 = State(True)
q3 = State()

q0.add('0', q1)
q1.add('0', q1)
q1.add('1', q2)
q2.add('0', q3)
q2.add('1', q3)

aut = Automata(q0=q0)
print(aut.parse('0000'))