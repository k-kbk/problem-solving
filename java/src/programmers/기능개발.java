package programmers;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

class 기능개발 {

	public List<Integer> solution(int[] progresses, int[] speeds) {
		Deque<Integer> days = new ArrayDeque<>();
		for (int i = 0; i < speeds.length; i++) {
			int progress = progresses[i];
			int speed = speeds[i];
			int day = 0;
			while (progress < 100) {
				progress += speed;
				day += 1;
			}
			days.add(day);
		}
		List<Integer> answer = new ArrayList<>();
		int first = days.poll();
		int count = 1;
		while (!days.isEmpty()) {
			int day = days.poll();
			if (day > first) {
				answer.add(count);
				first = day;
				count = 1;
				continue;
			}
			count += 1;
		}
		answer.add(count);
		return answer;
	}
}
