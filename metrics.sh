#!/bin/bash

# Specify the CSV file to store results
csv_file="test_results.csv"

# Print CSV header
echo "Num_Embeddings,Speedup" > $csv_file

# Set the range of documents you want to test
for doc in 10 50 100 150 200 300 400 500 700 1000; do
    parts=20  # Assuming parts is fixed at 20
    embeddings=$((doc * parts))
    
    echo "Running test for $embeddings embeddings"
    
    # Run your Python script with the specified parameters
    output=$(python run_test.py --documents $doc --parts $parts --words 200)

    # Extract speedup information
    speedup=$(echo "$output" | grep 'Redis Speeeedup' | awk '{print $3}' | sed 's/x$//')

    echo "Speedup for $embeddings embeddings: $speedup"
    
    # Append results to the CSV file
    echo "$embeddings,$speedup" >> $csv_file
done

# Run the visualization script
python visualize.py $csv_file