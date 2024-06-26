import pandas as pd
class Stops(object):
    def __init__(self, ws, time_delta, margin_start, margin_end, stop_speed):
        self.ws = ws
        self.time_delta = time_delta
        self.margin_start = margin_start
        self.margin_end = margin_end
        self.stop_speed = stop_speed


    def count_stops(trip):
        def trim(self,n):
            time_end = trip(self,n)['time_seconds'].max()
            trimed_start = trip(self,n)[trip(self,n).time_seconds > self.margin_start]
            trimmed = trimed_start[trimed_start.time_seconds < time_end - self.margin_end]
            sf = trimmed[trimmed.speed_meters_per_second < self.stop_speed]
            if sf.empty:
                return 0
            else:
                c = 1
                for i in range(len(sf) - 1):
                    if sf['time_seconds'].iloc[i+1] - sf['time_seconds'].iloc[i] > self.time_delta:
                        c = c + 1
                return c
        return trim

    @count_stops
    def trip(self,n):
        return self.ws.trip(n)
