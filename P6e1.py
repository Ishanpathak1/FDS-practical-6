from scipy import stats
n=15
N=20
p=0.5
i=stats.binom_test(n,N,p)
print(i)