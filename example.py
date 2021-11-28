import time
import sys
import tracemalloc

from sum_urandom import sum_urandom

def mb_bytes(mb):
  return mb * (10 ** 6)

if __name__ == '__main__':

  if len(sys.argv) != 2:
    print(f'Usage: {sys.argv[0]} [RSS_MB]', file=sys.stderr)
    sys.exit(1)

  rss_mb = int(sys.argv[1])

  print(f'sleeping for 15s before RSS grows to ~{rss_mb} MB')
  time.sleep(15.0)
  print('about to start loop')

  tracemalloc.start()
  (tm_cur_bytes_before, tm_peak_bytes_before,) = tracemalloc.get_traced_memory()
  tm_snap_before = tracemalloc.take_snapshot()

  rss_bytes = mb_bytes(rss_mb)
  urandom_read_len = 10000
  for i in range(int(rss_bytes / urandom_read_len)):
    _ = sum_urandom(urandom_read_len)

  print('sleeping for 15s after')
  time.sleep(15.0)

  (tm_cur_bytes_after, tm_peak_bytes_after,) = tracemalloc.get_traced_memory()
  tm_snap_after = tracemalloc.take_snapshot()

  tm_cur_bytes_diff = tm_cur_bytes_after - tm_cur_bytes_before
  tm_peak_bytes_diff = tm_peak_bytes_after - tm_peak_bytes_before

  print('tracemalloc stats')
  print('-----------------')
  print(f'tm_cur_bytes_diff:{tm_cur_bytes_diff}')
  print(f'tm_peak_bytes_diff:{tm_peak_bytes_diff}')
  print('-----------------')
  
  for snap_diff in tm_snap_after.compare_to(tm_snap_before, 'lineno', True):
    print(snap_diff)

  print('-----------------')



