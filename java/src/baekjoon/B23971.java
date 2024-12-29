package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B23971 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String[] inputs = br.readLine().split(" ");

		double H = Double.parseDouble(inputs[0]);
		double W = Double.parseDouble(inputs[1]);
		double N = Double.parseDouble(inputs[2]);
		double M = Double.parseDouble(inputs[3]);

		double x = Math.ceil(W / (M + 1));
		double y = Math.ceil(H / (N + 1));

		System.out.println((int) (x * y));
	}
}
