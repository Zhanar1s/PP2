class String:
    def inp(self):
        self.input_str = ""
    
    def getStr(self):
        self.input_str = input()

    def printStr(self):
        print(self.input_str.upper())

word = String()
word.getStr()
word.printStr()