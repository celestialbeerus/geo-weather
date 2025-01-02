class empolyee():
    company="ITC"
    salary="120000"
    def show(self):
        print(f"the company name is {self.company}.\n the salary is {self.salary}")

# class progammer():
#     company="ITC infotech"
#     def show(self):
#         print(f"the name is {self.name}.\n the salary is {self.salary}")

# def showlanguage(self):
#     print(f"the name is {self.name} and he is good in {self.language} language")

# the above line  can be replaced by 4 line of code so this function is called inheritance

class programmer(empolyee):
    company="ITC infotech"
    language="django"
    def showlanguage(self):    
        print(f"the company name is {self.company} and he is good in {self.language} language")

a=empolyee()
b=programmer

print(a.company,b.company)
