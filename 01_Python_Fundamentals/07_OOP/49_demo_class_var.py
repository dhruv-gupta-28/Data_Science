class Demo:
    x = 10

    def modify_x(self):
        Demo.x += 5

if __name__ == "__main__":
    d = Demo()
    print(f"Before: {Demo.x}")
    d.modify_x()
    print(f"After: {Demo.x}")
