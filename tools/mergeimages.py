import subprocess

# Command to execute
file1 = 3
file2 = 4
for file in range(3,80):
	args = f"{file1}.png {file2}.png"
	file1 += 2
	file2 += 2
	command = f"magick convert +append {args} a{file1}.png"
	subprocess.run(command, shell=True)

# mogrify -crop 438x540+252+9 -path ./test *.png
# use this to crop the images