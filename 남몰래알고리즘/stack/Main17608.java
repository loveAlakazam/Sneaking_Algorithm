// 소스코드 제출할때  패키지이름은 무조건 제거한다.
//package stack.boj17608;

// 임포트한 라이브러리는 되도록이면 남긴다.
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

// 클래스 이름은 무조건 Main으로 한다.
public class Main{
	public int solution(int n, int [] polls) {
		int result;
		int now=n-1;
		
		// arrayList를 사용
		ArrayList<Integer> answer=new ArrayList<Integer>();
		
		//오른쪽에서 보이는 막대기의 개수를 알아봐야하므로..
		//먼저, 마지막 polls를 answer리스트에 넣는다.
		answer.add(polls[n-1]);
		
		while(now>0) {
			// polls[now-1]과 answer의 가장 마지막 값과 비교한다.
			if( polls[now-1]> (int)answer.get(answer.size()-1)){
				answer.add(polls[now-1]);
			}
			now--;
		}
		
		result=answer.size();
		return result;
	}
	
	public static void main(String [] args) throws IOException {
		
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw= new BufferedWriter(new OutputStreamWriter(System.out));
		
		Main mainSolution= new Main();
		
		//막대기 개수
		int n= Integer.parseInt(br.readLine());
		
		//막대기들
		int polls[]= new int[n];
		for(int i=0; i<n; i++) {
			polls[i]= Integer.parseInt(br.readLine());
		}
		
		int answer=mainSolution.solution(n,polls);
		System.out.println(answer);
	}
}
