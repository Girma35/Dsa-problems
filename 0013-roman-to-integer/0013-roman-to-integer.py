class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        prev = 0 
        roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

        for symbol in reversed(s) :
            value = roman[symbol]
            if value < prev:
                total -= value
            else:
                 total += value
            prev = value
           
        return total


        