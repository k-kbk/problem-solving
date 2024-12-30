package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class B23971 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int[] inputs = Arrays.stream(br.readLine().split(" "))
			.mapToInt(Integer::parseInt)
			.toArray();

		int H = inputs[0];
		int W = inputs[1];
		int N = inputs[2];
		int M = inputs[3];

		int x = (W + M) / (M + 1);
		int y = (H + N) / (N + 1);

		System.out.println(x * y);
	}
}
