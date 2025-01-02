package programmers;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

class 베스트앨범 {

	public int[] solution(String[] genres, int[] plays) {
		Map<String, Integer> totalCountMap = new HashMap<>();
		for (int i = 0; i < genres.length; i++) {
			totalCountMap.put(genres[i], totalCountMap.getOrDefault(genres[i], 0) + plays[i]);
		}
		Map<Integer, List<Integer[]>> map = new TreeMap<>(Comparator.reverseOrder());
		for (int i = 0; i < genres.length; i++) {
			int totalCount = totalCountMap.get(genres[i]);
			List<Integer[]> list = map.getOrDefault(totalCount, new ArrayList<>());
			list.add(new Integer[]{plays[i], i});
			map.put(totalCount, list);
		}
		List<Integer> answer = new ArrayList<>();
		for (Map.Entry<Integer, List<Integer[]>> entry : map.entrySet()) {
			List<Integer[]> list = entry.getValue();
			list.sort((a, b) -> {
				if (!b[0].equals(a[0])) {
					return b[0] - a[0];
				} else {
					return a[1] - b[1];
				}
			});
			answer.add(list.get(0)[1]);
			if (list.size() > 1) {
				answer.add(list.get(1)[1]);
			}
		}
		return answer.stream().mapToInt(Integer::intValue).toArray();
	}
}
