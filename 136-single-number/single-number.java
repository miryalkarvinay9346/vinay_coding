class Solution {
    public int singleNumber(int[] nums) {
        int val=0;
        int l=nums.length;
        for (int i=0;i<l;i++){
           int count=0;
            for(int j=0;j<l;j++){
                if(nums[i]==nums[j]){
                    count++;
                }
            }if(count<=1){
                val=nums[i];
                break;

            }
        }return val ;
    }
}