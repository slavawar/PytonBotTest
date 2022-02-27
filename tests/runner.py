import os

files = filter(lambda x: x.endswith('.py'), os.listdir(os.getcwd()))

for file in files:
    cmd = f"pytest {str(file)}"
    os.system(cmd)