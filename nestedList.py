#printing second lowest score HackerRank Problem.
num = int(input())
marksheet = [[input(), float(input())] for _ in range(num)]

scondScore = sorted(list(set([marks for name, marks in marksheet])))[1]

print('\n'.join([a for a,b in sorted(marksheet) if b == scondScore]))


#print(scondScore)