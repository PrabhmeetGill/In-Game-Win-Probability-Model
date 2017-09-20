
import pandas
import statistics
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from multipolyfit import multipolyfit, mk_sympy_function
from scipy import linalg


filename = 'pbp.csv'
names = ['sequence_id',	'game_id', 'period', 'play_clock' , 'home_description',	'away_description', 
'score', 'player1_id', 'player1_name', 'player1_team', 'player2_id', 'player2_name', 'player2_team', 'player3_id', 
'player3_name', 'player3_team', 'event_type', 'event_description']
data = pandas.read_csv(filename, names=names)
print(data.shape)
length = data.shape[0]

score_diff_array_win = []
score_diff_array_loss = []
score_diff_array_win11 = []
score_diff_array_loss11 = []
score_diff_array_win10 = []
score_diff_array_loss10 = []
score_diff_array_win9 = []
score_diff_array_loss9 = []
score_diff_array_win8 = []
score_diff_array_loss8 = []
score_diff_array_win7 = []
score_diff_array_loss7 = []
score_diff_array_win6 = []
score_diff_array_loss6 = []
score_diff_array_win5 = []
score_diff_array_loss5 = []
score_diff_array_win4 = []
score_diff_array_loss4 = []
score_diff_array_win3 = []
score_diff_array_loss3 = []
score_diff_array_win2 = []
score_diff_array_loss2 = []
score_diff_array_win1 = []
score_diff_array_loss1 = []

score_diff_array_all = []

total_nums_games = 1149


x = data.score[1]
print(x)
x.split
point_diff =  ( ((int(x[5])*10) +  int(x[6])) - (((int(x[0]) *10)+int(x[1])) ))


c = data.play_clock[1]
c.split
game_clock = 12 - ((int(c[0]) * 10.0 ) + (int(c[1])) + 

	(((int(c[3]) *10.0) + (int(c[4]))))/60)

print(data.play_clock[153] == '0:00')

w =0
l = 0
t12 = False
t11 = False
t10 = False
t9 = False
t8 = False
t7 = False
t6 = False
t5 = False
t4 = False
t3 = False
t2 = False
t1 = False

g11 = False
g10 = False
g9 = False
g8 = False
g7 = False
g6 = False
g5 = False
g4 = False
g3 = False
g2 = False
g1 = False

