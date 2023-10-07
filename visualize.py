import pandas as pd
import matplotlib.pyplot as plt

def visualize_results(csv_file):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Plot the graph
    plt.plot(df['Num_Embeddings'], df['Speedup'], marker='o')
    plt.title('Speedup vs Num Embeddings')
    plt.xlabel('Num Embeddings')
    plt.ylabel('Speedup (Time taken SqLite/Redis)')
    plt.grid(True)
    plt.savefig('plot.png')

if __name__ == "__main__":
    import sys

    # Get CSV file from command line arguments
    if len(sys.argv) != 2:
        print("Usage: python visualize.py <csv_file>")
        sys.exit(1)

    csv_file = sys.argv[1]

    # Visualize the results
    visualize_results(csv_file)
