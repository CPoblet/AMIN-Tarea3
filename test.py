import subprocess

tau = [1.4, 1.5, 1.6, 1.7, 1.8]
file = 'salida.csv'

open(file, 'w').close()
for t in tau:
    for i in range(30):
        subprocess.run(['py', 'main.py', str(i), '100000', str(t), 'knapPI_1_50_1000.csv', file ])