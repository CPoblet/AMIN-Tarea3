import subprocess
import sys

tau = [1.3, 1.4, 1.5, 1.6, 1.7]
input_file = sys.argv[1]
output_file = sys.argv[2]
""" input_file = ['knapPI_1_50_1000.csv', 'knapPI_1_50_100000.csv', 'knapPI_11_20_1000.csv']
output_file = ['salida_small.csv', 'salida_large.csv', 'salida_hard.csv'] """

open(output_file, 'w').close()
for t in tau:
    for i in range(30):
        subprocess.run(['py', 'main.py', str(i), '100000', str(t), input_file, output_file ])