# Given lists
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Check if Alice is in both lists
if "Alice" in submitted and "Alice" in attended:
    print("Alice submitted their assignment and attended class.")
else:
    print("Alice did not submit their assignment or attend class.")