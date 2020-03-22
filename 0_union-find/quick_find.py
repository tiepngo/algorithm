class QF:
    def __init__(self, file):
        with open(file,"r") as f:
            line = f.readlines()
            self.N = int(line[0])
            self.id = [i for i in range(self.N)]
            for l in line[1:]:
                #print(l)
                self.p = int(l.split()[0])
                self.q = int(l.split()[1])
                #print(l)
                #print("---Before : " , self.get_list())
                self.union(self.p, self.q)
                #print("---After  : " , self.get_list())

    def union(self,p,q):
        pid = self.id[p]
        qid = self.id[q]
        for i,value  in enumerate(self.id) :
            if self.id[i] == pid:
                self.id[i] = qid
    
    def connected(self,p,q):
        return self.id[p] == self.id[q]
    
    def get_list(self):
        return self.id
test = QF("UF.txt")
def test_qf():
    test = QF("UF.txt")
    assert test.N == 10
    assert test.connected(0,6) == True
    assert test.connected(1,7) == True
    assert test.connected(0,3) == False
    print(test.get_list())
    test.union(0,8)
    print(test.get_list())
    assert test.connected(0,3) == True