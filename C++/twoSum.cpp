
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i = 0;
        int j = 1;
        vector<int> result(2);

        while (i < nums.size()) {
            while (j < nums.size()) {
                if (nums[i] + nums[j] == target) {
                    result[0] = i;
                    result[1] = j;
                    return result;
                }
                j++;
            }
            i++;
            j = i + 1;
        }

        return result;
    }
};