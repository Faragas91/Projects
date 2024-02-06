// You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 
// The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

// Given the string command, return the Goal Parser's interpretation of command.

// Example 1:

// Input: command = "G()(al)"
// Output: "Goal"
// Explanation: The Goal Parser interprets the command as follows:
// G -> G
// () -> o
// (al) -> al
// The final concatenated result is "Goal".
// Example 2:

// Input: command = "G()()()()(al)"
// Output: "Gooooal"
// Example 3:

// Input: command = "(al)G(al)()()G"
// Output: "alGalooG"

#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string interpret(string command) {
        string result;
        int i = 0;
        
        while (i < command.length()) {

            if (command[i] == 'G'){
                result += 'G';
                command.erase(command.begin());
            }
            if (command[i] == '(' and command[i + 1] == ')' ){
                result += 'o';
                command.erase(0,2);
            }
            if (command[i] == '(' and command[i + 1] == 'a' and command[i+2] == 'l' and command[i + 3] == ')' ){
                result += "al";
                command.erase(0,4);
            }
        }
        return result;
    }  
};

int main(){
    string command = "G()()()()(al)";

    Solution solution;
    string result = solution.interpret(command);
    std::cout << result << std::endl;

    return 0;
}