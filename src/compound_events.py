import random
import matplotlib.pyplot as plt

def simulate_compound_events(num_flips):
    both_heads = 0
    at_least_one_head = 0
    for _ in range(num_flips):
        flip1 = random.choice(['H', 'T'])
        flip2 = random.choice(['H', 'T'])
        if flip1 == 'H' and flip2 == 'H':
            both_heads += 1
        if flip1 == 'H' or flip2 == 'H':
            at_least_one_head += 1
    return both_heads, at_least_one_head

def plot_compound_events(both_heads, at_least_one_head):
    labels = ['Both Heads', 'At Least One Head']
    counts = [both_heads, at_least_one_head]
    plt.bar(labels, counts, color=['purple', 'cyan'])
    plt.title('Compound Events Results')
    plt.show()

if __name__ == "__main__":
    both_heads, at_least_one_head = simulate_compound_events(50)
    print(f"Both Heads: {both_heads}, At Least One Head: {at_least_one_head}")
    plot_compound_events(both_heads, at_least_one_head)
