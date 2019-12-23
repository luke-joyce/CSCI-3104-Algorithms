def alignStrings(x, y, ins_cost, del_cost, sub_cost):
	DP=[[0 for i in range(len(y)+1)] for j in range(len(x)+1)]
	for i in range(len(x)+1):
		DP[i][0]=i
	for j in range(len(y)+1):
		DP[0][j]=j

	for i in range(1,len(x)+1):
		for j in range(1,len(y)+1):
			if x[i-1]!=y[j-1]:
				DP[i][j]=min (DP[i-1][j-1]+sub_cost, DP[i][j-1]+ins_cost, DP[i-1][j]+del_cost,)
			else:
				DP[i][j]=DP[i-1][j-1]
	return DP


def extractAlignment(S, x, y, ins_cost, del_cost, sub_cost):
	ops=[]
	i=len(x)
	j=len(y)

	while (i>=1 or j>=1):

		ins=S[i][j-1]
		delete=S[i-1][j]
		sub=S[i-1][j-1]
		if min(ins,delete,sub)==S[i][j]:
			i=i-1
			j=j-1
			op=('/')
		elif min(ins,delete,sub)==delete:
			i=i-1
			op=('-')
		elif min(ins,delete,sub)==ins:
			j=j - 1
			op=('+')
		elif min(ins,delete,sub)==sub:
			i=i-1
			j=j-1
			op=('=')
		ops=[op]+ops
	return ops
    

def commonSubstrings(x, L, a):

	substr=''
	subStrings=[]
	place=0

	for inst in a:
		if inst=='/':
			substr=substr+x[place]
		else:
			if len(substr)>=L:
				subStrings.append(substr)
			substr=''
		if inst!='+':
			place=place+1
	if len(substr)>=L:
		subStrings.append(substr)
	return(subStrings) 


x='EXPONENTIAL'
y='POLYNOMIAL'
S=alignStrings(x, y, 2, 1, 2)
for i in S:
	print(i)


song1=open('Song1_Folsom_Prison.txt', 'r').read()
song2=open('Song2_Crescent_City_Blues.txt', 'r').read()

Answer=commonSubstrings(song1, 10, extractAlignment(alignStrings(song1, song2, 1, 1, 1), song1, song2, 1, 1, 1))

for j in Answer:
	print ("Length:",len(j),", Substring:",j)