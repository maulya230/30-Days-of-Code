# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())

for i in range (0,n):    
    s=input()
    print(s[0::2]+" "+s[1::2])
