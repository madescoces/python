from matplotlib import pyplot as plt

# Copyright Pablo Foglia(c)
def print(title,**kwargs):
    color_ = kwargs['color'] if 'color' in kwargs else 'gray'
    size_ = kwargs['size'] if 'size' in kwargs else 16
    
    plt.title(title, color=color_, size=size_ )
    plt.margins(y=0.1, x=0.1) if kwargs['margin']==True else plt.margins(y=0,x=0)
    plt.axis('on' if 'axis' in kwargs and kwargs['axis']==True else 'off')
    plt.show()

def squareText(txt, funct, **kwargss):
    _x = kwargss['x'] if 'x' in kwargss else 0
    _y = kwargss['y'] if 'y' in kwargss else 0
    _size = kwargss['font_size'] if 'font_size' in kwargss else 12

    plt.text(   
                _x, _y, s=txt + str(funct),
                size=_size, 
                ha="left", 
                va="top", 
                bbox=dict(  boxstyle="square",
                            ec=(1.0,0.7,0.5),
                            fc=(1.0,0.9,0.8),   )
            )