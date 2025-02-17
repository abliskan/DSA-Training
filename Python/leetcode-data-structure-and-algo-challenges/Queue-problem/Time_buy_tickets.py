class Solution:
    def timeRequiredToBuy(self, t: List[int], k: int) -> int:
        time_order = 0
        least_num = t[k]
        for i in range(len(t)):         
            if k < i and t[i] >= least_num :
                time_order += (least_num - 1)
            elif t[i] < least_num :                   #(2)
                time_order += t[i]
            else:                                            #(3)
                time_order += least_num
				
        return time_order