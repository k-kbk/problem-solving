package programmers;

import java.util.Arrays;

public class H_Index {

	public int solution(int[] citations) {
		Arrays.sort(citations);

		for (var i = 0; i < citations.length; i++) {
			var h = citations.length - i;
			if (citations[i] >= h) {
				return h;
			}
		}

		return 0;
	}
}
