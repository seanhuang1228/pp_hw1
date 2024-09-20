CXX = g++
CXXFLAGS = -std=c++11 -O3 -pthread -fopenmp

all: hw1

hw1: hw1.cpp
	$(CXX) $(CXXFLAGS) -o hw1 hw1.cpp -lpng

run: hw1
	srun -A ACD113119 -n1 -c8 ./hw1 case/input_1.png out/output_1.png

clean:
	rm -f hw1

.PHONY: all clean

