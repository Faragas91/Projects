#include "FastaParser.h"
#include "Nucleotide.h"

#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <exception>

// Header auslesen und Sequenzen in einer Vektorliste speichern
std::vector<FastaSequence> FastaParser::parseFastaFile(const std::string& filename) {
    std::vector<FastaSequence> sequences;
    std::ifstream inputFile(filename);

    if (!inputFile.is_open()) {
        std::cout << "Error opening file: " << filename << std::endl;
        return sequences;
    }

    std::string line;
    std::string currentHeader;
    FastaSequence* currentSequence = nullptr;
    bool isHeader = true;

    while (std::getline(inputFile, line)) {
        if (line.empty()) {
            continue; // Leere Zeilen überspringen
        }

        if (line[0] == '>' || line[0] == ';') {
            isHeader = true;
            if (currentSequence != nullptr) {
                sequences.push_back(*currentSequence); // Vorherige Sequenz zur Liste hinzufügen
                currentSequence = nullptr;
            }
            if (line[0] == '>') {
                currentHeader += line.substr(1); // Header-Zeile ohne das erste Zeichen (z.B. ">") speichern
            }
            else {
                currentHeader += "\n" + line; // Zeilenumbruch einfügen, wenn der Header mit ";" beginnt
            }
        }
        else {
            if (isHeader == true) {
                currentSequence = new FastaSequence(currentHeader); // Neue Sequenz mit dem aktuellen Header erstellen
                currentHeader = "";
                isHeader = false;
            }
            // Annahme: Die Sequenzelemente sind Nukleotide
            for (char elementCode : line) {
                FastaSequenceElement* element = new Nucleotide(elementCode); // Sequenzelement als Nukleotid erstellen
                currentSequence->addSequenceElement(element); // Sequenzelement zur aktuellen Sequenz hinzufügen
            }
        }
    }

    if (currentSequence != nullptr) {
        sequences.push_back(*currentSequence); // Letzte Sequenz zur Liste hinzufügen
        currentSequence = nullptr;
    }

    inputFile.close();
    return sequences; // Liste der eingelesenen Sequenzen zurückgeben
}

// Fasta-Datei erstellen und Sequenzen in die Datei schreiben
void FastaParser::writeFastaFile(const std::vector<FastaSequence>& sequences, const std::string& filename) {
    std::ofstream outputFile(filename);

    if (!outputFile.is_open()) {
        std::cout << "Error opening file: " << filename << std::endl;
        return;
    }

    for (const FastaSequence& sequence : sequences) {
        outputFile << ">" << sequence.getHeader() << std::endl; // Header-Zeile schreiben
        std::string sequenceString = sequence.getSequence();

        // Sequenz in Blöcken von 80 Zeichen schreiben
        for (size_t i = 0; i < sequenceString.length(); i += 80) {
            outputFile << sequenceString.substr(i, 80) << std::endl;
        }

        outputFile << std::endl; // Leerzeile nach jeder Sequenz
    }

    outputFile.close();
}
