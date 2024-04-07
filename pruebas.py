from scipy.stats import expon

probabilidad = round((expon.cdf(0.2205, scale= 1/5) - (expon.cdf(0.1115, scale= 1/5) )) * 100, 4)
print(probabilidad)