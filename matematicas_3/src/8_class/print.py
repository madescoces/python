from matplotlib import pyplot as plt

# Copyright Pablo Foglia(c)
def print(title,**kwargs):
    color_ = kwargs['color'] if 'color' in kwargs else 'gray'
    size_ = kwargs['size'] if 'size' in kwargs else 16
    
    plt.title(title, color=color_, size=size_ )
    plt.margins(y=0.1, x=0.1) if kwargs['margin']==True else plt.margins(y=0,x=0)
    plt.axis('on' if 'axis' in kwargs and kwargs['axis']==True else 'off')
    plt.show()