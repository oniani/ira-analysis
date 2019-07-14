# Run the program
run:
	echo 'Extracting the images...'
	python3 main.py
	echo 'All images have been extracted to the specified directory!'

organized:
	echo 'Extracting the images...'
	python3 main.py --organized=True
	echo 'All images have been extracted to the proper directories!'

# Remove some files
clean:
	echo 'Removing junk...'
	rm -rf __pycache__ extracted

# Don't display instructions while running
.SILENT:
	run
