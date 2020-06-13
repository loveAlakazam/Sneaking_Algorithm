class Solution {
    public String solution(String phone_number) {
        StringBuilder sb= new StringBuilder(phone_number);
        int length= phone_number.length();
        for(int i=0; i<length; i++){
            if(i<length-4){
                sb.replace(i,i+1,"*");
            }
        }
        String answer = sb.toString();
        return answer;
    }
}
