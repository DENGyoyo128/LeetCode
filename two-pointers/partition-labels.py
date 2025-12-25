class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occur={}
        for i,ch in enumerate(s):
            last_occur[ch]=i
        
        start=0
        end=0
        res=[]
        for i,ch in enumerate(s):
            end=max(end,last_occur[ch])
            if i==end:
                res.append(end-start+1)
                start=i+1
        return res