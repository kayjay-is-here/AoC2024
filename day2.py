import numpy as np

def parse(s):
    return [np.array([int(level) for level in report.split()]) for report in s.splitlines()]

with open("inputs/day2.txt", "r") as f:
    reports = [np.array([int(x) for x in line.split()]) for line in f.read().splitlines()]

def is_report_safe(report):
    diff = np.diff(report)
    all_descending = np.all(diff < 0)
    all_ascending = np.all(diff > 0)
    if not (all_descending or all_ascending):
        return False
    return np.all(np.abs(diff) <= 3)

def part_a(data):
    return sum(is_report_safe(report) for report in data)

def is_report_safe_after_dampener(report):
    if is_report_safe(report):
        return True
    for i in range(len(report)):
        dampened_report = np.delete(report, i)
        if is_report_safe(dampened_report):
            return True
    return False

def part_b(data):
    return sum(is_report_safe_after_dampener(report) for report in data)

print(part_b(reports))
