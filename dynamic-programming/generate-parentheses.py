class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(path:str,left_cnt:int,right_cnt:int):
            if len(path)==2*n:
                res.append(path)
                return
            
            if left_cnt<n:
                backtrack(path+"(",left_cnt+1,right_cnt)
            if right_cnt<left_cnt:
                backtrack(path+")",left_cnt,right_cnt+1)
            
        backtrack("",0,0)
        return res