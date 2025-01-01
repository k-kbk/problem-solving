package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B15953 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			String[] str = br.readLine().split(" ");
			int a = Integer.parseInt(str[0]);
			int b = Integer.parseInt(str[1]);
			System.out.println(first(a) + second(b));
		}
	}

	private static int first(int x) {
		if (x == 0 || x >= 22) {
			return 0;
		}
		int[] price = {5_000_000, 3_000_000, 2_000_000, 500_000, 300_000, 100_000};
		int rank = 0;
		while (x > 0) {
			rank += 1;
			x -= rank;

		}

		return price[rank - 1];
	}

	private static int second(int x) {
		if (x == 0 || x >= 32) {
			return 0;
		}
		int[] price = {5_120_000, 2_560_000, 1_280_000, 640_000, 320_000};
		int rank = 0;
		int amount = 1;
		while (x > 0) {
			rank += 1;
			x -= amount;
			amount *= 2;
		}

		return price[rank - 1];
	}
}
