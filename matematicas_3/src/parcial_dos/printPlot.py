from matplotlib import pyplot as plt
from matplotlib.font_manager import font_family_aliases

# Copyright Pablo Foglia(c)
def printPlot( title, fig, **kwargs ):
    color_ = kwargs['color'] if 'color' in kwargs else 'gray'
    size_ = kwargs['size'] if 'size' in kwargs else 16
    totalAxes = fig.axes 

    plt.title(title, color=color_, size=size_)
    for axs in totalAxes : axs.axis('on' if 'axis' in kwargs and kwargs['axis']==True else 'off')
    plt.show()

def squareText(txt, funct, *box, **kwargs):
    _x = kwargs['x'] if 'x' in kwargs else 0
    _y = kwargs['y'] if 'y' in kwargs else 0
    _size = kwargs['size'] if 'size' in kwargs else 12
    
    args = list(e for e in box)
    print(args)
    # Texto por consola
    print(txt + str(funct))
    
    if( 'true' in args ):
        plt.text(   
                    _x, _y, s=txt + str(funct),
                    size= _size,
                    ha= "left", 
                    va= "top",
                    fontname= 'sans-serif' if not 'font_family' in kwargs else kwargs['font_family'], 
                    bbox=dict(  boxstyle="square",
                                ec=(1.0,0.7,0.5),
                                fc=(1.0,0.9,0.8),   )
                )