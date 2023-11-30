flags = -std=c++17 -Wall -Wextra

all: main

main: main.o FastaParser.o FastaSequence.o 
	g++ -o main main.o FastaParser.o FastaSequence.o 

main.o: main.cpp
	g++ -c $(flags) main.cpp

FastaParser.o: FastaParser.cpp FastaParser.h
	g++ -c $(flags) FastaParser.cpp

FastaSequence.o: FastaSequence.cpp FastaSequence.h
	g++ -c $(flags) FastaSequence.cpp

clean:
	rm -f *.o main output.fasta

run: main
	./main input.fasta output.fasta

.PHONY: all clean run
