with open("input.txt") as file:
    reports = [[int(report) for report in line.split()] for line in file.readlines()]

MIN_SAFE_DIFFERENCE = 1
MAX_SAFE_DIFFERENCE = 3

def isSafe(report, problemTolerance=0):

    problemCount = 0
    hitProblem = False
    isIncreasing = report[0] < report[-1] or report[0] < report [-2]

    for i, level in enumerate(report):
        if not i:
            continue

        if not hitProblem:
            previousLevel = report[i - 1]

        hitProblem = False

        difference = abs(level - previousLevel)

        if difference > MAX_SAFE_DIFFERENCE or difference < MIN_SAFE_DIFFERENCE:
            problemCount += 1
            hitProblem = True
            continue
        
        currentIsIncreasing = level > previousLevel

        if currentIsIncreasing != isIncreasing:
            problemCount += 1
            hitProblem = True

    isReportSafe = problemCount <= problemTolerance

    return isReportSafe

def part1():
    count = sum(isSafe(report) for report in reports)
    print(count)

def part2():
    # This is complete jank and not efficient but it works
    count = sum(isSafe(report) or any(isSafe(report[:i] + report[i+1:]) for i in range(len(reports))) for report in reports)
    print(count)

part2()