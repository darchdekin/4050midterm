class Solution:
    def minimumSum(self, num: int) -> int:     
        digitList = [int(m) for m in str(num)]
        digitList.sort();
        
        
        num1 = (10 * digitList[0]) + digitList[3]
        num2 = (10 * digitList[1]) + digitList[2]
        answer = num1 + num2
        
        return answer

object = Solution();
exampleNumber = 8032
print(object.minimumSum(exampleNumber))