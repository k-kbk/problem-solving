package programmers;

import java.util.HashMap;
import java.util.Map;

class 완주하지못한선수 {

	public String solution(String[] participant, String[] completion) {
		String answer = "";
		Map<String, Integer> map = new HashMap<>();
		for (String name : participant) {
			map.put(name, map.getOrDefault(name, 0) + 1);
		}
		for (String name : completion) {
			map.replace(name, map.get(name) - 1);
		}
		for (Map.Entry<String, Integer> entry : map.entrySet()) {
			if (entry.getValue() == 1) {
				answer = entry.getKey();
				break;
			}
		}

		return answer;
	}
}
