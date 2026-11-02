# Week 1.6, Session 1: Task 5

from datetime import datetime

from feed import QuakeFeed
from quake import Quake


class QuakeDatasetError(Exception):
    """
    An exception type for errors involving QuakeDataset.
    """


class QuakeDataset:
    """
    An earthquake dataset obtained from a USGS data feed.
    """

    def __init__(self, feed):
        """
        Creates an empty dataset, linked to a specific data feed.
        """
        if not isinstance(feed, QuakeFeed):
            raise TypeError("feed must be specified as a QuakeFeed object")

        self.feed = feed
        self.data = []

    def read_feed(self):
        """
        Refreshes this dataset with data from the linked feed.

        The new data replaces any existing data.
        """
        self.data.clear()

        for info in self.feed.reader():
            # USGS times end in "Z" (UTC); older Pythons' fromisoformat()
            # can't parse that, so swap it for an explicit UTC offset
            when = datetime.fromisoformat(info["time"].replace("Z", "+00:00"))

            quake = Quake(
                when,
                float(info["longitude"]),
                float(info["latitude"]),
                float(info["depth"]),
                float(info["mag"]),
            )
            self.data.append(quake)

    def __len__(self):
        """
        Returns the size of this dataset.
        """
        return len(self.data)

    def __str__(self):
        """
        Returns information on this dataset as a string.
        """
        return f"{len(self.data)} quakes, from {self.feed}"

    def _check_not_empty(self):
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

    def mean_depth(self):
        """
        Returns the mean depth of the quakes in this dataset.
        """
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        total = sum(quake.depth for quake in self.data)
        return total / len(self.data)

    def mean_magnitude(self):
        """
        Returns the mean magnitude of the quakes in this dataset.
        """
        self._check_not_empty()

        total = sum(quake.magnitude for quake in self.data)
        return total / len(self.data)

    def shallowest_quake(self):
        """
        Returns details of the shallowest quake in this dataset.
        """
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        shallowest = self.data[0]
        for quake in self.data[1:]:
            if quake.depth < shallowest.depth:
                shallowest = quake
        return shallowest

    def strongest_quake(self):
        """
        Returns details of the strongest quake in this dataset.
        """
        self._check_not_empty()

        strongest = self.data[0]
        for quake in self.data[1:]:
            if quake.magnitude > strongest.magnitude:
                strongest = quake
        return strongest

    # ---- Optional extra work ----

    def deepest_quake(self):
        """
        Returns details of the deepest quake in this dataset.
        """
        self._check_not_empty()
        return max(self.data, key=lambda quake: quake.depth)

    def weakest_quake(self):
        """
        Returns details of the weakest quake in this dataset.
        """
        self._check_not_empty()
        return min(self.data, key=lambda quake: quake.magnitude)

    def print_table(self, quakes=None):
        """
        Prints details of quakes in a neatly formatted table.

        By default all quakes in the dataset are printed, but a different
        list of quakes can be supplied.
        """
        if quakes is None:
            quakes = self.data

        print(f"{'Date':<10}  {'Time':<8}  {'Longitude':>9}  {'Latitude':>8}"
              f"  {'Depth (km)':>10}  {'Mag':>4}")
        print("-" * 60)
        for quake in quakes:
            print(f"{quake.when:%Y-%m-%d}  {quake.when:%H:%M:%S}"
                  f"  {quake.longitude:9.3f}  {quake.latitude:8.3f}"
                  f"  {quake.depth:10.1f}  {quake.magnitude:4.1f}")

    def quakes_near(self, longitude, latitude, degrees):
        """
        Returns a list of quakes within the given number of degrees of the
        given longitude & latitude.
        """
        nearby = []
        for quake in self.data:
            # Longitude wraps around at +/-180, so take the shorter way round
            dlon = abs(quake.longitude - longitude) % 360
            dlon = min(dlon, 360 - dlon)
            dlat = quake.latitude - latitude
            if (dlon ** 2 + dlat ** 2) ** 0.5 <= degrees:
                nearby.append(quake)
        return nearby

    def print_quakes_near(self, longitude, latitude, degrees):
        """
        Displays all quakes within the given number of degrees of the
        given longitude & latitude.
        """
        nearby = self.quakes_near(longitude, latitude, degrees)
        print(f"{len(nearby)} quakes within {degrees}° of "
              f"({longitude}°, {latitude}°)")
        if nearby:
            self.print_table(nearby)
