class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        roman = ""
        i = 0

        while num > 0:
            quotient = num // nums[i]
            # print("quotient",quotient, "num",num, "nums",nums[i])

            for _ in range(quotient):
                roman += symbols[i]
                num -= nums[i]

            i += 1

        return roman

num = 1994
Solution.intToRoman(1, num)