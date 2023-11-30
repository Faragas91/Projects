#ifndef FASTA_SEQUENCE_H
#define FASTA_SEQUENCE_H

#include <string>
#include <vector>
#include <unordered_map>
#include "FastaSequenceElement.h"

class FastaSequence {
public:
    // Konstruktor
    FastaSequence(const std::string& i_header);

    // Destruktor
    virtual ~FastaSequence();

    // Getter für den Header der Sequenz
    std::string getHeader() const;
    
    // Getter für die Sequenz als Zeichenkette
    std::string getSequence() const;

    // Gibt die formatierte Sequenz zurück
    std::string getFormattedSequence() const;

    // Fügt ein SequenceElement zur Sequenz hinzu
    void addSequenceElement(FastaSequenceElement* i_element);

    // Zählt die Elemente in der Sequenz mit dem gegebenen Elementcode
    int countElements(char i_elementCode) const;

private:
    // Member
    std::string m_header;                               // Der Header der Sequenz
    std::vector<FastaSequenceElement*> m_sequenceElements;  // Eine Liste der SequenceElemente
};

#endif  // FASTA_SEQUENCE_H
