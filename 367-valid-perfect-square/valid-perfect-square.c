bool isPerfectSquare(int num) {
    int s=pow(num,0.5);
    if(s*s==num){
        return true;
    }else{
        return false;
    }
}