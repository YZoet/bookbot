def count_L(s):
        letter_counts = {}
        for char in s:
                if char in letter_counts:
                        letter_counts[char] += 1
                else:
                        letter_counts[char] = 1
        return letter_counts