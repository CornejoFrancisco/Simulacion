from scipy.stats import expon, norm

probabilidad = round((expon.cdf(0.2205, scale= 1/5) - (expon.cdf(0.1115, scale= 1/5) )) * 100, 4)
print(probabilidad)
prob = round(((norm.cdf(5.6850, loc=10, scale=2)) - (norm.cdf(5.0869, loc=10, scale=2))) * 200, 4)
print(prob)