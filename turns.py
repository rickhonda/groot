import pandas as pd

class Turns(object):
    def __init__(self, ws, angle_delta):
        self.ws = ws
        self.angle_delta = angle_delta
        
    def count_turns(trip):
        def delta(self,t): # for a trip t
            d = []
            for i in range(len(trip(self,t)) - 1):
                c = trip(self,t).heading_degrees[i+1] - trip(self,t).heading_degrees[i]
                if abs(c) > 30: # catch zero crossing
                    if c > 0:
                        c = trip(self,t).heading_degrees[i+1] - 360 - trip(self,t).heading_degrees[i]
                    else:
                        c = 360 - trip(self,t).heading_degrees[i] + trip(self,t).heading_degrees[i+1]
                d.append(c)
            return d

        def reformat(self,n):
            t = trip(self,n)
            d = delta(self,n)
            dd = pd.DataFrame(d, columns = ['delta'])
            t['delta'] = dd
            t.reset_index(inplace=True)
            return t

        def sign_change(self,f): # f is a Dataframe with extra index and a delta column
            L = [0]
            for i in range(len(f)- 1):
                if f['delta'][i] >= 0:# and f['delta'][i+1] < 0:
                    if f['delta'][i+1] < 0: # but next entry is negative
                        L.append(f['index'][i+1])
                else: # entry is negative
                    if f['delta'][i+1] > 0: #next entry is positive
                        L.append(f['index'][i+1])
            return L

        def sc_sums(self,n): 
            df_rt = reformat(self,n)
            zeros = sign_change(self,df_rt)
            D = {}
            s = 0; i = 0
            while s < len(zeros) - 1:
                sum = 0
                while abs(sum) < self.angle_delta and s < len(zeros)-1:
                    for j in range(zeros[s],zeros[s+1]):
                        sum = sum + (df_rt.delta.iloc[j])
                    s = s + 1
                    if abs(sum) > self.angle_delta: 
                        D[zeros[s]] = int(sum)
                    i = s
            return len(D)

        def asdf(self,n):
            return sc_sums(self,n)
        return asdf

    @count_turns
    def trip(self,t):
        return self.ws.trip(t)
