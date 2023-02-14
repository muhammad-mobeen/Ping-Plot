import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os
import re

def ping_shot(address, size):
    cmd = 'ping -n ' + str(size) + " " + address
    ping_data = os.popen(cmd).read()
    return ping_data

def ping_scraper(ping_data):
    pattern = "time=\d+..."
    scraped_data = re.findall(pattern, ping_data)
    plotter_data = [int(re.search('\d+',x).group()) for x in scraped_data]
    print(ping_data)
    print(scraped_data)
    print(plotter_data)
    return plotter_data

def ping_plotter(plotter_data, attack_size):
    # np.random.seed(10**7)
    n_bins = attack_size//2
    # x = np.random.randn(10000, 3)
    x = np.array(plotter_data)

    plt.hist(x, bins=n_bins)
    plt.gca().set(title='Ping Response Time Histogram', xlabel='Round-Trip Time (ms)', ylabel='Frequency');
    
    # plt.legend(prop ={'size': 10})
    
    # plt.title('matplotlib.pyplot.hist() function Example\n\n',
    #         fontweight ="bold")
    
    plt.show()

if __name__ == '__main__':
    target_address = "google.com"
    attack_size = 50
    ping_data = ping_shot(target_address, attack_size)
    plotter_data = ping_scraper(ping_data)
    ping_plotter(plotter_data, attack_size)