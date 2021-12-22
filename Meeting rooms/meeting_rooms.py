class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        out = True
        ordered = []
        ordered = sorted(intervals, key=lambda x:x[1])
        for i in range(len(ordered)-1):
                a,b =  ordered[i] 
                c,d = ordered[i+1]  
                print([a,b], [c,d])
                if (c>a and d>b and b<=c):
                    continue
                else:
                    return (not(out))    
        return out
                
            
        
        