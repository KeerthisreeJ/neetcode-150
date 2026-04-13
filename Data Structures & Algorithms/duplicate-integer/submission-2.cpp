class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        if (nums.size() > 1){
            for (int i = 0 ; i < (int)nums.size() - 1 ; i++){
                for (int j = i+1; j < (int)nums.size() ; j++){
                    if (nums[i] == nums[j]){
                        return true;
                    }
                }
            }
        }
        return false;
    }
};