import fnmatch, os, shutil

with open("filename.txt") as file:
	    lines = [line.rstrip() for line in file]

for f in os.listdir('.'):
    if any(fnmatch.fnmatch(f, pat+'*') for pat in calls):
        shutil.move(f, 'NDFCalls')