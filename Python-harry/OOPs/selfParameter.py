class Employee:
    language="Python"
    salary=120000
    
    def getInfo(self):
        print(f"The language is:{self.language}.The salary is:{self.salary}")
result=Employee()
result.language="Javascript"
result.getInfo()