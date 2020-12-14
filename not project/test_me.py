import os.path

# simple version for working with CWD

print(len([name for name in os.listdir('.') if os.path.isfile(name)]))
