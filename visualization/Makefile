# Generate barcharts
bar:
	./barchart

# Generate wordclouds
cloud:
	./wordcloud

# Generate regressions
regress:
	./regression

# Generate all plots at once
all:
	make clean && make bar && make regress

# Remove all plots
clean:
	rm -fr barchart-plots regression-plots __pycache__ top25.txt

# Don't display instructions while running
.SILENT:
	all
	barchart
	regression
	wordcloud
	clean
