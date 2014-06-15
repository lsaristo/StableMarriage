class Man(object):
    def __init__(self, n, p):
        self.pref = p
        self.number = n 
        self.attached = False
    def propose(self):
        if self.attached:
            return True
        if not (self.pref[0]).propose(self):
            self.pref.pop(0)
        else:
            self.attached = self.pref[0]
    def reject(self, woman):
        self.pref.pop(0)
        self.attached = False
    def __repr__(self):
        string = str(self.number) + " --> " + str(self.pref[0])
        return string
    def __str__(self):
        return self.__repr__()

class Woman(object):
    def __init__(self, l, p):
        self.pref = p
        self.letter = l
        self.attached = False
    def propose(self, man):
        if not self.attached:
            self.attached = man
            return True
        else:
            for m in self.pref:
                if m.number == man.number:
                    self.attached.reject(self)
                    self.attached = man
                    return True
                elif m.number == self.attached.number:
                    return False
    def __str__(self):
        return self.__repr__()              
    def __repr__(self):
        return self.letter

def main():
    """ The stable marriage algorithm """
    A_pref = [1,2,3]
    B_pref = [3,2,1]
    C_pref = [2,1,3]
    a_pref = ['A','B','C']
    b_pref = ['A','C','B']
    c_pref = ['A','C','B']

    a = Man(1, a_pref)
    b = Man(2, b_pref)
    c = Man(3, c_pref)
    A = Woman('A', A_pref);
    B = Woman('B', B_pref);
    C = Woman('C', C_pref);
    a.pref = [A,B,C]
    b.pref = [A,C,B]
    c.pref = [B,A,C]
    A.pref = [a,b,c]
    B.pref = [c,b,a]
    C.pref = [b,a,c]

    while not a.attached or not b.attached or not c.attached:
        a.propose()
        b.propose()
        c.propose()
    print "Run complete, here are the results", a, b, c
main()
