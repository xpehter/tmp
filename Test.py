import subprocess

command = ['git']
exec_command = subprocess.Popen(command, stdout=subprocess.PIPE)
# data = exec_command.communicate()
# print(data)

# for line in data:
#     print(line)

# for line in exec_command.stdout:
#     print(">>> " + str(line.rstrip()))
#     exec_command.stdout.flush()

for line in iter(exec_command.stdout.readline(), b''):
    print(">>> " + line.rstrip())

print('Test')