import csp
from csp import ts, stats
from datetime import timedelta
from datetime import datetime, timezone
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
    res = csp.run(poisson_counter, rate=2.0, starttime=datetime.now(timezone.utc), endtime=timedelta(seconds=10), realtime=False)
    print(f'Final count: {res[0][-1][1]}')   
    # print(f'all points: {res}')


@csp.graph
def events_per_minute_bucket(poisson_counter: ts[int]) -> ts[int]:
    minute_timer = csp.timer(interval=timedelta(minutes=1), value=True)
    sampled_event_count = csp.sample(trigger=minute_timer, x=poisson_counter)
    events_per_minute = csp.diff(sampled_event_count, lag=timedelta(minutes=1))
    return events_per_minute

@csp.graph
def corr_graph() -> ts[float]:
    # Define two Poisson point processes
    process_A = poisson_counter(rate=1.0)
    process_B = poisson_counter(rate=1.0)
   
    # Get the per minute event counts
    counts_A = events_per_minute_bucket(process_A)
    counts_B = events_per_minute_bucket(process_B)

    # Compute correlation between two independent processes
    corr = csp.stats.corr(counts_A, counts_B)
    return corr

def run_2():
    res = csp.run(corr_graph, starttime=datetime.now(timezone.utc),
                  endtime=timedelta(minutes=2500), realtime=False)
    print(f'Correlation between two independent Poisson processes: {res[0][-1][1]}')

if __name__ == "__main__":
    # run_1()
    run_2()
