class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        l = list(s)
        i,j = 0, len(l) - 1
        while i < j:
            while i < j and l[i] not in vowels:
                i += 1
            while i < j and l[j] not in vowels:
                j -= 1

            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1

        return ''.join(l)
