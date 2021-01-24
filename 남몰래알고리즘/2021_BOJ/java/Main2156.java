package boj_2156;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main2156 {
//10:07
	private static BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
	private static BufferedWriter bw= new BufferedWriter(new OutputStreamWriter(System.out));
	private static int n;
	private static int [] wines;
	private static int [] dp;
    private static int answer=0;
	public static void main(String[] args) throws IOException {
		n=Integer.parseInt(br.readLine());
		wines= new int[n+3];
		dp=new int[n+3];

		for(int i=3; i<n+3;i++) {
			wines[i]=Integer.parseInt(br.readLine());
		}

		for(int i=3; i<n+3; i++) {
			dp[i]=Math.max(wines[i]+dp[i-2], wines[i]+wines[i-1]+dp[i-3]);
            dp[i]=Math.max(dp[i], dp[i-1]);
            answer=Math.max(dp[i], answer);
		}
		bw.write(answer+"\n");
		bw.flush();
		bw.close();
	}
}
