import pandas as pd
import numpy as np

# Create 72 time stamps by hour
rng = pd.date_range('9/11/2017', periods=72, freq='H')  # 'M/D/Y'

ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)

# Pick items from 9/12/2017 to 9/13/2017
print(ts.truncate(before='9/12/2017', after='9/13/2017'))

# Change elements to datetime
print(pd.to_datetime(pd.Series(['Jul 31, 2009', '2010-01-10', None])))  # NaT: Not a Time
