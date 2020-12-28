class Solution:
    def combinationSum(self, candidates, target):
        def dfs(candidates,begin,path,answer,target):
            if target == 0:
                answer.append(path)
                return
            if target < 0:
                return
            if target > 0:
                for i in range(begin,len(candidates)):
                    dfs(candidates,i,path + [candidates[i]],answer,target - candidates[i])

        begin = 0
        path = []
        answer = []
        dfs(candidates,begin,path,answer,target)
        return answer
'''循环从begin开始是为了 不会出现往前搜索的情况，也就不会出现重复'''
