class empolyee():
    company="ITC"
    salary="120000"
    def show(self):
        print(f"the company name is {self.company}.\n the salary is {self.salary}")

class coder():
    language="python"
    def printlanguage(self):
        print(f"out of all language here is your language : {self.language}")

class programmer(empolyee,coder):
    company="ITC infotech"
    language="django"
    def showlanguage(self):    
        print(f"the company name is {self.company} and he is good in {self.language} language")

a=empolyee()
b=programmer()

b.show()
b.printlanguage()
b.showlanguage()