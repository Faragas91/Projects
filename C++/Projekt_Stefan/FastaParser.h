#ifndef FASTA_PARSER_H
#define FASTA_PARSER_H

#include <string>
#include <vector>
#include "FastaSequence.h"

class FastaParser {
public:
    // Funktion zum Einlesen einer Fasta-Datei und Rückgabe einer Liste von Fasta-Sequenzen
    static std::vector<FastaSequence> parseFastaFile(const std::string& filename);

    // Funktion zum Schreiben einer Liste von Fasta-Sequenzen in eine Fasta-Datei
    static void writeFastaFile(const std::vector<FastaSequence>& sequences, const std::string& filename);
};

#endif  // FASTA_PARSER_H
