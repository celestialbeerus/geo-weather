class employee:
    language="python"
    salary=1200000

    def getinfo(self):
        print(f"The language is {self.language}.\n the salary is {self.salary}")
    #so we can create function and in class and we can write anyting in parathesis but generally self is write it is important an variable in parathesis
        

harry=employee()
harry.language="javascript"#so now python will be not printed javascrpit will be printed this is called inasatance attribute
harry.getinfo()