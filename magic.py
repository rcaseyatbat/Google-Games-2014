import sys
# Set up the input and output files
sys.stdin = open('A-small-practice.in.txt', 'r')
sys.stdout = open('magicOutput.txt', 'w')
# Read in T

total_cases = int(raw_input())



#print total_cases
for case_number in xrange(1, total_cases + 1):
  # Read in C and W
  guess1 = int(raw_input())
  row11, row12, row13, row14 = map(int, raw_input().split())
  row21, row22, row23, row24 = map(int, raw_input().split())
  row31, row32, row33, row34 = map(int, raw_input().split())
  row41, row42, row43, row44 = map(int, raw_input().split())

  guess2 = int(raw_input())
  row51, row52, row53, row54 = map(int, raw_input().split())
  row61, row62, row63, row64 = map(int, raw_input().split())
  row71, row72, row73, row74 = map(int, raw_input().split())
  row81, row82, row83, row84 = map(int, raw_input().split())

  row1 = [row11, row12, row13, row14];
  row2 = [row21, row22, row23, row24];
  row3 = [row31, row32, row33, row34];
  row4 = [row41, row42, row43, row44];
  row5 = [row51, row52, row53, row54];
  row6 = [row61, row62, row63, row64];
  row7 = [row71, row72, row73, row74];
  row8 = [row81, row82, row83, row84];

  allrows = [row1, row2, row3, row4, row5, row6, row7, row8]

  guesses1 = allrows[guess1-1]
  guesses2 = allrows[guess2 + 3]

  totals = guesses1 + guesses2
  #print 'FINAL: ', totals

  frequencies = dict((i,totals.count(i)) for i in totals)

  #print frequencies

  possible = []

  for key in frequencies:
    #print key, 'corresponds to', frequencies[key]
    if frequencies[key] >= 2:
    	possible.append(key)

  #print 'POSSIBLE: ', possible

  if len(possible) == 0:
  	result = 'Volunteer cheated!'
  elif len(possible) == 1:
  	result = str(possible[0])
  else:
  	result = 'Bad magician!'


  #print 'Guess1: %d  Guess2: %d' % (guess1, guess2)
  #print 'Row1: %d %d %d %d' % (row11, row12, row13, row14)
  #print 'Row5: %d %d %d %d' % (row51, row52, row53, row54)
  #copies = int(copies)
  #word = " " + word
  # Output the result
  print 'Case #%d: %s' % (case_number, result)
