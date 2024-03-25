//Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n(0 - indexed).
//
//	Specifically, ans is the concatenation of two nums arrays.
//
//	Return the array ans.
//
//
//
//	Example 1:
//
//Input: nums = [1, 2, 1]
//Output : [1, 2, 1, 1, 2, 1]
//Explanation : The array ans is formed as follows :
//-ans = [nums[0], nums[1], nums[2], nums[0], nums[1], nums[2]]
//- ans = [1, 2, 1, 1, 2, 1]
//Example 2 :
//
//	Input : nums = [1, 3, 2, 1]
//	Output : [1, 3, 2, 1, 1, 3, 2, 1]
//	Explanation : The array ans is formed as follows :
//-ans = [nums[0], nums[1], nums[2], nums[3], nums[0], nums[1], nums[2], nums[3]]
//- ans = [1, 3, 2, 1, 1, 3, 2, 1]

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int z = 0;
        vector<int> bla;
        while (z < 2) {
            for (int i = 0; i < nums.size(); i++) {
                bla.push_back(nums[i]);
            }
            z++;
           
        }
        return bla;
    }
};

int main() {

    vector<int> nums = {1,2,1};
    vector<int> result = Solution().getConcatenation(nums);

    for (int j = 0; j < result.size(); j++) {
        cout << result[j] << endl;
    }

    return 0;
}