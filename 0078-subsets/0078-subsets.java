class Solution {
    public List<List<Integer>> subsets(int[] nums) {
    List<Integer> smallList = new ArrayList<>();
    List<List<Integer>> bigList = new ArrayList<>();
    backtrack(nums,0, smallList, bigList);
    return bigList;
    }

    public void backtrack(int[] nums,int index, List<Integer> smallList, List<List<Integer>> bigList) {
        bigList.add(new ArrayList<>(smallList));
        for (int i=index;i<nums.length;i++) {
            if (!smallList.contains(nums[i])) {
                smallList.add(nums[i]);
                backtrack(nums,i, smallList, bigList);
                smallList.remove(smallList.size() - 1);
            }
        }
        
    }
}