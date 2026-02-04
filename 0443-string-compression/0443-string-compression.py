class Solution:
    def compress(self, chars):
        write = 0   # position to write compressed characters
        read = 0    # position to read characters

        while read < len(chars):
            char = chars[read]
            count = 0

            # count occurrences of current character
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # write the character
            chars[write] = char
            write += 1

            # write the count if > 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

        return write
