import string
import re

class PhoneNumber:

    def __init__(self, number):
        self.number = re.sub(r'[-\(\)+.\s]', '', number)
        self.number = self.validate(self.number)
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.rest_of_number = self.number[6:]

    def validate(self, number):
        if len(number) > 11:
            raise ValueError("more than 11 digits")
        elif len(number) < 10:
            raise ValueError("incorrect number of digits")
        if len(number) == 11:
            if number[0] != '1':
                raise ValueError("11 digits must start with 1")
            else:
                number = number[1:]

        for i in number:
            if i in string.punctuation:
                raise ValueError("punctuations not permitted")

        for i in number:
            if i in string.ascii_letters:
                raise ValueError("letters not permitted")

        if number[0] == '0':
            raise ValueError("area code cannot start with zero")
        if number[0] == '1':
            raise ValueError("area code cannot start with one")
        if number[3] == '1':
            raise ValueError("exchange code cannot start with one")
        if number[3] == '0':
            raise ValueError("exchange code cannot start with zero")

        return number

    def pretty(self):
        return f'({self.area_code})-{self.exchange_code}-{self.rest_of_number}'