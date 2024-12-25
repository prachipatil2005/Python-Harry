class Employee:
    name="prachi"
    salary=12000
    @staticmethod
    def greet():
        print("Goog morning")
result=Employee()
result.greet()
print(f"{result.name}")