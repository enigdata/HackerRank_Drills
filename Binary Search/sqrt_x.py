'''
Implement int sqrt(int x)

Example 1:
	Input:  0
	Output: 0


Example 2:
	Input:  3
	Output: 1
	
	Explanation:
	return the largest integer y that y*y <= x. 
	
Example 3:
	Input:  4
	Output: 2
'''

class Solution():
    def sqrt_x(self, x):
        if x == 0:
            return 0

        left, right = 0, x//2 + 1
        while left <= right:
            middle = (left + right)//2
            print(middle)
            if middle ** 2 == x:
                return middle
            elif middle ** 2 > x:
                right = middle - 1
            elif middle ** 2 < x:
                left = middle + 1

        return right

if __name__ == "__main__":
    print(Solution().sqrt_x(81))