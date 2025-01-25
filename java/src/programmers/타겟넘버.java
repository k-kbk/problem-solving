package programmers;

class 타겟넘버 {

	public int solution(int[] numbers, int target) {
		return dfs(numbers, 0, target, 0);
	}

	public int dfs(int[] numbers, int depth, int target, int result) {
		if (depth == numbers.length) {
			return (target == result) ? 1 : 0;
		}

		int plus = dfs(numbers, depth + 1, target, result + numbers[depth]);
		int minus = dfs(numbers, depth + 1, target, result - numbers[depth]);

		return plus + minus;
	}
}
