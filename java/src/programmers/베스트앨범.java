package programmers;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class 베스트앨범 {

	public int[] solution(String[] genres, int[] plays) {
		Map<String, Integer> genreCountsMap = new HashMap<>();
		for (int i = 0; i < genres.length; i++) {
			genreCountsMap.put(genres[i], genreCountsMap.getOrDefault(genres[i], 0) + plays[i]);
		}
		List<Music> musics = new ArrayList<>();
		for (int i = 0; i < genres.length; i++) {
			int genreCounts = genreCountsMap.get(genres[i]);
			musics.add(new Music(i, plays[i], genreCounts));
		}
		Collections.sort(musics);
		List<Integer> answer = new ArrayList<>();
		int count = 0;
		int prev = 0;
		for (Music music : musics) {
			int curr = music.getGenreCounts();
			if (curr != prev) {
				count = 0;
			} else if (count == 2) {
				continue;
			}
			answer.add(music.getId());
			count += 1;
			prev = curr;
		}
		return answer.stream().mapToInt(Integer::intValue).toArray();
	}

	class Music implements Comparable<Music> {

		private final int id;
		private final int plays;
		private final int genreCounts;

		Music(int id, int plays, int genreCounts) {
			this.id = id;
			this.plays = plays;
			this.genreCounts = genreCounts;
		}

		int getId() {
			return this.id;
		}

		int getPlays() {
			return this.plays;
		}

		int getGenreCounts() {
			return this.genreCounts;
		}

		@Override
		public int compareTo(Music other) {
			if (this.genreCounts != other.genreCounts) {
				return Integer.compare(other.genreCounts, this.genreCounts);
			}

			if (this.plays != other.plays) {
				return Integer.compare(other.plays, this.plays);
			}

			return Integer.compare(this.id, other.id);
		}
	}
}
