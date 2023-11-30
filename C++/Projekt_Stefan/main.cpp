#include <iostream>
#include <fstream>
#include <cmath>
#include "FastaParser.h"
#include "AminoAcid.h"

// Funktion zur Berechnung der Basenzählungen
std::unordered_map<char, int> calculateBaseCounts(const std::string& sequence) {
    std::unordered_map<char, int> baseCounts;
    for (char base : sequence) {
        if (base == 'A' || base == 'C' || base == 'G' || base == 'U') {
            baseCounts[base]++;
        }
    }
    return baseCounts;
}

// Funktion zur Ausgabe der Basenzählungen
void printBaseCounts(const std::unordered_map<char, int>& baseCounts) {
    std::cout << "Base Counts:" << std::endl;
    std::cout << "A: " << baseCounts.at('A') << std::endl;
    std::cout << "C: " << baseCounts.at('C') << std::endl;
    std::cout << "G: " << baseCounts.at('G') << std::endl;
    std::cout << "U: " << baseCounts.at('U') << std::endl;
    std::cout << std::endl;
}

// Funktion zur Berechnung und Ausgabe des GC-Gehalts
void printGCGehalt(const std::string& sequence) {
    std::unordered_map<char, int> baseCounts = calculateBaseCounts(sequence);

    int gcCount = baseCounts.at('G') + baseCounts.at('C');
    float gcGehalt = static_cast<float>(gcCount) / sequence.length() * 100;
    gcGehalt = std::round(gcGehalt * 100) / 100; // Runden auf zwei Dezimalstellen

    std::cout << "Der GC-Gehalt beträgt: " << gcGehalt << "%" << std::endl;
    std::cout << std::endl;
}

// Funktion zur Ausgabe des Histogramms
void printBaseHistogram(const std::unordered_map<char, int>& baseCounts) {
    std::cout << "Base Histogram:" << std::endl;
    std::cout << "----------------------------------------" << std::endl;
    for (const auto& entry : baseCounts) {
        char base = entry.first;
        int count = entry.second;

        std::cout << base << ": ";
        for (int i = 0; i < count; i++) {
            std::cout << "=";
        }
        std::cout << std::endl;
    }
    std::cout << "----------------------------------------" << std::endl;
    std::cout << std::endl;
}

int main() {
    std::string inputFilename = "input.fasta";
    std::string outputFilename = "output.fasta";

    // Sequenzen aus der Eingabedatei einlesen
    std::vector<FastaSequence> sequences = FastaParser::parseFastaFile(inputFilename);

    // Überprüfen, ob Sequenzen vorhanden sind
    if (sequences.empty()) {
        std::cout << "No sequences found in the input file." << std::endl;
        return 0;
    }

    // Sequenzen in Ausgabedatei schreiben
    FastaParser::writeFastaFile(sequences, outputFilename);
    std::cout << "Die Sequenz wurde erfolgreich in " << outputFilename << " gespeichert." << "\n" << std::endl;

    // Sequenzen verarbeiten und ausgeben
    for (const FastaSequence& sequence : sequences) {
        std::cout << ">" << sequence.getHeader() << std::endl;
        std::cout << sequence.getFormattedSequence() << std::endl;

        // Sequenz in einen String speichern
        std::string sequenceString = sequence.getSequence();

        // Basenzählungen berechnen und ausgeben
        std::unordered_map<char, int> baseCounts = calculateBaseCounts(sequenceString);
        printBaseCounts(baseCounts);
        printGCGehalt(sequenceString);
        printBaseHistogram(baseCounts);

        // Aminosäuren
        std::string codon;
        std::vector<std::string> codons;

        // Durchlaufen der Sequenz in Codons
        for (std::string::size_type i = 0; i < sequenceString.length(); i += 3) {
            codon = sequenceString.substr(i, 3); // Extrahiere drei Buchstaben ab Index i
            codons.push_back(codon); // Füge das Codon dem Vektor hinzu
        }

        // Datei mit Abbildung der Aminosäure-Codons öffnen
        std::ifstream inputFile("AminoAcid_map.txt");
        if (!inputFile.is_open()) {
            std::cerr << "Die Datei konnte nicht geöffnet werden." << std::endl;
        }
        std::cout << std::endl;

        // Aminosäurenobjekt erstellen und Codons zuordnen
        AminoAcid aminoAcid(inputFile, codons);

        // Aminosäure-Sequenz ausgeben
        std::cout << "Aminosäure-Sequenz:" << std::endl;
        for (auto& amino_acid : aminoAcid.getLetters()) {
            std::cout << amino_acid << "";
        }
        std::cout << std::endl;
        std::cout << std::endl;

        // Three-Letter-Code ausgeben
        std::cout << "Three-Letter-Code:" << std::endl;
        for (auto& code : aminoAcid.getThreeLetterCodes()) {
            std::cout << code << "-";
        }
        std::cout << std::endl;
        std::cout << std::endl;
    }

    return 0;
}
