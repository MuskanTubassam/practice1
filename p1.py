marks = [88, 45, 92, 67, 30, 75]
passed=0
for mark in marks:
    if mark >= 50:
        passed = passed + 1
average = sum(marks) / len(marks)
print(f"Passed:{passed}")
print(f"Average:{average:.1f}")
print(f"Heighest:{max(marks)} Lowest:{min(marks)}")