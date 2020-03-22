class QU:
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

    def find_root(self,p):
        i = p
        while self.id[i] !=  i:
            i = self.id[i]
        return i    

    def union(self,p,q):
        pid = self.find_root(p)
        qid = self.find_root(q)
        
        self.id[p] = qid
    
    def connected(self,p,q):
        pid = self.find_root(p)
        qid = self.find_root(q)

        return pid == qid
    
    def get_list(self):
        return self.id
test = QU("UF.txt")
def test_qf():
    test = QU("UF.txt")
    assert test.N == 10
    assert test.connected(0,6) == True
    assert test.connected(1,7) == True
    assert test.connected(0,3) == False
    print(test.get_list())
    test.union(0,8)
    print(test.get_list())
    assert test.connected(0,3) == True