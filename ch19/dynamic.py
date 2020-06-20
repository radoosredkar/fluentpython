class testDynamic:
    st1 = None
    st2 = None

    def __str__(self):
        return f"{self.st1}, {self.st2}"

    def __getattr__(self, attr):
        if attr == "sum":
            return self.st1 + self.st2
        else:
            raise AttributeError(f"object has no attribute '{attr}'")

test = testDynamic()
test.st1 = 12
test.st2 = 14
print(test)
print(test.sum)
