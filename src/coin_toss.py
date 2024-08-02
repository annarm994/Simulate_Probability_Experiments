import random
import matplotlib.pyplot as plt

def simulate_coin_tosses(num_tosses):
    heads = 0
    tails = 0
    for _ in range(num_tosses):
        if random.choice(['H', 'T']) == 'H':
            heads += 1
        else:
            tails += 1
    return heads, tails

def plot_coin_tosses(heads, tails):
    labels = ['Heads', 'Tails']
    counts = [heads, tails]
    plt.bar(labels, counts, color=['blue', 'orange'])
    plt.title('Coin Toss Results')
    plt.show()

if __name__ == "__main__":
    heads, tails = simulate_coin_tosses(100)
    print(f"Heads: {heads}, Tails: {tails}")
    plot_coin_tosses(heads, tails)
