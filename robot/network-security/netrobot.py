#import commands
import subprocess
import fnmatch
import os,csv
path = '/etc/ansible/playbook/Network-Security'
files = []
files1 = []
files2 = []
files3 = []
for file in os.listdir(path):

    if fnmatch.fnmatch(file, '*.yml'):



        files.append(os.path.join(path, file))

for f in files:
  cmd1 = 'ansible-playbook --syntax-check --list-tasks '+ f
  str1=subprocess.getoutput(cmd1)
  if "ERROR! Syntax Error"  in str1:

     files1.append(f)

  elif "Syntax Error"  in str1:
     files1.append(f)

  elif "ERROR!"  in str1:
     files1.append(f)

  elif "The error appears"  in str1:

     files1.append(f)

  else:

     files2.append(f)

print(files2)

thecsv = csv.writer(open("net.csv", 'w'))
thecsv.writerow(["${filename}"])
for value in files:
    thecsv.writerow([value])
	
	
	
