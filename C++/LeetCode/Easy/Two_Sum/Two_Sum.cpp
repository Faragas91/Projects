// Given an array of integers nums and an integer target, 
// return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, 
// and you may not use the same element twice.

// You can return the answer in any order.

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        // Rückgabewert, falls keine Lösung gefunden wurde
        return {};
    }
};

int main() {
    vector<int> nums = {2, 7, 11, 15};
    int target = 18;

    Solution solution;
    vector<int> result = solution.twoSum(nums, target);

    // Ausgabe der gefundenen Indizes
    for (int index : result) {
        std::cout << index << " ";
    }

    return 0;
}


