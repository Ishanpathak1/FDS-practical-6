from scipy import stats
n=1
N=3
p=0.2
i=stats.binom_test(n,N,p)
print(i)