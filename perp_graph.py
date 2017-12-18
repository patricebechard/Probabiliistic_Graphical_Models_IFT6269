import numpy as np 
import matplotlib.pyplot as plt 


perp_train_sk = np.loadtxt("perp_train_sklearn.txt")
perp_test_sk = np.loadtxt('perp_test_sklearn.txt')

perp_train_gibbs = np.loadtxt("perp_train_gibbs.txt")
perp_test_gibbs = np.loadtxt("perp_test_gibbs.txt")


num_topics = [i for i in range(2,30,2)]

plt.plot(num_topics, perp_train_sk, 'r', label="Training set (Sklearn)")
plt.plot(num_topics, perp_test_sk, 'r--', label="Test set (Sklearn)")
plt.plot(num_topics, perp_train_gibbs, 'g', label="Training set (Gibbs sampling)")
plt.plot(num_topics, perp_test_gibbs, 'g--', label="Test set (Gibbs sampling)")

plt.xlabel("Number of topics")
plt.ylabel("Perplexity")
plt.legend(fancybox=True, shadow=True)

plt.savefig("perplexity.png")

plt.show()