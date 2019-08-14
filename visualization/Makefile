# Generate all plots at once
all:
	make clean && ./barchart && ./regression

# Generate barcharts
barchart:
	./barchart

# Generate regressions
regression:
	./regression

# Remove all plots
clean:
	rm -fr barchart-plots regression-plots __pycache__

# Don't display instructions while running
.SILENT:
	all
	clean
