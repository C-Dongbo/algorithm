class Solution:
    def romanToInt(self, s: str) -> int:
        roman2int = {}
        roman2int['I'] = 1
        roman2int['V'] = 5
        roman2int['X'] = 10
        roman2int['L'] = 50
        roman2int['C'] = 100
        roman2int['D'] = 500
        roman2int['M'] = 1000
        roman2int['IV'] = -2
        roman2int['IX'] = -2
        roman2int['XL'] = -20
        roman2int['XC'] = -20
        roman2int['CD'] = -200
        roman2int['CM'] = -200

        result = 0

        for i in range(len(s)-1):
            result += roman2int[s[i]]
            if s[i] + s[i+1] in roman2int.keys():
                result += roman2int[s[i] + s[i+1]]

        result += roman2int[s[-1]]
        return result

if __name__ == '__main__':
    solution = Solution()
    test = 'IV'
    print(solution.romanToInt(test))