#this for loop parses the data into 2 categories: win and loss based off the score at the start of the quarter vs. the score at the end of the quarter
#essentially this gives me 3 arrays, one containing the point difference at the start of the quarter in wins, and in losses, 
#and the last array is just the total number of games
for i in range(1, length):
	cur_game = data.game_id[i]
	if(data.play_clock[i] == '12:00'):
		z = data.score[i]
		if(isinstance(z, str) != False):
			#print(len(z))
			z.split
	
			if(len(z) == 7):
				point_diff_begin =  ( ((int(z[5])*10) +  int(z[6])) - (((int(z[0]) *10)+int(z[1])) ))
				t12 = True
				#print(point_diff_begin)
			elif(len(z) == 8 and z[3] == '-' ):
				point_diff_begin =  ( ( (int(z[5]) * 100) + (int(z[6])*10) +  int(z[7])) - (((int(z[0]) *10)+int(z[1])) ))
				t12 = True
				#print(point_diff_begin)
			elif(len(z) == 9):
				point_diff_begin =  ( ( (int(z[6]) * 100) + (int(z[7])*10) +  int(z[8])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t12 = True
				#print(point_diff_begin)
			else:
				point_diff_begin =  ( ((int(z[6])*10) +  int(z[7])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t12 = True
				#print(point_diff_begin)

	elif((data.play_clock[i] == '11:00' or  data.play_clock[i] == '10:59' or data.play_clock[i] == '10:58' 
		or data.play_clock[i] == '10:57' or data.play_clock[i] == '10:56' or data.play_clock[i] == '10:55') and g11 == False):
		z = data.score[i]
		if(isinstance(z, str) != False):
			#print(len(z))
			z.split
	
			if(len(z) == 7):
				point_diff_11 =  ( ((int(z[5])*10) +  int(z[6])) - (((int(z[0]) *10)+int(z[1])) ))
				t11 = True
				#print(point_diff_begin)
			elif(len(z) == 8 and z[3] == '-' ):
				point_diff_11 =  ( ( (int(z[5]) * 100) + (int(z[6])*10) +  int(z[7])) - (((int(z[0]) *10)+int(z[1])) ))
				t11 = True
				#print(point_diff_begin)
			elif(len(z) == 9):
				point_diff_11 =  ( ( (int(z[6]) * 100) + (int(z[7])*10) +  int(z[8])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t11 = True
				#print(point_diff_begin)
			else:
				point_diff_11 =  ( ((int(z[6])*10) +  int(z[7])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t11 = True
				#print(point_diff_begin)
			g11 = True



	elif(g10 == False and (data.play_clock[i] == '10:00' or  data.play_clock[i] == '9:59' or data.play_clock[i] == '9:58' 
		or data.play_clock[i] == '9:57' or data.play_clock[i] == '9:56' or data.play_clock[i] == '9:55')):
		z = data.score[i]
		if(isinstance(z, str) != False):
			#print(len(z))
			z.split
	
			if(len(z) == 7):
				point_diff_10 =  ( ((int(z[5])*10) +  int(z[6])) - (((int(z[0]) *10)+int(z[1])) ))
				t10 = True
				#print(point_diff_begin)
			elif(len(z) == 8 and z[3] == '-' ):
				point_diff_10 =  ( ( (int(z[5]) * 100) + (int(z[6])*10) +  int(z[7])) - (((int(z[0]) *10)+int(z[1])) ))
				t10 = True
				#print(point_diff_begin)
			elif(len(z) == 9):
				point_diff_10 =  ( ( (int(z[6]) * 100) + (int(z[7])*10) +  int(z[8])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t10 = True
				#print(point_diff_begin)
			else:
				point_diff_10 =  ( ((int(z[6])*10) +  int(z[7])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t10 = True
				#print(point_diff_begin)
			g10 = True		

	elif(data.play_clock[i] == '9:00'):
		z = data.score[i]
		if(isinstance(z, str) != False):
			#print(len(z))
			z.split
	
			if(len(z) == 7):
				point_diff_9 =  ( ((int(z[5])*10) +  int(z[6])) - (((int(z[0]) *10)+int(z[1])) ))
				t9 = True
				#print(point_diff_begin)
			elif(len(z) == 8 and z[3] == '-' ):
				point_diff_9 =  ( ( (int(z[5]) * 100) + (int(z[6])*10) +  int(z[7])) - (((int(z[0]) *10)+int(z[1])) ))
				t9 = True
				#print(point_diff_begin)
			elif(len(z) == 9):
				point_diff_9 =  ( ( (int(z[6]) * 100) + (int(z[7])*10) +  int(z[8])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t9 = True
				#print(point_diff_begin)
			else:
				point_diff_9 =  ( ((int(z[6])*10) +  int(z[7])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t9 = True
				#print(point_diff_begin)	


	elif(data.play_clock[i] == '8:00'):
		z = data.score[i]
		if(isinstance(z, str) != False):
			#print(len(z))
			z.split
	
			if(len(z) == 7):
				point_diff_8 =  ( ((int(z[5])*10) +  int(z[6])) - (((int(z[0]) *10)+int(z[1])) ))
				t8 = True
				#print(point_diff_begin)
			elif(len(z) == 8 and z[3] == '-' ):
				point_diff_8 =  ( ( (int(z[5]) * 100) + (int(z[6])*10) +  int(z[7])) - (((int(z[0]) *10)+int(z[1])) ))
				t8 = True
				#print(point_diff_begin)
			elif(len(z) == 9):
				point_diff_8 =  ( ( (int(z[6]) * 100) + (int(z[7])*10) +  int(z[8])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t8 = True
				#print(point_diff_begin)
			else:
				point_diff_8 =  ( ((int(z[6])*10) +  int(z[7])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t8 = True
				#print(point_diff_begin)

	elif(data.play_clock[i] == '7:00'):
		z = data.score[i]
		if(isinstance(z, str) != False):
			#print(len(z))
			z.split
	
			if(len(z) == 7):
				point_diff_7 =  ( ((int(z[5])*10) +  int(z[6])) - (((int(z[0]) *10)+int(z[1])) ))
				t7 = True
				#print(point_diff_begin)
			elif(len(z) == 8 and z[3] == '-' ):
				point_diff_7 =  ( ( (int(z[5]) * 100) + (int(z[6])*10) +  int(z[7])) - (((int(z[0]) *10)+int(z[1])) ))
				t7 = True
				#print(point_diff_begin)
			elif(len(z) == 9):
				point_diff_7 =  ( ( (int(z[6]) * 100) + (int(z[7])*10) +  int(z[8])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t7 = True
				#print(point_diff_begin)
			else:
				point_diff_7 =  ( ((int(z[6])*10) +  int(z[7])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t7 = True
				#print(point_diff_begin)


	elif(data.play_clock[i] == '6:00'):
		z = data.score[i]
		if(isinstance(z, str) != False):
			#print(len(z))
			z.split
	
			if(len(z) == 7):
				point_diff_6 =  ( ((int(z[5])*10) +  int(z[6])) - (((int(z[0]) *10)+int(z[1])) ))
				t6 = True
				#print(point_diff_begin)
			elif(len(z) == 8 and z[3] == '-' ):
				point_diff_6 =  ( ( (int(z[5]) * 100) + (int(z[6])*10) +  int(z[7])) - (((int(z[0]) *10)+int(z[1])) ))
				t6 = True
				#print(point_diff_begin)
			elif(len(z) == 9):
				point_diff_6 =  ( ( (int(z[6]) * 100) + (int(z[7])*10) +  int(z[8])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t6 = True
				#print(point_diff_begin)
			else:
				point_diff_6 =  ( ((int(z[6])*10) +  int(z[7])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t6 = True
				#print(point_diff_begin)



	elif(data.play_clock[i] == '5:00'):
		z = data.score[i]
		if(isinstance(z, str) != False):
			#print(len(z))
			z.split
	
			if(len(z) == 7):
				point_diff_5 =  ( ((int(z[5])*10) +  int(z[6])) - (((int(z[0]) *10)+int(z[1])) ))
				t5 = True
				#print(point_diff_begin)
			elif(len(z) == 8 and z[3] == '-' ):
				point_diff_5 =  ( ( (int(z[5]) * 100) + (int(z[6])*10) +  int(z[7])) - (((int(z[0]) *10)+int(z[1])) ))
				t5 = True
				#print(point_diff_begin)
			elif(len(z) == 9):
				point_diff_5 =  ( ( (int(z[6]) * 100) + (int(z[7])*10) +  int(z[8])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t5 = True
				#print(point_diff_begin)
			else:
				point_diff_5 =  ( ((int(z[6])*10) +  int(z[7])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t5 = True
				#print(point_diff_begin)


	elif(data.play_clock[i] == '4:00'):
		z = data.score[i]
		if(isinstance(z, str) != False):
			#print(len(z))
			z.split
	
			if(len(z) == 7):
				point_diff_4 =  ( ((int(z[5])*10) +  int(z[6])) - (((int(z[0]) *10)+int(z[1])) ))
				t4 = True
				#print(point_diff_begin)
			elif(len(z) == 8 and z[3] == '-' ):
				point_diff_4 =  ( ( (int(z[5]) * 100) + (int(z[6])*10) +  int(z[7])) - (((int(z[0]) *10)+int(z[1])) ))
				t4 = True
				#print(point_diff_begin)
			elif(len(z) == 9):
				point_diff_4 =  ( ( (int(z[6]) * 100) + (int(z[7])*10) +  int(z[8])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t4 = True
				#print(point_diff_begin)
			else:
				point_diff_4 =  ( ((int(z[6])*10) +  int(z[7])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t4 = True
				#print(point_diff_begin)


	elif(data.play_clock[i] == '3:00'):
		z = data.score[i]
		if(isinstance(z, str) != False):
			#print(len(z))
			z.split
	
			if(len(z) == 7):
				point_diff_3 =  ( ((int(z[5])*10) +  int(z[6])) - (((int(z[0]) *10)+int(z[1])) ))
				t3 = True
				#print(point_diff_begin)
			elif(len(z) == 8 and z[3] == '-' ):
				point_diff_3 =  ( ( (int(z[5]) * 100) + (int(z[6])*10) +  int(z[7])) - (((int(z[0]) *10)+int(z[1])) ))
				t3 = True
				#print(point_diff_begin)
			elif(len(z) == 9):
				point_diff_3 =  ( ( (int(z[6]) * 100) + (int(z[7])*10) +  int(z[8])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t3 = True
				#print(point_diff_begin)
			else:
				point_diff_3 =  ( ((int(z[6])*10) +  int(z[7])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t3 = True
				#print(point_diff_begin)

	elif(data.play_clock[i] == '2:00'):
		z = data.score[i]
		if(isinstance(z, str) != False):
			#print(len(z))
			z.split
	
			if(len(z) == 7):
				point_diff_2 =  ( ((int(z[5])*10) +  int(z[6])) - (((int(z[0]) *10)+int(z[1])) ))
				t2 = True
				#print(point_diff_begin)
			elif(len(z) == 8 and z[3] == '-' ):
				point_diff_2 =  ( ( (int(z[5]) * 100) + (int(z[6])*10) +  int(z[7])) - (((int(z[0]) *10)+int(z[1])) ))
				t2 = True
				#print(point_diff_begin)
			elif(len(z) == 9):
				point_diff_2 =  ( ( (int(z[6]) * 100) + (int(z[7])*10) +  int(z[8])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t2 = True
				#print(point_diff_begin)
			else:
				point_diff_4 =  ( ((int(z[6])*10) +  int(z[7])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t2 = True
				#print(point_diff_begin)


	elif(data.play_clock[i] == '1:00'):
		z = data.score[i]
		if(isinstance(z, str) != False):
			#print(len(z))
			z.split
	
			if(len(z) == 7):
				point_diff_1 =  ( ((int(z[5])*10) +  int(z[6])) - (((int(z[0]) *10)+int(z[1])) ))
				t1 = True
				#print(point_diff_begin)
			elif(len(z) == 8 and z[3] == '-' ):
				point_diff_1 =  ( ( (int(z[5]) * 100) + (int(z[6])*10) +  int(z[7])) - (((int(z[0]) *10)+int(z[1])) ))
				t1 = True
				#print(point_diff_begin)
			elif(len(z) == 9):
				point_diff_1 =  ( ( (int(z[6]) * 100) + (int(z[7])*10) +  int(z[8])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t1 = True
				#print(point_diff_begin)
			else:
				point_diff_1 =  ( ((int(z[6])*10) +  int(z[7])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				t1 = True
				#print(point_diff_begin)			



	elif(data.play_clock[i] == '0:00'):
		z = data.score[i]
		if(isinstance(z, str) != False):
			#print(z)
			z.split

			if(len(z) == 7):
				point_diff_end =  ( ((int(z[5])*10) +  int(z[6])) - (((int(z[0]) *10)+int(z[1])) ))
				#print(point_diff)
			elif(len(z) == 8 and z[3] == '-'):
				point_diff_end =  ( ( (int(z[5]) * 100) + (int(z[6])*10) +  int(z[7])) - (((int(z[0]) *10)+int(z[1])) ))
				#print(point_diff)
			elif(len(z) == 9):
				point_diff_end =  ( ( (int(z[6]) * 100) + (int(z[7])*10) +  int(z[8])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				#print(point_diff)
			else:
				point_diff_end =  ( ((int(z[6])*10) +  int(z[7])) - (((int(z[0]) *100)+ (int(z[1])) * 10) + int(z[2]) ))
				#print(point_diff)

			if(point_diff_end == 0):
				continue


		if(point_diff_end > 0 and t12 == True):
			score_diff_array_win.append(point_diff_begin)
			t12 = False

		elif(point_diff_end < 0 and t12 == True):
			score_diff_array_loss.append(point_diff_begin)
			t12 = False

		if(point_diff_end > 0 and t11 == True):
			score_diff_array_win11.append(point_diff_11)
			t11 = False

		elif(point_diff_end < 0 and t11 == True):
			score_diff_array_loss11.append(point_diff_11)
			t11 = False
			#print(point_diff_end)

		if(point_diff_end > 0 and t10 == True):
			score_diff_array_win10.append(point_diff_10)
			t10 = False

		elif(point_diff_end < 0 and t10 == True):
			score_diff_array_loss10.append(point_diff_10)
			t10 = False
			#print(point_diff_end)

		if(point_diff_end > 0 and t9 == True):
			score_diff_array_win9.append(point_diff_9)
			t9 = False

		elif(point_diff_end < 0 and t9 == True):
			score_diff_array_loss9.append(point_diff_9)
			t9 = False
			#print(point_diff_end)

		if(point_diff_end > 0 and t8 == True):
			score_diff_array_win8.append(point_diff_8)
			t8 = False

		elif(point_diff_end < 0 and t8 == True):
			score_diff_array_loss8.append(point_diff_8)
			t8 = False
			#print(point_diff_end)

		if(point_diff_end > 0 and t7 == True):
			score_diff_array_win7.append(point_diff_7)
			t7 = False

		elif(point_diff_end < 0 and t7 == True):
			score_diff_array_loss7.append(point_diff_7)
			t7 = False
			#print(point_diff_end)

		if(point_diff_end > 0 and t6 == True):
			score_diff_array_win6.append(point_diff_6)
			t6 = False

		elif(point_diff_end < 0 and t6 == True):
			score_diff_array_loss6.append(point_diff_6)
			t6 = False
			#print(point_diff_end)

		if(point_diff_end > 0 and t5 == True):
			score_diff_array_win5.append(point_diff_5)
			t5 = False

		elif(point_diff_end < 0 and t5 == True):
			score_diff_array_loss5.append(point_diff_5)
			t5 = False
			#print(point_diff_end)


		if(point_diff_end > 0 and t4 == True):
			score_diff_array_win4.append(point_diff_4)
			t4 = False

		elif(point_diff_end < 0 and t4 == True):
			score_diff_array_loss4.append(point_diff_4)
			t4 = False
			#print(point_diff_end)

		if(point_diff_end > 0 and t3 == True):
			score_diff_array_win3.append(point_diff_3)
			t3 = False

		elif(point_diff_end < 0 and t3 == True):
			score_diff_array_loss3.append(point_diff_3)
			t3 = False
			#print(point_diff_end)

		if(point_diff_end > 0 and t2 == True):
			score_diff_array_win2.append(point_diff_2)
			t2 = False

		elif(point_diff_end < 0 and t2 == True):
			score_diff_array_loss2.append(point_diff_2)
			t2 = False
			#print(point_diff_end)

		if(point_diff_end > 0 and t1 == True):
			score_diff_array_win1.append(point_diff_1)
			t1 = False

		elif(point_diff_end < 0 and t1 == True):
			score_diff_array_loss1.append(point_diff_1)
			t1 = False
			#print(point_diff_end)




		if(point_diff_end != 0):
			score_diff_array_all.append(point_diff_begin)


#print(score_diff_array_win)
#regr = linear_model.LinearRegression()

print(np.mean(score_diff_array_win))

print(np.std(score_diff_array_win))

print(statistics.variance(score_diff_array_win))



print(np.mean(score_diff_array_loss))

print(np.std(score_diff_array_loss))

print(statistics.variance(score_diff_array_loss))


one = np.ones(len(score_diff_array_win))

print(score_diff_array_win11)
print(score_diff_array_win10)

plt.figure(1)
bins = np.linspace(-40, 40, 81)

time = np.linspace(0.0, 1.0,75)

plt.hist(score_diff_array_win, bins)
print(plt.hist(score_diff_array_win,bins))
#print(plt.hist(score_diff_array_win10,bins))
#print(plt.hist(score_diff_array_win11,bins))
#print(plt.hist(score_diff_array_win1,bins))




#win1 = plt.hist(score_diff_array_win,bins)

win12 =  np.array([    0.,       0.,    0.,    0.,    0.,
          2.,    0.,    0.,    1.,    1.,    2.,    0.,    0.,    0.,
          2.,    3.,    3.,    2.,    5.,   12.,   13.,   18.,    6.,
         22.,   10.,   19.,   18.,   28.,   47.,   54.,   42.,   80.,
         51.,   68.,   94.,   79.,   88.,   88.,  106.,   88.,  103.,
         79.,   79.,   84.,  103.,   92.,  103.,   90.,   74.,   60.,
         61.,   51.,   44.,   51.,   47.,   37.,   29.,   27.,   27.,
         15.,   15.,   19.,   13.,    5.,   13.,    4.,    6.,    2.,
          1.,    2.,    5.,    3.,      2.,    2.,    2.])

win11 = np.array([  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.,  0.,  0.,  1.,  0.,  0.,  1.,  1.,  1.,
        1.,  1.,  1.,  3.,  1.,  1.,  2.,  1.,  2.,  1.,  0.,  2.,  2.,
        1.,  3.,  1.,  0.,  1.,  0.,  1.,  1.,  1.,  2.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,   0.,
        0.,  0.])

win10 = np.array([   0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        1.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  1.,  1.,  1.,  1.,  1.,
        1.,  1.,  0.,  2.,  4.,  1.,  2.,  3.,  1.,  2.,  1.,  3.,  2.,
        1.,  3.,  1.,  1.,  3.,  0.,  2.,  1.,  1.,  0.,  0.,  2.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,
        0.,  0.])

win9 = np.array([   0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  1.,
        0.,  0.,  0.,  1.,  3.,  1.,  0.,  0.,  0.,  1.,  1.,  0.,  0.,
        3.,  2.,  2.,  1.,  3.,  2.,  2.,  0.,  0.,  3.,  3.,  1.,  2.,
        2.,  1.,  0.,  2.,  3.,  3.,  1.,  3.,  2.,  1.,  1.,  0.,  2.,
        0.,  0.,  0.,  1.,  0.,  1.,  1.,  0.,  0.,  0.,  0.,   0.,
        0.,  0.])

win8 = np.array([   0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        2.,  0.,  1.,  1.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  1.,  0.,
        2.,  0.,  1.,  1.,  4.,  1.,  0.,  1.,  1.,  2.,  1.,  5.,  0.,
        0.,  1.,  1.,  0.,  1.,  1.,  2.,  0.,  2.,  0.,  0.,  3.,  0.,
        1.,  0.,  2.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  1.])

win7 = np.array([   0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,
        1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  1.,  1.,  1.,  3.,
        3.,  4.,  1.,  1.,  1.,  3.,  0.,  1.,  2.,  1.,  3.,  0.,  2.,
        1.,  0.,  2.,  1.,  2.,  1.,  1.,  2.,  0.,  1.,  0.,  0.,  1.,
        0.,  2.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  1.,  1.,  1., 
        0.,  0.])

win6 = np.array([  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,
        0.,  1.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,  1.,  4.,  1.,  3.,
        0.,  2.,  3.,  0.,  1.,  3.,  0.,  1.,  1.,  1.,  1.,  1.,  2.,
        4.,  2.,  2.,  0.,  2.,  1.,  1.,  3.,  2.,  1.,  2.,  1.,  0.,
        0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,   0.,
        0.,  0.])

win5 = np.array([     0.,   0.,   0.,   0.,   0.,   0.,   0.,
         0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
         1.,   0.,   0.,   0.,   0.,   1.,   0.,   1.,   0.,   0.,   0.,
         0.,   0.,   0.,   1.,   1.,   2.,   4.,  82.,   0.,   3.,   3.,
         2.,   0.,   2.,   3.,   2.,   2.,   3.,   0.,   0.,   1.,   1.,
         0.,   0.,   1.,   1.,   1.,   2.,   2.,   0.,   1.,   1.,   1.,
         0.,   0.,   1.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
         0.,   0.,   0.])

win4 = np.array([   0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,
        2.,  3.,  0.,  2.,  3.,  1.,  0.,  5.,  3.,  0.,  2.,  1.,  2.,
        3.,  1.,  0.,  2.,  0.,  0.,  0.,  1.,  0.,  1.,  2.,  1.,  1.,
        0.,  1.,  2.,  1.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,
        0.,  2.])

win3 = np.array([   0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  1.,  2.,
        2.,  3.,  2.,  2.,  2.,  2.,  4.,  1.,  0.,  3.,  0.,  2.,  1.,
        1.,  0.,  2.,  2.,  4.,  2.,  1.,  1.,  0.,  1.,  1.,  0.,  0.,
        0.,  1.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,
        1.,  0.])

win2 = np.array([   0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,  2.,  3.,  1.,  0.,
        3.,  3.,  7.,  5.,  3.,  1.,  8.,  3.,  4.,  1.,  1.,  3.,  2.,
        1.,  3.,  5.,  3.,  2.,  4.,  3.,  4.,  1.,  1.,  0.,  2.,  0.,
        1.,  3.,  0.,  1.,  2.,  0.,  0.,  0.,  0.,  0.,  0.,   1.,
        1.,  0.])

win1 = np.array([  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  1.,  2.,  0.,  0.,  0.,  1.,  3.,
        3.,  1.,  1.,  2.,  2.,  1.,  3.,  3.,  1.,  2.,  3.,  3.,  3.,
        3.,  1.,  2.,  0.,  1.,  3.,  0.,  0.,  3.,  1.,  1.,  1.,  0.,
        0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,    0.,
        0.,  0.])



print(time)
point_diff2 = np.array([ -36., -34., -33., -32., -31., -30.,
       -29., -28., -27., -26., -25., -24., -23., -22., -21., -20., -19.,
       -18., -17., -16., -15., -14., -13., -12., -11., -10.,  -9.,  -8.,
        -7.,  -6.,  -5.,  -4.,  -3.,  -2.,  -1.,   0.,   1.,   2.,   3.,
         4.,   5.,   6.,   7.,   8.,   9.,  10.,  11.,  12.,  13.,  14.,
        15.,  16.,  17.,  18.,  19.,  20.,  21.,  22.,  23.,  24.,  25.,
        26.,  27.,  28.,  29.,  30.,  31.,  32.,  33.,  34.,  35., 
        37.,  38.,  39.,  40. ])


plt.show()



plt.figure(2)
plt.hist(score_diff_array_loss,bins)
plt.show()



plt.figure(3)
plt.hist(score_diff_array_all,bins)
print(plt.hist(score_diff_array_all,bins))

#total1 = plt.hist(score_diff_array_all,bins)

total1 =  np.array([   1.,        1.,    1.,    2.,    1.,
          4.,    2.,    5.,    8.,    7.,   11.,    7.,    9.,    7.,
         23.,   27.,   20.,   25.,   30.,   29.,   46.,   60.,   43.,
         64.,   55.,   52.,   80.,  100.,  101.,  147.,  110.,  136.,
        153.,  133.,  153.,  137.,  161.,  125.,  157.,  158.,  149.,
        132.,  121.,  127.,  147.,  126.,  117.,  102.,   91.,   74.,
         68.,   57.,   53.,   55.,   51.,   43.,   31.,   27.,   29.,
         17.,   18.,   19.,   14.,    5.,   13.,    4.,    6.,    2.,
          1.,    2.,    6.,    3.,     2.,    2.,    4.])



plt.show()

win_percent_array = [(float(w) / float(t) ) for w,t in zip(win12, total1)]
win_percent_array11 = [float(w) / float(t) for w,t in zip(win11, total1)]
win_percent_array10 = [float(w) / float(t) for w,t in zip(win10, total1)]
win_percent_array9 = [float(w) / float(t) for w,t in zip(win9, total1)]
win_percent_array8 = [float(w) / float(t) for w,t in zip(win8, total1)]
win_percent_array7 = [float(w) / float(t) for w,t in zip(win7, total1)]
win_percent_array6 = [float(w) / float(t) for w,t in zip(win6, total1)]
win_percent_array5 = [float(w) / float(t) for w,t in zip(win5, total1)]
win_percent_array4 = [float(w) / float(t) for w,t in zip(win4, total1)]
win_percent_array3 = [float(w) / float(t) for w,t in zip(win3, total1)]
win_percent_array2 = [float(w) / float(t) for w,t in zip(win2, total1)]
win_percent_array1 = [float(w) / float(t) for w,t in zip(win1, total1)]

print(win_percent_array)

xs = ([ -36., -34., -33., -32., -31., -30.,
       -29., -28., -27., -26., -25., -24., -23., -22., -21., -20., -19.,
       -18., -17., -16., -15., -14., -13., -12., -11., -10.,  -9.,  -8.,
        -7.,  -6.,  -5.,  -4.,  -3.,  -2.,  -1.,   0.,   1.,   2.,   3.,
         4.,   5.,   6.,   7.,   8.,   9.,  10.,  11.,  12.,  13.,  14.,
        15.,  16.,  17.,  18.,  19.,  20.,  21.,  22.,  23.,  24.,  25.,
        26.,  27.,  28.,  29.,  30.,  31.,  32.,  33.,  34.,  35., 
        37.,  38.,  39.,  40. ]),   ([( 12.+(12*3))/48,  (11.83783784+(12*3))/48, (11.67567568+(12*3))/48 , (11.51351351+(12*3))/48 , (11.35135135+(12*3))/48,
  (11.18918919+(12*3))/48,  (11.02702703+(12*3))/48,  (10.86486486+(12*3))/48, ( 10.7027027+(12*3))/48,   (10.54054054+(12*3))/48,
  (10.37837838+(12*3))/48,  (10.21621622+(12*3))/48,  (10.05405405+(12*3))/48,  ( 9.89189189+(12*3))/48,  ( 9.72972973+(12*3))/48,
  ( 9.56756757+(12*3))/48,  ( 9.40540541+(12*3))/48,  ( 9.24324324+(12*3))/48,  ( 9.08108108+(12*3))/48,  ( 8.91891892+(12*3))/48,
  ( 8.75675676+(12*3))/48,  ( 8.59459459+(12*3))/48,  ( 8.43243243+(12*3))/48,  ( 8.27027027+(12*3))/48,  ( 8.10810811+(12*3))/48,
  ( 7.94594595+(12*3))/48,  ( 7.78378378+(12*3))/48,  ( 7.62162162+(12*3))/48,  ( 7.45945946+(12*3))/48, (  7.2972973+(12*3))/48,
  ( 7.13513514+(12*3))/48,  ( 6.97297297+(12*3))/48,  ( 6.81081081+(12*3))/48,  ( 6.64864865+(12*3))/48,  ( 6.48648649+(12*3))/48,
  ( 6.32432432+(12*3))/48,  ( 6.16216216+(12*3))/48,   (6. +(12*3))/48        , ( 5.83783784+(12*3))/48,  ( 5.67567568+(12*3))/48,
  ( 5.51351351+(12*3))/48,  ( 5.35135135+(12*3))/48,  ( 5.18918919+(12*3))/48,  ( 5.02702703+(12*3))/48,  ( 4.86486486+(12*3))/48,
 (  4.7027027+(12*3))/48 ,  ( 4.54054054+(12*3))/48,  ( 4.37837838+(12*3))/48,  ( 4.21621622+(12*3))/48,  ( 4.05405405+(12*3))/48,
  ( 3.89189189+(12*3))/48,  ( 3.72972973+(12*3))/48,  ( 3.56756757+(12*3))/48,  ( 3.40540541+(12*3))/48,  ( 3.24324324+(12*3))/48,
  ( 3.08108108+(12*3))/48,  ( 2.91891892+(12*3))/48,  ( 2.75675676+(12*3))/48,  ( 2.59459459+(12*3))/48,  ( 2.43243243+(12*3))/48,
  ( 2.27027027+(12*3))/48,  ( 2.10810811+(12*3))/48,  ( 1.94594595+(12*3))/48,  ( 1.78378378+(12*3))/48,  ( 1.62162162+(12*3))/48,
  ( 1.45945946+(12*3))/48, (  1.2972973+(12*3))/48 ,  ( 1.13513514+(12*3))/48,  ( 0.97297297+(12*3))/48,  ( 0.81081081+(12*3))/48,
  ( 0.64864865+(12*3))/48,  ( 0.48648649+(12*3))/48,  ( 0.32432432+(12*3))/48,  ( 0.16216216+(12*3))/48,   0.        ])
xs = zip(*xs)




time1 = ([( 12.+(12*3))/48,  (11.83783784+(12*3))/48, (11.67567568+(12*3))/48 , (11.51351351+(12*3))/48 , (11.35135135+(12*3))/48,
  (11.18918919+(12*3))/48,  (11.02702703+(12*3))/48,  (10.86486486+(12*3))/48, ( 10.7027027+(12*3))/48,   (10.54054054+(12*3))/48,
  (10.37837838+(12*3))/48,  (10.21621622+(12*3))/48,  (10.05405405+(12*3))/48,  ( 9.89189189+(12*3))/48,  ( 9.72972973+(12*3))/48,
  ( 9.56756757+(12*3))/48,  ( 9.40540541+(12*3))/48,  ( 9.24324324+(12*3))/48,  ( 9.08108108+(12*3))/48,  ( 8.91891892+(12*3))/48,
  ( 8.75675676+(12*3))/48,  ( 8.59459459+(12*3))/48,  ( 8.43243243+(12*3))/48,  ( 8.27027027+(12*3))/48,  ( 8.10810811+(12*3))/48,
  ( 7.94594595+(12*3))/48,  ( 7.78378378+(12*3))/48,  ( 7.62162162+(12*3))/48,  ( 7.45945946+(12*3))/48, (  7.2972973+(12*3))/48,
  ( 7.13513514+(12*3))/48,  ( 6.97297297+(12*3))/48,  ( 6.81081081+(12*3))/48,  ( 6.64864865+(12*3))/48,  ( 6.48648649+(12*3))/48,
  ( 6.32432432+(12*3))/48,  ( 6.16216216+(12*3))/48,   (6. +(12*3))/48        , ( 5.83783784+(12*3))/48,  ( 5.67567568+(12*3))/48,
  ( 5.51351351+(12*3))/48,  ( 5.35135135+(12*3))/48,  ( 5.18918919+(12*3))/48,  ( 5.02702703+(12*3))/48,  ( 4.86486486+(12*3))/48,
 (  4.7027027+(12*3))/48 ,  ( 4.54054054+(12*3))/48,  ( 4.37837838+(12*3))/48,  ( 4.21621622+(12*3))/48,  ( 4.05405405+(12*3))/48,
  ( 3.89189189+(12*3))/48,  ( 3.72972973+(12*3))/48,  ( 3.56756757+(12*3))/48,  ( 3.40540541+(12*3))/48,  ( 3.24324324+(12*3))/48,
  ( 3.08108108+(12*3))/48,  ( 2.91891892+(12*3))/48,  ( 2.75675676+(12*3))/48,  ( 2.59459459+(12*3))/48,  ( 2.43243243+(12*3))/48,
  ( 2.27027027+(12*3))/48,  ( 2.10810811+(12*3))/48,  ( 1.94594595+(12*3))/48,  ( 1.78378378+(12*3))/48,  ( 1.62162162+(12*3))/48,
  ( 1.45945946+(12*3))/48, (  1.2972973+(12*3))/48 ,  ( 1.13513514+(12*3))/48,  ( 0.97297297+(12*3))/48,  ( 0.81081081+(12*3))/48,
  ( 0.64864865+(12*3))/48,  ( 0.48648649+(12*3))/48,  ( 0.32432432+(12*3))/48,  ( 0.16216216+(12*3))/48,   0.        ])
#win_percent_array = win1/total2,win2/total2

#plt.figure(4)
#plt.scatter(win_percent_array, point_diff2)
#plt.show()

out, m, b = multipolyfit(xs, win_percent_array, 1, model_out = False)

print(out)
print(m)
print(b)

print(np.mean(win_percent_array))

print(np.std(win_percent_array))

print(statistics.variance(win_percent_array))


plt.figure(4)
plt.plot(xs, win_percent_array, '.')
#plt.plot(point_diff2, m*point_diff2**2 + b*time+ out, '-')s
plt.plot(point_diff2, b*(point_diff2) + m*(time) + out, '-')
plt.show()



m, b = np.polyfit(point_diff2, win_percent_array, 1)
print(m)
print(b)

print(out)


plt.figure(5)
plt.plot(point_diff2, win_percent_array, '.')
plt.plot(point_diff2, m*point_diff2 + b, '-')
plt.show()

m, b = np.polyfit(point_diff2, win_percent_array5, 1)
print(m)
print(b)



plt.figure(6)
plt.plot(point_diff2, win_percent_array5, '.')
plt.plot(point_diff2, m*point_diff2 + b, '-')
plt.show()

print(len(point_diff2))
print(len(win_percent_array))

