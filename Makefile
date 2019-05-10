all: build/main.pdf

# hier Python-Skripte:
#build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
#	TEXINPUTS=$$(pwd): python plot.py
build/einzel_mittel.pdf: einzel_mittel.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python einzel_mittel.py

build/einzel_klein.pdf: einzel_klein.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python einzel_klein.py

build/em_fourier.pdf: em_fourier.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python em_fourier.py

build/ek_fourier.pdf: ek_fourier.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python ek_fourier.py
# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/einzel_mittel.pdf  build/einzel_klein.pdf build/em_fourier.pdf build/ek_fourier.pdf

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
