"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#
speedData = [[0, 15, 34], [200, 15, 32], [400, 15, 30], [600, 11.428, 28]]
totalBrevetException = [[200, 810, 353], [300, 1200, 540], [400, 1620, 728], [600, 2400, 1128], [1000, 4500, 1985]]

def calculate(control_dist_km, brevet_dist_km, open):
	timeDiff = 0
	pastDistance = 0
	index = 2 if open else 1

	if control_dist_km > brevet_dist_km * 1.2 or control_dist_km < 0:
		return 0 

	if control_dist_km >= brevet_dist_km:
		for i in range(0, len(totalBrevetException)):
			if brevet_dist_km == totalBrevetException[i][0]:
				return totalBrevetException[i][index]

	if not open and control_dist_km < 60:
		return round((control_dist_km / 20 * 60) + 60)

	for i in range(len(speedData)-1, -1, -1):
		if control_dist_km > speedData[i][0]:
			speed = speedData[i][index]
			tempDist = control_dist_km - pastDistance - speedData[i][0]
			pastDistance += tempDist
			timeDiff += (tempDist / speed) * 60

	return round(timeDiff)

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
	"""
	Args:
	   control_dist_km:  number, control distance in kilometers
	   brevet_dist_km: number, nominal distance of the brevet
		   in kilometers, which must be one of 200, 300, 400, 600,
		   or 1000 (the only official ACP brevet distances)
	   brevet_start_time:  A date object (arrow)
	Returns:
	   A date object indicating the control open time.
	   This will be in the same time zone as the brevet start time.
	"""
	time = calculate(control_dist_km, brevet_dist_km, True)
	brevet_start_time = brevet_start_time.shift(minutes=(time % 60))
	brevet_start_time = brevet_start_time.shift(hours=(time // 60))
	return brevet_start_time


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
	"""
	Args:
	   control_dist_km:  number, control distance in kilometers
		  brevet_dist_km: number, nominal distance of the brevet
		  in kilometers, which must be one of 200, 300, 400, 600, or 1000
		  (the only official ACP brevet distances)
	   brevet_start_time:  A date object (arrow)
	Returns:
	   A date object indicating the control close time.
	   This will be in the same time zone as the brevet start time.
	"""
	time = calculate(control_dist_km, brevet_dist_km, False)

	brevet_start_time = brevet_start_time.shift(minutes=(time % 60))
	brevet_start_time = brevet_start_time.shift(hours=(time // 60))
	return brevet_start_time
