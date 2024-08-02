import random
import matplotlib.pyplot as plt

def simulate_die_rolls(num_rolls):
    outcomes = [0] * 6
    for _ in range(num_rolls):
        roll = random.randint(1, 6)
        outcomes[roll - 1] += 1
    return outcomes

def plot_die_rolls(outcomes):
    labels = ['1', '2', '3', '4', '5', '6']
    plt.bar(labels, outcomes, color='green')
    plt.title('Die Roll Results')
    plt.show()

if __name__ == "__main__":
    outcomes = simulate_die_rolls(60)
    for i, count in enumerate(outcomes):
        print(f"{i+1}: {count}")
    plot_die_rolls(outcomes)
