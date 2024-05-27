class Solution():
    def reverseString(self,string):
        left,right=0,len(string)-1
        while left<right:
            string[left],string[right]=string[right],string[left]
            left,right=left+1,right-1
            
reverse=Solution()

stringList=list(input("input a string: "))

reverse.reverseString(stringList)
teststring=''.join(stringList)
print(teststring)