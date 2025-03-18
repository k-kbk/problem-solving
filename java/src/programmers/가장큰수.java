package programmers;

import java.util.Arrays;
import java.util.stream.Collectors;

public class 가장큰수 {

	public String solution(int[] numbers) {
		var result = Arrays.stream(numbers)
			.mapToObj(String::valueOf)
			.sorted((a, b) -> (b + a).compareTo(a + b))
			.collect(Collectors.joining());

		return result.startsWith("0") ? "0" : result;
	}
}
