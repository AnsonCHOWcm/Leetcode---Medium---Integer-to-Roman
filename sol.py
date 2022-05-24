class Solution:
    def intToRoman(self, num: int) -> str:

        roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

        i = 0

        res = []

        while (num != 0):

            i += 2

            digit = num % 10
            num = num // 10

            if (i > 6):

                for j in range(digit):
                    res.append(roman[-1])

                continue

            component_1 = roman[i - 2]
            component_2 = roman[i - 1]
            component_3 = roman[i]

            if (digit < 4):

                for j in range(digit):
                    res.append(component_1)

            elif (digit == 4):

                res.append(component_2)
                res.append(component_1)

            elif (digit == 5):

                res.append(component_2)

            elif (digit < 9):

                for j in range(digit - 5):
                    res.append(component_1)

                res.append(component_2)

            elif (digit == 9):

                res.append(component_3)
                res.append(component_1)

        res = res[::-1]

        return (''.join(res))