class Solution {
    public int maxSubArray(int[] nums) {
        int cur = nums[0];
        int max = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if ((cur + nums[i]) > nums[i]) {
                cur += nums[i];
            } else {
                cur = nums[i];
            }
            if (cur > max) {
                max = cur;
            }
        }
        return max;
    }
}