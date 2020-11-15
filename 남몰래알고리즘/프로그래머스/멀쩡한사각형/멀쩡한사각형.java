class Solution {
    public long gcd(long w, long h) {
		long big=(w>h)? w:h;
		long small=(w<=h)?w:h;
		
		//최대 공약수
		long tmp;
		while(small!=0) {
			tmp=big%small;
			big=small;
			small=tmp;
		}
		return big;
	}
    
	public long solution(int w, int h) {
        long wl= Long.parseLong(String.valueOf(w));
        long hl= Long.parseLong(String.valueOf(h));
		return (wl*hl)-(wl+hl-gcd(wl,hl) );
	}
}
