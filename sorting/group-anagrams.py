class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # record={}
        # path=[]
        # result=[]
        # for st in  strs:
        #     for s in st:
        #         if s in record:
        #             record[s]-=1
        #         record[s]+=1
        #     #如果三个都能找到
        #     path.append(str)

        groups=defaultdict(list)
        for str in strs:
            key="".join(sorted(str))
            groups[key].append(str)
        return list(groups.values())
            
            