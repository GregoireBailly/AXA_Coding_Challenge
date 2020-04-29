class Person:
    def __init__(self, name, domain, morning, evening):
        self.name = name
        self.domain = domain
        self.morning  = morning
        self.evening = evening

        # the index of the option (0 to n-1); -1 if the person is not going to work
        self.optionM = -1
        self.optionE = -1

    def __str__(self):
        toPrint = self.name
        toPrint += str(self.domain)
        toPrint += str(self.morning)
        toPrint += str(self.evening)

        return toPrint
