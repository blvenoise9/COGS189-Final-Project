import numpy as np
import scipy.io
import os
from pathlib import Path
import pandas as pd

# Define paths to data directories
adhd_part1_path = Path('ADHD_part1')
adhd_part2_path = Path('ADHD_part2')
control_part1_path = Path('Control_part1')
control_part2_path = Path('Control_part2')

def load_mat_files(directory):
    """Load all .mat files from a directory into a dictionary"""
    data_dict = {}
    if not os.path.exists(directory):
        print(f"Directory {directory} not found")
        return data_dict
        
    for file in os.listdir(directory):
        if file.endswith('.mat'):
            file_path = os.path.join(directory, file)
            try:
                # Load the .mat file
                mat_data = scipy.io.loadmat(file_path)
                # Store in dictionary with filename as key
                data_dict[file] = mat_data
                print(f"Successfully loaded {file}")
            except Exception as e:
                print(f"Error loading {file}: {str(e)}")
    return data_dict

def main():
    # Load all data
    print("Loading ADHD group data...")
    adhd_data_part1 = load_mat_files(adhd_part1_path)
    adhd_data_part2 = load_mat_files(adhd_part2_path)

    print("\nLoading Control group data...")
    control_data_part1 = load_mat_files(control_part1_path)
    control_data_part2 = load_mat_files(control_part2_path)

    # Print summary of loaded data
    print(f"\nSummary:")
    print(f"ADHD Part 1: {len(adhd_data_part1)} files loaded")
    print(f"ADHD Part 2: {len(adhd_data_part2)} files loaded")
    print(f"Control Part 1: {len(control_data_part1)} files loaded")
    print(f"Control Part 2: {len(control_data_part2)} files loaded")

    # Examine the structure of one file from each group
    print("\nADHD Group Data Structure:")
    if adhd_data_part1:
        first_file = list(adhd_data_part1.keys())[0]
        first_data = adhd_data_part1[first_file]
        print(f"\nExamining file: {first_file}")
        print("Keys in the .mat file:")
        for key in first_data.keys():
            if not key.startswith('__'):  # Skip MATLAB metadata
                print(f"Key: {key}")
                print(f"Shape: {first_data[key].shape}")

    return {
        'adhd_part1': adhd_data_part1,
        'adhd_part2': adhd_data_part2,
        'control_part1': control_data_part1,
        'control_part2': control_data_part2
    }

if __name__ == "__main__":
    data = main() 