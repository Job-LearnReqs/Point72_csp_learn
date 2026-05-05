import csp
from csp import ts
from datetime import timedelta
from datetime import datetime
import numpy as np

@csp.node(memoize=False)
def poisson_counter(rate: float) -> ts[int]:
    with csp.alarms():
        event = csp.alarm(int)
    with csp.state():
        s_count = 0
    with csp.start():
        delay = np.random.exponential(rate)
        csp.schedule_alarm(event, timedelta(seconds=delay), True)
        
    if csp.ticked(event):
        s_count += 1
        next_delay = np.random.exponential(rate)
        csp.schedule_alarm(event, timedelta(seconds=next_delay), True)
        return s_count


def run_1():
    res = csp.run(poisson_counter, rate=2.0, starttime=datetime.utcnow(), endtime=timedelta(seconds=10), realtime=False)
    print(f'Final count: {res[0][-1][1]}')   
    # print(f'all points: {res}')


if __name__ == "__main__":
    run_1()
