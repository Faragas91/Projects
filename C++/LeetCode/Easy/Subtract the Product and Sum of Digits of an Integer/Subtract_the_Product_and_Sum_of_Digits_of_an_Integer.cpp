//Given an integer number n, return the difference between the product of its digits and the sum of its digits.
//
//
//Example 1:
//
//Input: n = 234
//Output : 15
//Explanation :
//	Product of digits = 2 * 3 * 4 = 24
//	Sum of digits = 2 + 3 + 4 = 9
//	Result = 24 - 9 = 15
//	Example 2 :
//
//	Input : n = 4421
//	Output : 21
//	Explanation :
//	Product of digits = 4 * 4 * 2 * 1 = 32
//	Sum of digits = 4 + 4 + 2 + 1 = 11
//	Result = 32 - 11 = 21


#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
	int subtractProductAndSum(int n) {
		vector<int> digits = divideNumber(n);

		int produkt = 1;
		int sum = 0;

		for (int digit : digits) {
			produkt *= digit;
			sum += digit;
		}

		return produkt - sum;
	}


	vector<int> divideNumber(int num) {
		vector<int> number;

		while (num > 0) {
			int lastNumber = num % 10;
			number.push_back(lastNumber);
			num /= 10;
		}
		reverse(number.begin(), number.end());

		return number;
	}
};


int main() {

	int n = 234;

	int result = Solution().subtractProductAndSum(n);

	cout << result << endl;

	return 0;
}