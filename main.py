import sys

PROBLEMS = {
	1: ['two_sum', 'contains_duplicate', 'valid_anagram'],
	2: ['range_sum_query_immutable', 'subarray_sum_equals_k', 'find_pivot_index'],
	3: ['valid_palindrome', 'two_sum_ii_input_array_is_sorted', 'squares_of_a_sorted_array'],
	4: ['best_time_to_buy_and_sell_stock', 'longest_substring_without_repeating_characters', 'permutation_in_string'],
	5: ['binary_search', 'search_insert_position', 'koko_eating_bananas'],
	6: ['valid_parentheses', 'min_stack', 'daily_temperatures'],
	7: ['number_of_islands', 'rotting_oranges', 'flood_fill'],
	8: ['max_area_of_island', 'surrounded_regions', 'word_search'],
	9: ['climbing_stairs', 'house_robber', 'coin_change'],
	10: ['min_cost_climbing_stairs', 'unique_paths', 'longest_common_subsequence'],
}

def run_one(lesson, problem_index):
	name = PROBLEMS[lesson][problem_index - 1]
	mod = f"lesson{lesson}.practice.{name}"
	m = __import__(mod, fromlist=["run_tests"])
	m.run_tests()

def main():
	if len(sys.argv) == 1:
		for i in range(1, 4):
			run_one(1, i)
		return

	lesson = int(sys.argv[1])
	if len(sys.argv) == 2:
		for i in range(1, 4):
			run_one(lesson, i)
		return

	problem = int(sys.argv[2])
	run_one(lesson, problem)

if __name__ == "__main__":
	main()
