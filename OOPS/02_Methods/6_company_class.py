"""
6. Create a class `Company` with:
   - class variable `company_name`
   - class method `change_company(name)`
   - show that the change reflects for all objects
"""

class Company:
    company_name = "Tech Corp"

    @classmethod
    def change_company(cls, name):
        cls.company_name = name

if __name__ == "__main__":
    e1 = Company()
    e2 = Company()

    print(f"Initial: {e1.company_name}, {e2.company_name}")

    Company.change_company("Innovate Ltd")

    print(f"After Change: {e1.company_name}, {e2.company_name}")
