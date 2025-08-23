class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#用哈希表记录字符的出现次数
        ans=0
        cnt=Counter()#hashmap
        left=0
        for  right,c in enumerate(s):
            cnt[c]+=1
            while cnt[c]>1:
                cnt[s[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans
        
        