package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Map;
import java.util.SortedMap;
import java.util.TreeMap;

public class B2480 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] arr = br.readLine().split(" ");

		SortedMap<Integer, Integer> map = new TreeMap<>();

		for (String str : arr) {
			map.put(Integer.parseInt(str), map.getOrDefault(Integer.parseInt(str), 0) + 1);
		}

		int size = map.size();
		int price;

		if (size == 1) {
			price = 10_000 + map.lastKey() * 1_000;

		} else if (size == 2) {
			int key = 0;
			for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
				if (entry.getValue() == 2) {
					key = entry.getKey();
					break;
				}
			}
			price = 1_000 + key * 100;

		} else {
			price = map.lastKey() * 100;
		}

		System.out.println(price);
	}
}
