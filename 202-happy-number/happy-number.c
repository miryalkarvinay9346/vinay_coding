bool isHappy(int n) {
    here: 
     if(n==1){
            return true;
        }
        else if(n==4){
            return false;
        }else{
        int rem=0;
        int sum=0;
        int temp=n;
        while(temp>0){
            rem=temp%10;
            sum+=rem*rem;
            temp/=10;
        }
        if(sum==1){
            return true;
        }
        else{
            n=sum;
            goto here;
        }
        }
    
}