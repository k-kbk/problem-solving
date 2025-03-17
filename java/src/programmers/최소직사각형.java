package programmers;

public class 최소직사각형 {

	public int solution(int[][] sizes) {
		int maxWidth = 0;
		int maxHeight = 0;

		for (int[] size : sizes) {
			int w = Math.max(size[0], size[1]);
			int h = Math.min(size[0], size[1]);

			maxWidth = Math.max(maxWidth, w);
			maxHeight = Math.max(maxHeight, h);
		}

		return maxWidth * maxHeight;
	}
}
