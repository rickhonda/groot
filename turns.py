import pandas as pd

class Turns(object):
    def __init__(self, ws, angle_delta):
        self.ws = ws
        self.angle_delta = angle_delta
        
    def delta(self,t): # for a trip t
        d = []
        for i in range(len(t) - 1):
            c = t.heading_degrees[i+1] - t.heading_degrees[i]
            if abs(c) > 30: # catch zero crossing
                if c > 0:
                    c = t.heading_degrees[i+1] - 360 - t.heading_degrees[i]
                else:
                    c = 360 - t.heading_degrees[i] + t.heading_degrees[i+1]
            d.append(c)
        return d

    def reformat(self,trip):
        t = trip
        d = self.delta(t)
        dd = pd.DataFrame(d, columns = ['delta'])
        t['delta'] = dd
        t.reset_index(inplace=True)
        return t

    def sign_change(self,f):
        L = []
        for i in range(len(f)- 1):
            if f['delta'][i] >= 0:# and f['delta'][i+1] < 0:
                if f['delta'][i+1] < 0: # but next entry is negative
                    L.append(f['index'][i+1])
            else: # entry is negative
                if f['delta'][i+1] > 0: #next entry is positive
                    L.append(f['index'][i+1])
        return L
