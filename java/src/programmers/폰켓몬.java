package programmers;

import java.util.HashSet;
import java.util.Set;

public class 폰켓몬 {

	public int solution(int[] nums) {
		Set<Integer> set = new HashSet<>();
		for (int n : nums) {
			set.add(n);
		}
		int size = set.size();

		return Math.min(size, nums.length / 2);
	}
}
