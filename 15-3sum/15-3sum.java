class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        HashSet<Integer> visit = new HashSet<Integer>();
        HashSet<List<Integer>> res = new HashSet<List<Integer>>();
        Arrays.sort(nums);
        for (int i=0; i<nums.length; i++){
            for (int j=i+1; j<nums.length; j++){
                if (visit.contains(-nums[i]-nums[j])){
                    List<Integer> arr = new ArrayList<>(Arrays.asList(-nums[i]-nums[j], nums[i], nums[j]));
                    res.add(arr);
                }
            }
            visit.add(nums[i]);
        }
        List<List<Integer>> r = new ArrayList<>(res);
        return r;
    }
}