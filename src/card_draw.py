import random
import matplotlib.pyplot as plt

def simulate_card_draws(num_draws):
    deck = ['red'] * 26 + ['black'] * 26
    random.shuffle(deck)
    red_count = 0
    black_count = 0
    for _ in range(num_draws):
        card = deck.pop()
        if card == 'red':
            red_count += 1
        else:
            black_count += 1
    return red_count, black_count

def plot_card_draws(red_count, black_count):
    labels = ['Red', 'Black']
    counts = [red_count, black_count]
    plt.bar(labels, counts, color=['red', 'black'])
    plt.title('Card Draw Results')
    plt.show()

if __name__ == "__main__":
    red_count, black_count = simulate_card_draws(20)
    print(f"Red: {red_count}, Black: {black_count}")
    plot_card_draws(red_count, black_count)
