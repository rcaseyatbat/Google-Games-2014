
import sys
# Set up the input and output files
sys.stdin = open('A-small-2-attempt0.in.txt', 'r')
sys.stdout = open('A2sample.out', 'w')
# Read in T
total_cases = int(raw_input())
for case_number in xrange(1, total_cases + 1):
  # Read in C and W
  copies, word = raw_input().split()
  copies = int(copies)
  word = " " + word
  # Output the result
  print 'Case #%d: %s' % (case_number, word * copies)

  