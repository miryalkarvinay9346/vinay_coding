int addDigits(int num) {
    here:
    if(num==0 ){
        return 0;
        }
        if(num<=9){
        return num;
    }
    else{
       int sum=0;
        while(num>0){
            sum+=num%10;
            num/=10;
        }
        if(sum<=9){
            return sum;
        }else{
            num=sum;
            goto here;
        }
    }
}