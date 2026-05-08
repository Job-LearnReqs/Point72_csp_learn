from datetime import datetime, timedelta

import csp
from csp import ts
import re

@csp.node
def regex_match(log_line: ts[str], regex: str) -> ts[bool]:
    if re.match(regex, log_line):
        return True


start = datetime(2020,1,1)
    
@csp.graph
def monitor_deployment():
    log_msgs = csp.curve(typ=str, data=[
        (start, 'WARNING: Load is heavy @ 90%'),
        (start + timedelta(minutes=1), 'INFO: New connection on port 42'),
        (start + timedelta(minutes=4), 'WARNING: Load is heavy @ 95%'),
        (start + timedelta(minutes=6), 'INFO: New connection on port 43'),
        (start + timedelta(minutes=9), 'CRITICAL: Overloaded, cannot connect new users!'),
    ])
    
    load_warnings = csp.count(regex_match(log_msgs, r'.*WARNING.*Load.*'))
    new_connections = csp.count(regex_match(log_msgs, r'.*INFO.*New connection.*'))

    csp.print("load_warnings", load_warnings)
    csp.print("new_connections", new_connections)

csp.run(monitor_deployment, starttime=start, endtime=timedelta(minutes=10))

