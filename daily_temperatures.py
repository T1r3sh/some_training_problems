from collections import defaultdict
from itertools import chain

class SolutionX:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer_arr = []
        for idx, temp in enumerate(temperatures):
            len_ans = len(answer_arr)
            for n_idx, a_temp in enumerate(temperatures[idx+1:]):
                if a_temp>temp:
                    answer_arr.append(n_idx+1)
                    break
            if len_ans==len(answer_arr):
                answer_arr.append(0)
        return answer_arr
            
    def better_realization(self, temperatures: list[int]) -> list[int]:
        answer_arr = []
        info_arr = []
        for idx, temp in enumerate(temperatures):
            answer_arr.append(0)
            info_arr.append((idx, temp))
            for jxd, prev_temp in info_arr[:-1]:
                if idx>0 and temp>prev_temp:
                    answer_arr[jxd] = idx-jxd
                    info_arr.remove((jxd, prev_temp))
        return answer_arr
    
    def even_better_this_time(self, temperatures: list[int]) -> list[int]:
        answer_arr = []
        previous_temp_idx = defaultdict(list)
        for idx, temp in enumerate(temperatures):
            answer_arr.append(0)
            previous_temp_idx[temp].append(idx)
            greater_temp_indices = list(filter(lambda x: temp>x, previous_temp_idx.keys()))
            greater_temp = [previous_temp_idx.pop(pr_temp) for pr_temp in greater_temp_indices]
            flatten_indices = chain(*greater_temp)
            for index in flatten_indices:
                answer_arr[index] = idx-index
        return answer_arr
    
    def third_party_solution(self, T):
        next_warm_day = [0 for _ in T]

        for d in range(len(T) - 2, -1, -1):
            next_day = 1
            while next_day and T[d + next_day] <= T[d]: # while next_node and next_node.val <= curr_node.val
                if next_warm_day[d + next_day]:
                    next_day += next_warm_day[d + next_day]
                else:
                    next_day = 0
            next_warm_day[d] = next_day
        return next_warm_day
        
    
sol = SolutionX()
ans = sol.third_party_solution([89,62,70,58,47,47,46,76,100,70])
print(ans)            