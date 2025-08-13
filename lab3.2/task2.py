import statistics

def calculate_stats():
    nums = input("Enter numbers separated by spaces: ")
    num_list = [float(x) for x in nums.split()]
    avg = sum(num_list) / len(num_list)
    median = statistics.median(num_list)
    try:
        mode = statistics.mode(num_list)
    except statistics.StatisticsError:
        mode = "No unique mode"
    print(f"Average: {avg}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")

if __name__ == "__main__":
    calculate_stats()