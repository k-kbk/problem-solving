package programmers;

import java.util.Arrays;

class K번째수 {

	public int[] solution(int[] array, int[][] commands) {
		int[] ans = new int[commands.length];

		for (int i = 0; i < commands.length; i++) {
			int[] subArray = Arrays.copyOfRange(array, commands[i][0] - 1, commands[i][1]);
			Arrays.sort(subArray);
			ans[i] = subArray[commands[i][2] - 1];
		}

		return ans;
	}
}
