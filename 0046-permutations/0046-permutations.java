class Solution {
    public List<List<Integer>> permute(int[] nums) {
       
        List<Integer> smallList = new ArrayList<>();
    List<List<Integer>> bigList = new ArrayList<>();
    backtrack(nums, smallList, bigList);
    return bigList;
    }

    public void backtrack(int[] nums, List<Integer> smallList, List<List<Integer>> bigList) {
        if (nums.length == smallList.size()) {
            bigList.add(new ArrayList<>(smallList));
            return;
        }
        for (int i : nums) {
            if (!smallList.contains(i)) {
                smallList.add(i);
                backtrack(nums, smallList, bigList);
                smallList.remove(smallList.size() - 1);
            }
        }
}}