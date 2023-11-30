#include "FastaSequence.h"

// Konstruktor
FastaSequence::FastaSequence(const std::string& i_header) : m_header(i_header) {}

// Destruktor
FastaSequence::~FastaSequence() {}

// Fügt ein SequenceElement zur Sequenz hinzu
void FastaSequence::addSequenceElement(FastaSequenceElement* i_element) {
    m_sequenceElements.push_back(i_element);
}

// Getter für den Header der Sequenz
std::string FastaSequence::getHeader() const {
    return m_header;
}

// Getter für die Sequenz als Zeichenkette
std::string FastaSequence::getSequence() const {
    std::string sequence;
    for (FastaSequenceElement* element : m_sequenceElements) {
        sequence += element->getDescription();
    }
    return sequence;
}

// Formatiert die DNA-Sequenz für die Ausgabe
std::string FastaSequence::getFormattedSequence() const {
    std::string sequence = getSequence();
    std::string formattedSequence;
    size_t chunkSize = 80;

    for (size_t i = 0; i < sequence.length(); i += chunkSize) {
        formattedSequence += sequence.substr(i, chunkSize);
        formattedSequence += "\n";
    }
    return formattedSequence;
}

// Zählt die Elemente in der Sequenz
int FastaSequence::countElements(char i_elementCode) const {
    int count = 0;
    for (FastaSequenceElement* element : m_sequenceElements) {
        if (element->getDescription() == std::string(1, i_elementCode)) {
            count++;
        }
    }
    return count;
}
