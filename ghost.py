import sys
# Set up the input and output files
sys.stdin = open('D-small-2-attempt1.in.txt', 'r')
#sys.stdout = open('hammerOutput1.txt', 'w')

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

# Read in T
total_cases = int(raw_input())
for case_number in xrange(1, total_cases + 1):
  totalstring = raw_input()
  #print totalstring

  occur = list(find_all(totalstring, 'G'))
  #print list(find_all(totalstring, 'G'))

  #print totalstring[5:10]
  count = 0

  while (len(occur) != 0):
    found = False;
    for index in occur:
      if totalstring[index:index+5] == 'GHOST':
        #print 'FOUND'
        found = True
        count += 1
        #print totalstring[0:index-1] 
        totalstring = totalstring[0:index] + totalstring[index+5:]
        #print totalstring
        occur = list(find_all(totalstring, 'G'))

        print 'Occur:', occur
    if found == False:
      break
    #if totalstring()
  '''
  pants = int(raw_input())
  #print 'Pants!: ', pants
  cities = {}
  count = 0

  alreadySubbed = []
  for pant in xrange(1, pants + 1):
  	city, color, score = raw_input().split()
  	#print city, color, score
  	if (color, score) in cities.keys():
  		if city == cities[(color, score)]:
  			# we've already counted this one
  			continue
  		else:
  			#continue
  			if (color, score) in alreadySubbed:
  				continue
  			else:
  				#print 'SUBBING'
  				alreadySubbed.append((color, score))
  				count -= 1
  				#print 'Subbed: ', count
  		#del cities[(color, score)]
  	else:
  		count += 1
  		#print 'adding: ', count 
  		#print city, color, score
  		cities[(color, score)] = city
  	#city[(city, color)] = score
  	#if (color, score) not in cities.values():
  		#print 'append'
  		#if city in cities.keys():
  			#cities[city].append(color, score)
  		#else:
  			#cities[city] = (color, score)
	  	#cities[city].append((color, score))
  	#print cities
  #print cities
  #print len(cities)
  # Read in C and W
  #copies, word = raw_input().split()
  #copies = int(copies)
  #word = " " + word
  # Output the result
  '''



  print 'Case #%d: %s' % (case_number, count)