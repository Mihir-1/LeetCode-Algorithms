class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> vals = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (vals.containsKey(target - nums[i])) {
                return new int[]{i, vals.get(target - nums[i])};
            } else {
                vals.put(nums[i], i);
            }
        }
        return new int[0];
    }
}