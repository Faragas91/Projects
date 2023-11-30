#ifndef FASTA_SEQUENCE_ELEMENT_H
#define FASTA_SEQUENCE_ELEMENT_H

#include <string>

class FastaSequenceElement {
public:
    // Konstruktor
    FastaSequenceElement(char i_elementCode) : m_elementCode(i_elementCode) {}
    
    // Dekonstruktor
    virtual ~FastaSequenceElement() {}

    // Getter
    virtual std::string getDescription() const = 0;
    
    // Member
    char m_elementCode;
};
#endif  // FASTA_SEQUENCE_ELEMENT_H
