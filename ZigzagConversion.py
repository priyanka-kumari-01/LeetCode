class Solution:
  def convert_to_zigzag(s, num_rows):
    if num_rows == 1 or len(s) <= num_rows:
        return s

    rows = [''] * num_rows
    curr_row = 0
    direction = 1

    for char in s:
        rows[curr_row] += char
        if curr_row == 0:
            direction = 1
        elif curr_row == num_rows - 1:
            direction = -1
        curr_row += direction
        # print("ro2",rows, "C2",curr_row, "di2", direction, "num_row2",num_rows )
    return ''.join(rows)

# Example usage
s = "PAYPALISHIRING"
num_rows = 4
Solution.convert_to_zigzag(s, num_rows)
