from scipy.stats import t

#Set the t_values and degree of freedom
t_value = 0.22
dof = 24

#Calculate the CDF value
cdf_value = t.cdf(t_value,dof)
print(f"cdf_value:{cdf_value}")