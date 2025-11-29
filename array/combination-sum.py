class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()#方便剪枝
        def backtrack(start:int,remain:int,path: List[int]):
            if remain==0:
                res.append(path.copy())
                return
            
            for i in range(start,len(candidates)):
                nums=candidates[i]
                if nums>remain:
                    break
                path.append(nums)
                backtrack(i,remain-nums,path)
                path.pop()
        backtrack(0,target,[])
        return res
            