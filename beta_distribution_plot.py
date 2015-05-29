# coding=utf-8
from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np

class beta_distribution(object):
    def __init__(self):
        self.x = (np.linspace(0.001, 0.999,1000))
        self.colors = "bgrcmykw"
        self.colors_index=0
        self.hyperparameter=self.choice_hyperparameter()

    def prior_beta(self,a,b):
        p_x=[]
        for theta in self.x :
            p_x.append(beta.pdf(theta, a, b))
        return p_x

    def plot_bete(self,data,color):
        plt.axis([0, 1, 0,3])
        plt.plot(self.x,data,color,label='a=%s,b=%s'%(self.hyperparameter[0],self.hyperparameter[1]),linewidth=2.0)
        plt.legend(loc='best')

    def show_pic(self):
        plt.grid(True)
        plt.show()
    def plot_single_curve(self,a=1,b=1):
        p_x=self.prior_beta(a,b)
        self.plot_bete(p_x,self.colors[self.colors_index])
        self.show_pic()

    def plot_multi_curve(self):
        for (a,b) in self.hyperparameter:
            p_x=self.prior_beta(a,b)
            self.plot_bete(p_x,self.colors[self.colors_index])
            self.colors_index+=1
        self.show_pic()
        return 0

    def choice_hyperparameter(self):
        return [(5,1),(2,2),(0.5,0.5),(2,2),(2,5)]

#----------------------------------------------------------------
class likehood(object):
    print 'a'
    pass
def main():
    prior_beta=beta_distribution()
    prior_beta.plot_multi_curve()
    prior_beta.plot_single_curve()
if __name__=="__main__":
    main()
