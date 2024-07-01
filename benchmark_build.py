#!/usr/bin/env python3

import os
import subprocess
import time
import csv
import platform

# Define paths and parameters
output_dir = os.path.expanduser("~/Documents/Benchmark_tests")
compilation_output_file = os.path.join(output_dir, "benchmark_compilation.csv")
trials = 3  # Number of trials

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Identify the current running kernel
kernel = platform.release()

def run_compilation_benchmark(project_path):
    start_time = time.time()
    subprocess.run(["make", "clean"], cwd=project_path, check=True)
    subprocess.run(["make", "-j4"], cwd=project_path, check=True)  # Adjust -j4 based on your CPU cores
    end_time = time.time()
    return end_time - start_time

def save_to_csv(file_path, kernel, benchmark_type, times):
    file_exists = os.path.isfile(file_path)
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Kernel", "Trial", benchmark_type])
        for i, time in enumerate(times, 1):
            writer.writerow([kernel, i, time])

def main():
    project_path = "path/to/ocaml"  # Update with the actual path
    compilation_times = []
    
    for _ in range(trials):
        compilation_times.append(run_compilation_benchmark(project_path))
    
    save_to_csv(compilation_output_file, kernel, "Compilation Time", compilation_times)
    print("Benchmarking completed.")

if __name__ == "__main__":
    main()

