class Person:
    def __init__(self, name, domain, morning, evening):
        self.name = name
        self.domain = domain
        self.morning  = morning
        self.evening = evening

    def __str__(self):
        toPrint = self.name
        toPrint += str(self.domain)
        toPrint += str(self.morning)
        toPrint += str(self.evening)

        return toPrint
