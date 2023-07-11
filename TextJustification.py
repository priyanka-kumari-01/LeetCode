from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        current_line = []
        current_width = 0
        # print("fullJustify - words",words,|"maxWidth",maxWidth)
        for word in words:
            # print("full - current_width",current_width,"len(current_line)",len(current_line),"len(word)",len(word))
            if current_width + len(current_line) + len(word) > maxWidth:
              lines.append(self.justify_line(current_line, current_width, maxWidth))
              current_line = []
              current_width = 0

            current_line.append(word)
            current_width += len(word)

        # Process the last line
        last_line = " ".join(current_line)
        last_line += " " * (maxWidth - len(last_line))
        lines.append(last_line)

        return lines

    def justify_line(self, line, current_width, max_width):
        if len(line) == 1:
            return line[0] + " " * (max_width - current_width)

        num_words = len(line)
        num_spaces = max_width - current_width
        space_gaps = num_words - 1
        # print("   justify_line- num_words",num_words,"num_spaces",num_spaces,"space_gaps",space_gaps)
        spaces_per_gap = num_spaces // space_gaps
        extra_spaces = num_spaces % space_gaps

        justified_line = line[0]

        for i in range(1, len(line)):
            spaces = spaces_per_gap + (extra_spaces > 0)
            justified_line += " " * spaces
            extra_spaces -= 1
            justified_line += line[i]

        return justified_line

words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
maxWidth = 20

solution = Solution()
justified_text = solution.fullJustify(words, maxWidth)

for line in justified_text:
    print(line)