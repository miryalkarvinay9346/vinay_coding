class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m=nums1.length,n=nums2.length;
        int []a=new int[m+n];
        for(int i=0;i<m;i++){
            a[i]=nums1[i];
        }
        for(int j=0;j<n;j++){
            a[m+j]=nums2[j];
        }
        for(int i=0;i<m+n-1;i++){
            for(int j=0;j<m+n-i-1;j++){
                if(a[j]>a[j+1]){
                    int temp=a[j];
                    a[j]=a[j+1];
                    a[j+1]=temp;
                }

            }
        }
        if((m+n)%2==0){
            return  (a[(m+n)/2 -1]+a[(m+n)/2])/2.0;
        }else{
            return a[(m+n)/2];
        }
    }
}