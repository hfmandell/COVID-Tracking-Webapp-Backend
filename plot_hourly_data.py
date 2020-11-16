import matplotlib.pyplot as plt

data = {"Lincoln": {8: 3, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 15: 6, 16: 10, 17: 5}, 
        "Frary": {8: 0, 9: 1, 10: 3, 11: 6, 12: 1, 13: 1, 15: 7, 16: 10, 17: 10}, 
        "North Seaver": {8: 0, 9: 1, 10: 2, 11: 5, 12: 1, 13: 1, 15: 6, 16: 15, 17: 0}}

def plot_data(data):
    for i,j in data.items():
        x = j.keys()
        y = j.values()

        plt.plot(x,y, label = i)
    plt.legend()
    plt.xlabel("Hours")
    plt.ylabel("Visits")
    plt.title("title")
    plt.savefig("hourly_traffic.png") # saves the graph to a png file  
    # plt.show() # uncomment this to see the graph

plot_data(data)