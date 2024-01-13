import random
import matplotlib.pyplot as plt

def scatter_plot():
    x = [random.randrange(0,50) for _ in range(0,500)]
    y = [random.randrange(0,250) for _ in range(0, 500)]
    sizes = [random.randrange(1,450) for _ in range(0, 500)]
    colors = [random.random() for _ in range(0,500)]

    plt.scatter(x, y, alpha=0.7, c=colors, s=sizes, cmap='inferno')


def line_plot():
    x = [i for i in range(20)]
    y = [random.randrange(0,250) for _ in range(0, 20)]
    y2 = [random.randrange(0,100) for _ in range(0,20)]

    plt.xlabel('Time')
    plt.ylabel('Quantity')
    plt.title('Simple Line Plot')

    plt.plot(x,y, c='red', linestyle='--', label='line 1')
    plt.plot(x,y2, c='yellow', linestyle='dashdot', label='line 2')
    plt.legend()

def bar_plot():
    products = ['A', 'B', 'C']
    sales = [150, 200, 120]
    labels = ['Product A', 'Product B', 'Product C']
    colors = ['red', 'blue', 'green']
    widths = [0.5, 0.25, 0.75]

    plt.xlabel('Products')
    plt.ylabel('Sales')
    plt.title('Proudct and Sales')

    for i, value in enumerate(sales):
        plt.text(i, value + 5, str(value), ha='center', va='bottom')

    
    plt.bar(products, sales, color=colors, label=labels, width=widths, edgecolor='#000')
    plt.legend()

def hist_plot():
    scores = [random.randint(1,250) for _ in range(20)]

    plt.hist(scores, bins=10, color='green', alpha=0.8)
    

def sub_plot():
    plt.subplot(2, 2, 1)
    scatter_plot()

    plt.subplot(2, 2, 2)
    bar_plot()

    plt.subplot(2, 1, 2)
    hist_plot()




if __name__ == "__main__":
    sub_plot()
    plt.show()