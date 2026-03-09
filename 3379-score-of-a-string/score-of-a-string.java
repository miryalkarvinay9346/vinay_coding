class Solution {
    public int scoreOfString(String s) {
        int c=0;
        for(int i=0;i<s.length()-1;i++){
            char a=s.charAt(i);
            char b=s.charAt(i+1);
            c+=Math.abs((int)a-(int)b);
        }
        return(c);
    }
}