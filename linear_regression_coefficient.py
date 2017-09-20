
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
#print(data.shape)
length = data.shape[0]

score_diff_array_win = []
score_diff_array_loss = []

score_diff_array_all = []

total_nums_games = 1149


x = data.score[1]
#print(x)
x.split
point_diff =  ( ((int(x[5])*10) +  int(x[6])) - (((int(x[0]) *10)+int(x[1])) ))


c = data.play_clock[1]
c.split
game_clock = 12 - ((int(c[0]) * 10.0 ) + (int(c[1])) + 

	(((int(c[3]) *10.0) + (int(c[4]))))/60)


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

		#adds to win or loss array, based of if point difference is negative or positive
		if(point_diff_end > 0 ):
			score_diff_array_win.append(point_diff_begin)

		elif(point_diff_end < 0):
			score_diff_array_loss.append(point_diff_begin)


		if(point_diff_end != 0):
			score_diff_array_all.append(point_diff_begin)



print(np.mean(score_diff_array_win))

print(np.std(score_diff_array_win))

print(statistics.variance(score_diff_array_win))



#histogram of all of the point difference at the start of the quarter in games won
plt.figure('histogram for games won')
bins = np.linspace(-40, 40, 81)

time = np.linspace(0.0, 1.0,75)

plt.hist(score_diff_array_win, bins)
plt.ylabel('point difference')
plt.xlabel('frequency')
plt.show()




win12 =  np.array([    0.,       0.,    0.,    0.,    0.,
          2.,    0.,    0.,    1.,    1.,    2.,    0.,    0.,    0.,
          2.,    3.,    3.,    2.,    5.,   12.,   13.,   18.,    6.,
         22.,   10.,   19.,   18.,   28.,   47.,   54.,   42.,   80.,
         51.,   68.,   94.,   79.,   88.,   88.,  106.,   88.,  103.,
         79.,   79.,   84.,  103.,   92.,  103.,   90.,   74.,   60.,
         61.,   51.,   44.,   51.,   47.,   37.,   29.,   27.,   27.,
         15.,   15.,   19.,   13.,    5.,   13.,    4.,    6.,    2.,
          1.,    2.,    5.,    3.,      2.,    2.,    2.])


point_diff2 = np.array([ -36., -34., -33., -32., -31., -30.,
       -29., -28., -27., -26., -25., -24., -23., -22., -21., -20., -19.,
       -18., -17., -16., -15., -14., -13., -12., -11., -10.,  -9.,  -8.,
        -7.,  -6.,  -5.,  -4.,  -3.,  -2.,  -1.,   0.,   1.,   2.,   3.,
         4.,   5.,   6.,   7.,   8.,   9.,  10.,  11.,  12.,  13.,  14.,
        15.,  16.,  17.,  18.,  19.,  20.,  21.,  22.,  23.,  24.,  25.,
        26.,  27.,  28.,  29.,  30.,  31.,  32.,  33.,  34.,  35., 
        37.,  38.,  39.,  40. ])



#histogram of all of the point difference at the start of the quarter in games lost
plt.figure('histogram for games lost')
plt.hist(score_diff_array_loss,bins)
plt.ylabel('point difference')
plt.xlabel('frequency')
plt.show()


#histogram of all of the point difference at the start of the quarter in all games
plt.figure('histogram for total games')
plt.hist(score_diff_array_all,bins)
plt.ylabel('point difference')
plt.xlabel('frequency')
plt.show()

#print(plt.hist(score_diff_array_all,bins))


total1 =  np.array([   1.,        1.,    1.,    2.,    1.,
          4.,    2.,    5.,    8.,    7.,   11.,    7.,    9.,    7.,
         23.,   27.,   20.,   25.,   30.,   29.,   46.,   60.,   43.,
         64.,   55.,   52.,   80.,  100.,  101.,  147.,  110.,  136.,
        153.,  133.,  153.,  137.,  161.,  125.,  157.,  158.,  149.,
        132.,  121.,  127.,  147.,  126.,  117.,  102.,   91.,   74.,
         68.,   57.,   53.,   55.,   51.,   43.,   31.,   27.,   29.,
         17.,   18.,   19.,   14.,    5.,   13.,    4.,    6.,    2.,
          1.,    2.,    6.,    3.,     2.,    2.,    4.])




#calculating a win percentage for the games won / total games
win_percent_array = [(float(w) / float(t) ) for w,t in zip(win12, total1)]

#print(win_percent_array)

#setting up the matrix for multi variable linear regression

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


#performing multi variable linear regression and graphing it
out, m, b = multipolyfit(xs, win_percent_array, 1, model_out = False)

print(out)
print(m)
print(b)

print(np.mean(win_percent_array))

print(np.std(win_percent_array))

print(statistics.variance(win_percent_array))


plt.figure('linear regression for win percentage')
plt.plot(xs, win_percent_array, '.')
plt.plot(point_diff2, b*(point_diff2) + m*(time) + out, '-')
plt.ylabel('win percentage')
plt.xlabel('point difference')
plt.show()

