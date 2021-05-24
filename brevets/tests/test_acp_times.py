import arrow
from acp_times import open_time, close_time
#https://rusa.org/cgi-bin/octime.pl

testData = [[0, 0],[100, 200],[250, 400],[500, 600],[750, 1000], [1000, 1000], [1200, 1000], [360, 300]]
openOutput = ["2020-01-01 00:00:00+00:00", "2020-01-01 02:56:00+00:00", "2020-01-01 07:27:00+00:00", "2020-01-01 15:28:00+00:00", "2020-01-02 00:09:00+00:00", "2020-01-02 09:05:00+00:00", "2020-01-02 09:05:00+00:00", "2020-01-01 09:00:00+00:00"]
closeOutput = ["2020-01-01 01:00:00+00:00", "2020-01-01 06:40:00+00:00", "2020-01-01 16:40:00+00:00", "2020-01-02 09:20:00+00:00", "2020-01-03 05:08:00+00:00", "2020-01-04 03:00:00+00:00", "2020-01-04 03:00:00+00:00", "2020-01-01 20:00:00+00:00"]


def test_open_time():
	for i in range(0, len(testData)):
		sarrow = arrow.get("2020-01-01T00:00:00+00:00")
		testVal = open_time(testData[i][0], testData[i][1], sarrow)
		assert testVal.format() == openOutput[i]

def test_close_time():
	for i in range(0, len(testData)):
		sarrow = arrow.get("2020-01-01T00:00:00+00:00")
		testVal = close_time(testData[i][0], testData[i][1], sarrow)
		assert testVal.format() == closeOutput[i]
