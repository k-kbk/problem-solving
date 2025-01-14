package programmers;

class 올바른괄호 {

	boolean solution(String s) {
		int count = 0;
		for (char c : s.toCharArray()) {
			if (c == '(') {
				count++;
			} else {
				if (count == 0) {
					return false;
				}
				count--;
			}
		}
		return count == 0;
	}
}
