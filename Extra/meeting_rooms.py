#__author__ = ritvikareddy2
#__date__ = 2019-02-15

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def minMeetingRooms(intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    start_times = []
    end_times = []
    for interval in intervals:
        start_times.append(interval.start)
        end_times.append(interval.end)

    start_times.sort()
    end_times.sort()

    count = 0
    s, e = 0, 0

    while s < len(start_times):

        if start_times[s] >= end_times[e]:
            e += 1
            count -= 1

        s += 1
        count += 1



    return count


if __name__ == '__main__':
    input = [[13, 15], [1, 13], [6, 9]]
    intervals = [Interval(i[0], i[1]) for i in input]
    print(minMeetingRooms(intervals))