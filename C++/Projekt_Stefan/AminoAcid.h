#ifndef AMINO_ACID_H
#define AMINO_ACID_H

#include <vector>
#include "FastaSequenceElement.h"
#include <iostream>

class AminoAcid {
public:
    // Konstruktor
    AminoAcid(std::ifstream& inputFile, std::vector<std::string> codons) : m_inputFile(inputFile), m_codons(codons) {
        addAmino();
    }

    // Dekonstruktor
    virtual ~AminoAcid() {}

    // Getter
    std::vector<std::string> getLetters() {
        return this->m_letters;
    };

    std::vector<std::string> getThreeLetterCodes() {
        return this->m_threeLetterCodes;
    };

    //Setter
    void setLetters(const std::vector<std::string>& i_letters) {
        this->m_letters = i_letters;
    }

    void setThreeLetterCodes(const std::vector<std::string>& i_threeLetterCodes) {
        this->m_threeLetterCodes = i_threeLetterCodes;
    }

    // Funktion zum Hinzufügen von Aminosäuren
    void addAmino() {
        std::string line;
        std::vector<std::string> letters;
        std::vector<std::string> threeLetterCodes;

        // Durchlaufen der Codons
        for (std::string::size_type i = 0; i < m_codons.size(); i++) {
            start:
            // Einlesen der Zeilen aus der Eingabedatei
            while (std::getline(m_inputFile, line)) {
                if (m_codons[i] == line.substr(0, 3)) {
                    letters.push_back(std::string(1, line[4])); // Das zweite Zeichen (Aminosäure) zur Ausgabeliste hinzufügen
                    threeLetterCodes.push_back(line.substr(6, 3));
                    goto start; // Gehe zum Label "start" und starte die innere Schleife von vorne
                }
            }
            
            // Zurückspulen des Eingabestroms für die nächste Iteration der äußeren Schleife
            m_inputFile.clear();
            m_inputFile.seekg(0);
        }

        // Aminosäure- und Three-Letter-Code-Listen setzen
        setThreeLetterCodes(threeLetterCodes);
        setLetters(letters);
    }

    // Member-Variablen
    std::vector<std::string> m_letters;
    std::vector<std::string> m_threeLetterCodes;
    std::ifstream& m_inputFile;
    std::vector<std::string> m_codons;
};

#endif  // AMINO_ACID_H
