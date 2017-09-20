# Load CSV using Pandas
import pandas
import matplotlib.pyplot as plt
import numpy as np

filename = 'pbp.csv'
names = ['sequence_id',	'game_id', 'period', 'play_clock' , 'home_description',	'away_description', 
'score', 'player1_id', 'player1_name', 'player1_team', 'player2_id', 'player2_name', 'player2_team', 'player3_id', 
'player3_name', 'player3_team', 'event_type', 'event_description']
data = pandas.read_csv(filename, names=names)
#print(data.shape)
length = data.shape[0]

#values based off of basketball reference 2016-2017 season as a percent http://www.basketball-reference.com/leagues/NBA_stats.html
def_rebound = .767
off_rebound = .233
twopt_field_goal = .457
threept_field_goal = .358
turnover = .127
free_throw = .772
effective_field_goal = .514

#helper function to calculate the time variable in eqaution
def time(cur_time, period):
	if(period <= 4 ):
		return (cur_time +(12 * (period-1)))/48
	elif(period > 4):
		return (cur_time + 48 + (5*(period - 5))) /(48 + (5*(period-4)))


x = data.score[403]
#2661
#403
#154
#277
#154
#909
#1598
print(x)
x.split
point_diff =  ( ((int(x[5])*10) +  int(x[6])) - (((int(x[0]) *10)+int(x[1])) ))

c = data.play_clock[1]
c.split
game_clock = 12 - ((int(c[0]) * 10.0 ) + (int(c[1])) + (((int(c[3]) *10.0) + (int(c[4]))))/60)


#print(game_clock)

print(point_diff)
win_percentage = 50.0

time1 = time(game_clock, int (data.period[1] ))
#print(time1)



one_min = 47.0 / 48.0
#if the game time is less than one minute enter deicision tree, if not use the formula
if(time1 < one_min):


	#created a formula to find the win percentages given the time in game and point difference
	#it is based off a mutltivariable linear regression, using python's mutltipolyfit function
	#it inputs time and point difference and projects a win percentage
	if(point_diff > 0 and time1 < one_min):

		win_percentage_point_diff1 = 50 + ((( 0.88516012 *(point_diff)) + (0.01899752* ((time1))) - 0.25782663) / .357971177776)

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



#MEAN = 0.546591808933
#SD = 0.357971177776
#VAR = 0.129875031201

#linear regression values: [-0.25782663  0.01899752  0.88516012]


win_percentage1 = win_percentage_point_diff1

win_percentage_array = []
win_percentage_array.append(win_percentage1)

cur_game = data.game_id[403]


