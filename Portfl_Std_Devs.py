# Code Snippet to see the minimum variance portfolio with 2 securities

import numpy as np
import matplotlib.pyplot as plt


#Function to input the returns of the portfolio
def input_returns(m):
    returns = np.zeros([m,m],dtype=float)
    i=0
    for i in range(n):
        returns[i,i] = float(input(f"Enter the return(%) of asset{i+1}: "))
    
    return returns


#Function to input standard deviation 
def input_StdDev(m):
    StdDev = np.zeros([m,m],dtype=float)
    i=0
    for i in range(n):
        StdDev[i,i] = float(input(f"Enter the standard deviation(%) of asset{i+1}: "))
    
    return StdDev


#Function to input weights of assets in the portfolio 
def input_weights(m):
    weights = np.zeros(m, dtype=float)
    i=0
    total = 0
    for i in range(m):
        weights[i] =  float(input(f"Enter the weight(%) of asset{i+1} in the portfolio: "))
        total += weights[i]
   
    return weights, total
    

#Function to input correlation between assets in the portfolio
def input_correlation_matrix(m):
    correlation_matrix = np.zeros([m,m], dtype=float)
    i=0
    for i in range(m):
        correlation_matrix[i][i] = 1
    i=0
    while i < m:
        j=i+1
        while j<m:
            correlation_matrix[i][j] = float(input(f"Enter the correlation between Asset{i+1} and Asset{j+1}: "))
            if ((correlation_matrix[i][j] <=1) and (correlation_matrix[i][j] >= -1)):
                correlation_matrix[j][i] = correlation_matrix[i][j]
            else:
                print("Error!!! Correlation must range -1 to 1. Please re-enter the correlation")
                j = j-1
            j+=1
            
        i+=1
            
    return correlation_matrix


def portfl_return(m,ret_matrix,wt_matrix):
    i=0
    portfl_ret = 0
    for i in range(m):
        portfl_ret += wt_matrix[i]*ret_matrix[i][i]/100
        
    return portfl_ret
        


########################################################################
#Number of assets
########################################################################

n = 2


########################################################################
#Return(%) of an asset in portfolio
########################################################################

print("\nReturns of each asset in percentage(%): ")
returns_matrix = input_returns(n)


########################################################################
#Stadard deviation of an asset in portfolio
########################################################################

print("\nStandard Deviantion of each asset in percentage(%): ")
StdDev_matrix = input_StdDev(n)
         
        

########################################################################
#Correlation matrix
########################################################################

print("\nCorrelation between various assets in the portfolio: ")
corr_matrix = input_correlation_matrix(n)



########################################################################
#Variance-Covariance matrix
########################################################################

Var_Covar_matrix = StdDev_matrix.dot(corr_matrix).dot(StdDev_matrix)

########################################################################


w1 = 100
w2 = 0
StdDev_portfl = []
return_portfl = []
weight_matrix = np.zeros(n, dtype=float)

while w2!=101:
    weight_matrix[0] = w1
    weight_matrix[1] = w2
    weight_matrix_transpose = weight_matrix.reshape((-1, 1))
    var_portfl = (weight_matrix.dot(Var_Covar_matrix).dot(weight_matrix_transpose))/10000
    StdDev_portfl.append(round(np.sqrt(var_portfl[0]),4))
    return_portfl.append(portfl_return(n, returns_matrix, weight_matrix))
    if w2 == 0:
        msd_ret = return_portfl[0]
        min_std_dev = StdDev_portfl[0]
        msd_wt = [w1,w2]
    elif min_std_dev>StdDev_portfl[w2]:
        msd_ret = return_portfl[w2]
        min_std_dev = StdDev_portfl[w2]
        msd_wt = [w1,w2]
    w2+=1
    w1-=1


plt.plot(StdDev_portfl, return_portfl,color='r')
plt.plot(min_std_dev,msd_ret,'bs')
plt.text(min_std_dev,msd_ret,f" {(min_std_dev,msd_ret)}") 
plt.xlabel('Standard Deviation')
plt.ylabel('Return')
plt.title('Return vs Standard Deviation of Portfolio')
#plt.grid()
plt.savefig('myimage.png', format='png', dpi=1200)
plt.show()






