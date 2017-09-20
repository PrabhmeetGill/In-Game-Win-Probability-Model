



time_min = input('Enter game in mintues(0-12): ')
time_sec = input('Enter game in seconds(0-60): ')

point_diff_input = input('Enter the point difference: ')
quarter = input('Enter the quarter (1-4): ')


time2 = time_min + (time_sec/60)
time1 = time(time2, quarter)
point_diff = point_diff_input 

def time(cur_time, period):
	if(period <= 4 ):
		return (cur_time +(12 * (period-1)))/48
	elif(period > 4):
		return (cur_time + 48 + (5*(period - 5))) /(48 + (5*(period-4)))
	one_min = 47.0 / 48.0
#if the game time is less than one minute enter deicision tree, if not use the formula
if(time1 < one_min):

	#created a formula to find the win percentages given the time in game and point difference
	#it is based off a mutltivariable linear regression, using python's mutltipolyfit function
	#it inputs time and point difference and projects a win percentage
	if(point_diff > 0 and time1 < one_min):

		win_percentage_point_diff1 = 50 + ((( 0.88516012 *(point_diff)) + (0.01899752* ((time1))) - 0.25782663) / .357971177776)
		#win_percentage_point_diff1 = (( 0.01899752*(point_diff) + (0.88516012 * (time1)) + -0.25782663 )) + 50 
		#win_percentage_point_diff1 = ( 1.90492871 *(-16) -1.57033168*(time1) ) +50
		print(win_percentage_point_diff1)
	elif(point_diff < 0 and time1 < one_min):
		#multipying by the SD of the data
		win_percentage_point_diff1 =  50 - ((( 0.88516012 *(-point_diff)) + (0.01899752* (time1)) - 0.25782663) / 0.357971177776)
		print(win_percentage_point_diff1)
	elif(point_diff ==0):
		win_percentage_point_diff1 = 50
		print(win_percentage_point_diff1)

elif(time1 >= one_min):
	#creating a simple decision tree for when the game is under a minute and less than a 5 point game
	if(point_diff == 1 ):
		#1 - effective field goal% (chance of making a shot based on NBA year)
		win_percentage_point_diff1 = 51.4
	elif(point_diff == -1 ):
		#effective field goal% (chance of making a shot based on NBA year)
		win_percentage_point_diff1 =  49.6
	elif(point_diff == 2 ):
		#1 - 2 point field goal% (change of making a two based on NBA year)
		win_percentage_point_diff1 =  54.3
	elif(point_diff == -2 ):
		#2 point field goal% (change of making a two based on NBA year)
		win_percentage_point_diff1 =  45.7
	elif(point_diff == 3 ):
		#1 - 3 point field goal% (change of making a three based on NBA year)
		win_percentage_point_diff1 =  64.2
	elif(point_diff == -3 ):
		#3 point field goal% (change of making a three based on NBA year)
		win_percentage_point_diff1 =  35.8
	elif(point_diff == 4):
		#assuming 2 free throws are made, you need two threes to tie. so I took the 3pt field goal% and squared it, since you need to make 2.
		win_percentage_point_diff1 =  87.2
	elif(point_diff == -4 ):
		#assuming 2 free throws are made, you need two threes to tie. so I took the 3pt field goal% and squared it, since you need to make 2.
		win_percentage_point_diff1 =  12.8
	elif(point_diff == 5 ):
		#assuming all free throws are made, you need to make 3 threes to tie. so I took the 3pt field goal% and cubed it, since you need to make 3.
		win_percentage_point_diff1 =  95.42
	elif(point_diff == -5 ):
		#assuming all free throws are made, you need to make 3 threes to tie. so I took the 3pt field goal% and cubed it, since you need to make 3.
		win_percentage_point_diff1 =  4.58	
	elif(point_diff == 6 ):
		#assuming all free throws are made, you need to make 3 threes to tie. so I took the 3pt field goal% and put it to the fourth power since you need to make 3.
		win_percentage_point_diff1 =  98.39
	elif(point_diff == -6 ):
		#assuming all free throws are made, you need to make 3 threes to tie. so I took the 3pt field goal% and put it to the fourth power since you need to make 3.
		win_percentage_point_diff1 =  1.61	
	elif(point_diff > 0):
		win_percentage_point_diff1  = 100
	elif(point_diff < 0):
		win_percentage_point_diff1 = 0
	elif(point_diff == 0):
		win_percentage_point_diff1 = 50	


print(win_percentage_point_diff1)