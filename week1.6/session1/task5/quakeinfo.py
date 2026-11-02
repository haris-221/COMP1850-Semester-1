# Week 1.6, Session 1: Task 5

# Usage: python quakeinfo.py [level] [period]
# e.g.   python quakeinfo.py 4.5 week
# If level and period aren't given on the command line, you'll be prompted.

import sys

from dataset import QuakeDataset
from feed import QuakeFeed

if len(sys.argv) == 3:
    level, period = sys.argv[1], sys.argv[2]
else:
    level = input("Significance level (all, 1.0, 2.5, 4.5, significant): ")
    period = input("Time period (hour, day, week, month): ")

try:
    feed = QuakeFeed(level, period)
except ValueError as error:
    sys.exit(f"Error: {error}")

dataset = QuakeDataset(feed)
dataset.read_feed()

print(dataset)
if len(dataset) == 0:
    sys.exit()

print(f"Mean depth = {dataset.mean_depth():.2f} km")
print(f"Mean magnitude = {dataset.mean_magnitude():.1f}")

strongest = dataset.strongest_quake()
print()
print(f"Strongest quake occurred at {strongest.when:%H:%M:%S} "
      f"on {strongest.when:%Y-%m-%d}")
print(f"at {strongest.longitude}° longitude, {strongest.latitude}° latitude")
print(f"The depth was {strongest.depth} km")
print(f"The magnitude was {strongest.magnitude}")
