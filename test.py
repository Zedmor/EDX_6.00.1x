class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        m = len(s)
        result = ''
        for z in range(numRows):
            for i in range(z,m,(2*numRows)-2):
                result += s[i]
            # for i in range(1,m,numRows-1):
            #     result +=s[i]
            # for i in range(0,m,(2*numRows)-2):
            #     result += s[i]
        return result

a = Solution()
print(a.convert('PAYPALISHIRING',3))