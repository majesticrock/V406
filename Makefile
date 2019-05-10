all: build/main.pdf

# hier Python-Skripte:
#build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
#	TEXINPUTS=$$(pwd): python plot.py
build/einzel_mittel.pdf: einzel_mittel.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python einzel_mittel.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/einzel_mittel.pdf 

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
