import pickle

class StrToBytes:
    def __init__(self, fileobj):
        self.fileobj = fileobj
    def read(self, size):
        return self.fileobj.read(size).encode()
    def readline(self, size=-1):
        return self.fileobj.readline(size).encode()

dict_inds = {}
test_dict = './datasets/Capitals64/test_dict/dict.pkl'
with open(test_dict, 'r', encoding="utf-8") as file:
    dict_inds = pickle.load(StrToBytes(file), encoding = "utf-8")
print(dict_inds)
