class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_p=counter(p)
        left=0
        ans=[]
        for right, value in enumerate(s):
            left=right
            if value in cnt_p:
                cnt_p[value]-=1
                right+=1
                while left<right:
                    ans.append(left)
                