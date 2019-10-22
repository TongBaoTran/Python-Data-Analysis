class Prepend:
    def __init__(self, istring):
        self.start=istring

    def write(self,s):
         print(self.start+s)

p = Prepend("+++ ")
p.write("Hello")

