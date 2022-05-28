class Solution {
    public int[] productExceptSelf(int[] nums) {
        int res[] = new int[nums.length];
        res[0] = 1;
        int right[] = new int[nums.length];
        right[right.length - 1] = 1;
        for (int i = 1; i < res.length; i++) {
            res[i] = res[i - 1] * nums[i - 1];
        }
        for (int i = (right.length - 2); i >= 0; i--) {
            right[i] = right[i + 1] * nums[i + 1];
        }
        for (int i = 0; i < res.length; i++) {
            res[i] *= right[i];
        }
        return res;
    }
}