#ifndef NUCLEOTIDE_H
#define NUCLEOTIDE_H

#include "FastaSequenceElement.h"

class Nucleotide : public FastaSequenceElement {
public:
    // Konstruktor
    Nucleotide(char i_elementCode) : FastaSequenceElement(i_elementCode) {}

    // Getter für die Beschreibung des Nukleotids
    virtual std::string getDescription() const override;
};

// Gibt die Beschreibung des Nukleotids zurück
std::string Nucleotide::getDescription() const {
    return std::string(1, m_elementCode);
}

#endif  // NUCLEOTIDE_H