for i in range(403, length):
	if(cur_game != data.game_id[i]):
		break


	z = data.score[i]

	#simple formula to find the point difference at all time instances of the data
	if(isinstance(z, str) != False ):
		#print(z)
		z.split
		if(len(z) == 7):
			point_diff =  abs( ((int(z[5])*10) +  int(z[6])) - (((int(z[0]) *10)+int(z[1])) ))
			point_diff_real = ( ((int(z[5])*10) +  int(z[6])) - (((int(z[0]) *10)+int(z[1])) ))
			print(point_diff_real)
		elif(len(z) == 8 and z[3] == '-'):
			point_diff =  abs( ( (int(z[5]) * 100) + (int(z[6])*10) +  int(z[7])) - (((int(z[0]) *10)+int(z[1])) ))
			point_diff_real = ( ( (int(z[5]) * 100) + (int(z[6])*10) +  int(z[7])) - (((int(z[0]) *10)+int(z[1])) ))
			print(point_diff_real)
		elif(len(z) == 9):
			point_diff =  abs( ( (int(z[6]) * 100) + (int(z[7])*10) +  int(z[8])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
			point_diff_real = ( ( (int(z[6]) * 100) + (int(z[7])*10) +  int(z[8])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
			print(point_diff_real)
		else:
			point_diff =  abs( ((int(z[6])*10) +  int(z[7])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
			point_diff_real = ( ((int(z[6])*10) +  int(z[7])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
			print(point_diff_real)


	#simple formula to parse the game clock into a usable integer
	c = data.play_clock[i]
	c.split
	if(c[1] != ':'):
		game_clock = 12 - ((int(c[0]) * 10.0 ) + (int(c[1])) + (((int(c[3]) *10.0) + (int(c[4]) )))/60.0)
		#print(game_clock)
	else:
		game_clock = 12 -  ( (int(c[0])) + (((int(c[2]) *10.0) + (int(c[3]) )))/60.0)
		#print(game_clock)

	
	#avoding a divide by 0
	if(point_diff == 0):
		point_diff = 1
	
	#formula to increase/ decrease win percentage based on current point diff, the time, and the NBA's average effective field goal percentage
	if(data.event_type[i] == 'Made Shot '):
		time1 = time(game_clock, int (data.period[i] ))
		if(isinstance(data.home_description[i], str) == True ):
			#home team
			if(time1 < one_min):
				win_percentage1 += ((time1 * (effective_field_goal)) / point_diff)*10
			elif(time1 >= one_min):
				win_percentage1 += ((time1 * (effective_field_goal)) / point_diff)*20

			if(point_diff_real > 0 and win_percentage1 > 50):
				win_percentage_array.append(win_percentage1)
				print(win_percentage1)
			elif(point_diff_real < 0 and win_percentage1 < 50):
				win_percentage_array.append(win_percentage1)
				print(win_percentage1)
			elif(point_diff_real == 0):
				win_percentage_array.append(win_percentage1)
				win_percentage1 = 50
				print(win_percentage1)
			else:
				#this is to counteract an issue that I was having with games that included a large comeback and a lead change
				if(point_diff_real > 0):
					win_percentage1 = 50 + ((( 0.88516012 *(point_diff)) + (0.01899752* ((time1))) - 0.25782663) / .357971177776)
					win_percentage_array.append(win_percentage1)
					print(win_percentage1)	

				elif(point_diff_real < 0):
					win_percentage1 =  50 - ((( 0.88516012 *(point_diff)) + (0.01899752* ((time1))) - 0.25782663) / 0.357971177776)
					win_percentage_array.append(win_percentage1)
					print(win_percentage1)	



		else:
			#away team
			if(time1 < one_min):
				win_percentage1-= ((time1 * (effective_field_goal)) / point_diff)*10
			elif(time1 >= one_min):
				win_percentage1-= ((time1 * (effective_field_goal)) / point_diff)*10
	
	

			if(point_diff_real > 0 and win_percentage1 > 50):
				win_percentage_array.append(win_percentage1)
				print(win_percentage1)
			elif(point_diff_real < 0 and win_percentage1 < 50):
				win_percentage_array.append(win_percentage1)
				print(win_percentage1)
			elif(point_diff_real == 0):
				win_percentage_array.append(win_percentage1)
				win_percentage1 = 50
				print(win_percentage1)
			else:
				#this is to counteract an issue that I was having with games that included a large comeback and a lead change
				if(point_diff_real > 0):
					win_percentage1 = 50 + ((( 0.88516012 *(point_diff)) + (0.01899752* ((time1))) - 0.25782663) / .357971177776)
					win_percentage_array.append(win_percentage1)
					print(win_percentage1)	

				elif(point_diff_real < 0):
					win_percentage1 =  50 - ((( 0.88516012 *(point_diff)) + (0.01899752* ((time1))) - 0.25782663) / 0.357971177776)
					win_percentage_array.append(win_percentage1)
					print(win_percentage1)		
	
	#formula to increase/ decreaase win percentage based on current point diff, the time, and the inverse of NBA's average effective field goal percentage
	elif(data.event_type[i] == 'Missed Shot '):
		time1 = time(game_clock,  int (data.period[i] ))
		if(isinstance(data.home_description[i], str) == True ):
			#home team
			if(time1 < one_min):
				win_percentage1 -= ((time1 * (1- effective_field_goal)) / point_diff)*10
			else:
				win_percentage1 -= ((time1 * (1- effective_field_goal)) / point_diff)*20
			if(point_diff_real > 0 and win_percentage1 > 50):
				win_percentage_array.append(win_percentage1)
				print(win_percentage1)
			elif(point_diff_real < 0 and win_percentage1 < 50):
				win_percentage_array.append(win_percentage1)
				print(win_percentage1)
			elif(point_diff_real == 0):
				win_percentage_array.append(win_percentage1)
				win_percentage1 = 50
				print(win_percentage1)
			else:
				#this is to counteract an issue that I was having with games that included a large comeback and a lead change
				if(point_diff_real > 0):
					win_percentage1 = 50 + ((( 0.88516012 *(point_diff)) + (0.01899752* ((time1))) - 0.25782663) / .357971177776)
					win_percentage_array.append(win_percentage1)
					print(win_percentage1)	

				elif(point_diff_real < 0):
					win_percentage1 =  50 - ((( 0.88516012 *(point_diff)) + (0.01899752* ((time1))) - 0.25782663) / 0.357971177776)
					win_percentage_array.append(win_percentage1)
					print(win_percentage1)	


		else:
			#away team
			if(time1 < one_min):
				win_percentage1 += ((time1 * (1-effective_field_goal)) / point_diff)*10
			else:
				win_percentage1 += ((time1 * (1-effective_field_goal)) / point_diff)*20
			if(point_diff_real > 0 and win_percentage1 > 50):
				win_percentage_array.append(win_percentage1)
				print(win_percentage1)
			elif(point_diff_real < 0 and win_percentage1 < 50):
				win_percentage_array.append(win_percentage1)
				print(win_percentage1)
			elif(point_diff_real == 0):
				win_percentage_array.append(win_percentage1)
				win_percentage1 = 50
				print(win_percentage1)
			else:
				#this is to counteract an issue that I was having with games that included a large comeback and a lead change
				if(point_diff_real > 0):
					win_percentage1 = 50 + ((( 0.88516012 *(point_diff)) + (0.01899752* ((time1))) - 0.25782663) / .357971177776)
					win_percentage_array.append(win_percentage1)
					print(win_percentage1)	

				elif(point_diff_real < 0):
					win_percentage1 =  50 - ((( 0.88516012 *(point_diff)) + (0.0189975 *((time1))) - 0.25782663) / 0.357971177776)
					win_percentage_array.append(win_percentage1)
					print(win_percentage1)	

	#formula to increase/ decrease win percentage based on current point diff, the time, and the NBA's average defensive rebounding percentage
	elif(data.event_type[i] == 'Rebound '):
		time1 = time(game_clock,  int (data.period[i] ))
		if(isinstance(data.home_description[i], str) == True ):
			#home team
			if(time1 < one_min):
				win_percentage1 += ((time1 * (1-def_rebound)) / point_diff)*10
			else:
				win_percentage1 += ((time1 * (1-def_rebound)) / point_diff)*20	
			if(point_diff_real > 0 and win_percentage1 > 50):
				win_percentage_array.append(win_percentage1)
				print(win_percentage1)
			elif(point_diff_real < 0 and win_percentage1 < 50):
				win_percentage_array.append(win_percentage1)
				print(win_percentage1)
			elif(point_diff_real == 0):
				win_percentage_array.append(win_percentage1)
				win_percentage1 = 50
				print(win_percentage1)
			else:
				#this is to counteract an issue that I was having with games that included a large comeback and a lead change
				if(point_diff_real > 0):
					win_percentage1 = 50 + ((( 0.88516012 *(point_diff)) + (0.01899752* ((time1))) - 0.25782663) / .357971177776)
					win_percentage_array.append(win_percentage1)
					print(win_percentage1)	

				elif(point_diff_real < 0):
						#multipying by the SD of the data
					win_percentage1 =  50 - ((( 0.88516012 *(point_diff)) + (0.01899752* ((time1))) - 0.25782663) / 0.357971177776)
					win_percentage_array.append(win_percentage1)
					print(win_percentage1)	


		else:
			#away team
			if(time1 < one_min):
				win_percentage1 -= ((time1 * ( 1-def_rebound)) / point_diff)*10
			else:
				win_percentage1 -= ((time1 * ( 1-def_rebound)) / point_diff)*20
			if(point_diff_real > 0 and win_percentage1 > 50):
				win_percentage_array.append(win_percentage1)
				print(win_percentage1)
			elif(point_diff_real < 0 and win_percentage1 < 50):
				win_percentage_array.append(win_percentage1)
				print(win_percentage1)
			elif(point_diff_real == 0):
				win_percentage_array.append(win_percentage1)
				win_percentage1 = 50
				print(win_percentage1)
			else:
				#this is to counteract an issue that I was having with games that included a large comeback and a lead change
				if(point_diff_real > 0):
					win_percentage1 = 50 + ((( 0.88516012 *(point_diff)) + (0.01899752* ((time1))) - 0.25782663) / .357971177776)
					win_percentage_array.append(win_percentage1)
					print(win_percentage1)	

				elif(point_diff_real < 0):
					win_percentage1 =  50 - ((( 0.88516012 *(point_diff)) + (0.01899752* ((time1))) - 0.25782663) / 0.357971177776)
					win_percentage_array.append(win_percentage1)
					print(win_percentage1)	

	#formula to increase/ decrease win percentage based on current point diff, the time, and the NBA's average turnover percentage
	elif(data.event_type[i] == 'Turnover '):
		time1 = time(game_clock,  int (data.period[i] ))
		if(isinstance(data.home_description[i], str) == True ):
			if(time1 < one_min):
				win_percentage1 -= ((time1 * (1- turnover)) / point_diff)*10
			else:
				win_percentage1 -= ((time1 * ( 1- turnover)) / point_diff)*20
			if(point_diff_real > 0 and win_percentage1 > 50):
				win_percentage_array.append(win_percentage1)
				print(win_percentage1)
			elif(point_diff_real < 0 and win_percentage1 < 50):
				win_percentage_array.append(win_percentage1)
				print(win_percentage1)
			elif(point_diff_real == 0):
				win_percentage_array.append(win_percentage1)
				win_percentage1 = 50
				print(win_percentage1)
			else:
				#this is to counteract an issue that I was having with games that included a large comeback and a lead change
				if(point_diff_real > 0):
					win_percentage1 = 50 + ((( 0.88516012 *(point_diff)) + (0.01899752* ((time1))) - 0.25782663) / .357971177776)
					win_percentage_array.append(win_percentage1)
					print(win_percentage1)	

				elif(point_diff_real < 0):
						#multipying by the SD of the data
					win_percentage1 =  50 - ((( 0.88516012 *(point_diff)) + (0.01899752* ((time1))) - 0.25782663) / 0.357971177776)
					win_percentage_array.append(win_percentage1)
					print(win_percentage1)	


		else:
			if(time1 < one_min):
				win_percentage1 += ((time1 * ( 1-turnover)) / point_diff)*10
			else:
				win_percentage1 += ((time1 * ( 1-turnover)) / point_diff)*20
			if(point_diff_real > 0 and win_percentage1 > 50):
				win_percentage_array.append(win_percentage1)
				print(win_percentage1)
			elif(point_diff_real < 0 and win_percentage1 < 50):
				win_percentage_array.append(win_percentage1)
				print(win_percentage1)
			elif(point_diff_real == 0):
				win_percentage_array.append(win_percentage1)
				win_percentage1 = 50
				print(win_percentage1)
			else:
				#this is to counteract an issue that I was having with games that included a large comeback and a lead change
				if(point_diff_real > 0):
					win_percentage1 = 50 + ((( 0.88516012 *(point_diff)) + (0.01899752* ((time1))) - 0.25782663) / .357971177776)
					win_percentage_array.append(win_percentage1)
					print(win_percentage1)	

				elif(point_diff_real < 0):
						#multipying by the SD of the data
					win_percentage1 =  50 - ((( 0.88516012 *(point_diff)) + (0.01899752* ((time1))) - 0.25782663) / 0.357971177776)
					win_percentage_array.append(win_percentage1)
					print(win_percentage1)	


	#formula to increase/ decrease win percentage based on current point diff, the time, and the NBA's average free throw percentage
	elif(data.event_type[i] == 'Free Throw '):
		time1 = time(game_clock,  int (data.period[i] ))
		#no change if missed free throw
		if(isinstance(data.home_description[i], str) == True and data.home_description[i].find("MISS") == -1 ):
			#home team
			if(one_min < time1):
				win_percentage1 += ((time1 * (1- free_throw)) / point_diff)*10
			else:
				win_percentage1 += ((time1 * (1- free_throw)) / point_diff)*20
			if(point_diff_real > 0 and win_percentage1 > 50):
				win_percentage_array.append(win_percentage1)
				print(win_percentage1)
			elif(point_diff_real < 0 and win_percentage1 < 50):
				win_percentage_array.append(win_percentage1)
				print(win_percentage1)
			elif(point_diff_real == 0):
				win_percentage_array.append(win_percentage1)
				win_percentage1 = 50
				print(win_percentage1)
			else:
				#this is to counteract an issue that I was having with games that included a large comeback and a lead change
				if(point_diff_real > 0):
					win_percentage1 = 50 + ((( 0.88516012 *(point_diff)) + (0.01899752* ((time1))) - 0.25782663) / .357971177776)
					win_percentage_array.append(win_percentage1)
					print(win_percentage1)	

				elif(point_diff_real < 0):
						#multipying by the SD of the data
					win_percentage1 =  50 - ((( 0.88516012 *(point_diff)) + (0.01899752* ((time1))) - 0.25782663) / 0.357971177776)
					win_percentage_array.append(win_percentage1)
					print(win_percentage1)	

		#no change if missed free throw
		elif(isinstance(data.away_description[i], str) == True and data.away_description[i].find('MISS') == -1):
			#away team
			if(one_min < time1):
				win_percentage1 -= ((time1 * (1- free_throw)) / point_diff)*10
			else:
				win_percentage1 -= ((time1 * (1- free_throw)) / point_diff)*20
			if(point_diff_real > 0 and win_percentage1 > 50):
				win_percentage_array.append(win_percentage1)
				print(win_percentage1)
			elif(point_diff_real < 0 and win_percentage1 < 50):
				win_percentage_array.append(win_percentage1)
				print(win_percentage1)
			elif(point_diff_real == 0):
				win_percentage_array.append(win_percentage1)
				win_percentage1 = 50
				print(win_percentage1)
			else:
				#this is to counteract an issue that I was having with games that included a large comeback and a lead change
				if(point_diff_real > 0):
					win_percentage1 = 50 + ((( 0.88516012 *(point_diff)) + (0.01899752* ((time1))) - 0.25782663) / .357971177776)
					win_percentage_array.append(win_percentage1)
					print(win_percentage1)	

				elif(point_diff_real < 0):
					win_percentage1 =  50 - ((( 0.88516012 *(point_diff)) + (0.01899752* ((time1))) - 0.25782663) / 0.357971177776)
					win_percentage_array.append(win_percentage1)
					print(win_percentage1)	


#adding last point for win or loss
if(point_diff_real > 0 ):
	win_percentage_array.append(100)
else:
	win_percentage_array.append(0)

#graphing the win_percent data points
print(len(win_percentage_array))

x = np.linspace(0, len(win_percentage_array), len(win_percentage_array))
 

plt.figure('in game win percentage graph')
plt.plot(x , win_percentage_array, '.')
plt.plot(x , win_percentage_array, '-')
plt.ylabel('win percentage')
plt.show()
