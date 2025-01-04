package programmers;

import java.util.ArrayDeque;
import java.util.Deque;

class 같은숫자는싫어 {

	public int[] solution(int[] arr) {
		Deque<Integer> deque = new ArrayDeque<>();
		for (int num : arr) {
			if (deque.isEmpty() || deque.peekLast() != num) {
				deque.add(num);
			}
		}
		return deque.stream()
			.mapToInt(Integer::intValue)
			.toArray();
	}
}
