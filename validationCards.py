class ValidationOfCreditCards:
    def __init__(self):
        self.sumOfEvenIndexNumbers_to_str = None
        self.doubleEvenListValue = None
        self.listOfEvenIndexNumbers = None
        self.sumOfEvenIndexNumbers = None
        self.sumOfOddIndexNumbers = None
        self.list_card_numbers = None
        self.card_number = None

    def __int__(self):
        pass

    def valid(self, cardNumber):

        self.card_number = cardNumber
        self.list_card_numbers = list(self.card_number)
        self.sumOfOddIndexNumbers = 0
        self.sumOfEvenIndexNumbers = 0
        self.listOfEvenIndexNumbers = []
        self.doubleEvenListValue = []
        # print(list_card_numbers)

        for (index, value) in enumerate(self.list_card_numbers):
            if index % 2 != 0:
                self.sumOfOddIndexNumbers += int(value)
            else:
                self.listOfEvenIndexNumbers.append(int(value) * 2)

        # converting the list to a single string
        self.sumOfevenIndexNumbers_to_str = ""
        for x in self.listOfEvenIndexNumbers:
            self.sumOfevenIndexNumbers_to_str += str(x)

        # converting the string back  to a list
        listOfEvenIndexNumbers = list(self.sumOfevenIndexNumbers_to_str)
        for x in listOfEvenIndexNumbers:
            self.sumOfEvenIndexNumbers += int(x)

        print(f"sumOfOddIndexNumbers = {self.sumOfOddIndexNumbers}")
        print(f"sumOfEvenIndexNumbers = {self.sumOfEvenIndexNumbers}")

        if (self.sumOfOddIndexNumbers + self.sumOfEvenIndexNumbers) % 10 == 0:
            return "valid Card"
        else:
            return "Invalid Card"


v = ValidationOfCreditCards()
print(v.valid("5326103310346893"))