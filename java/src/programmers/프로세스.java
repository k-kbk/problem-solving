package programmers;

import java.util.ArrayDeque;
import java.util.Deque;

class 프로세스 {

	public int solution(int[] priorities, int location) {
		Deque<int[]> deque = new ArrayDeque<>();
		for (int i = 0; i < priorities.length; i++) {
			deque.add(new int[]{priorities[i], i});
		}
		int count = 0;
		while (!deque.isEmpty()) {
			int max = Integer.MIN_VALUE;
			for (int[] array : deque) {
				if (array[0] > max) {
					max = array[0];
				}
			}
			int[] p = deque.poll();
			if (p[0] == max) {
				count += 1;
				if (p[1] == location) {
					return count;
				}
			} else {
				deque.add(p);
			}
		}
		return count;
	}
}
