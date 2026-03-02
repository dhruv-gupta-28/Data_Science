class Company:
    company_name = "ABC Corp"

    @classmethod
    def change_company(cls, name):
        cls.company_name = name

    def show(self):
        print(f"Company: {self.company_name}")

if __name__ == "__main__":
    e1 = Company()
    e2 = Company()

    print("Before change:")
    e1.show()
    e2.show()

    Company.change_company("XYZ Ltd")

    print("After change:")
    e1.show()
    e2.show()
