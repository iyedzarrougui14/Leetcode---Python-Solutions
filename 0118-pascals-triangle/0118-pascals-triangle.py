class Solution(object):
    def generate(self, numRows):
        output = []
        for i in range(numRows):
            if i == 0:
                # First row is always [1]
                output.append([1])
            else:
                # Start the current row with 1
                curr = [1]
                # Calculate the middle elements
                for j in range(1, i):
                    curr.append(output[i-1][j-1] + output[i-1][j])
                # End the current row with 1
                curr.append(1)
                # Add the current row to the output
                output.append(curr)
        return output