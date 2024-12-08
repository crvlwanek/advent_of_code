import collections

with open("input.txt") as file:
    text = file.read()



def part1():
    graph = collections.defaultdict(list)
    total = 0

    rules, updates = text.split("\n\n")

    for rule in rules.split("\n"):
        a, b = rule.split("|")
        graph[b].append(a)

    for update in updates.split("\n"):

        correct = True
        pageNumbers = update.split(",")
        for i, num1 in enumerate(pageNumbers):
           for j, num2 in enumerate(pageNumbers):
               if i > j and num1 in graph[num2]:
                   correct = False

        if correct:
            total += int(pageNumbers[len(pageNumbers) // 2])

    print(total)

def part2():
    graph = collections.defaultdict(list)
    total = 0

    rules, updates = text.split("\n\n")

    for rule in rules.split("\n"):
        a, b = rule.split("|")
        graph[b].append(a)

    for update in updates.split("\n"):

        # warning, jank ensuing below...
        correct = False
        didReorder = False
        pageNumbers = update.split(",")
        while not correct:
            correct = True
            for i, num1 in enumerate(pageNumbers):
                for j, num2 in enumerate(pageNumbers):
                    if i > j and num1 in graph[num2]:
                        correct = False
                        didReorder = True
                        pageNumbers[i], pageNumbers[j] = pageNumbers[j], pageNumbers[i]

        if didReorder:
            total += int(pageNumbers[len(pageNumbers) // 2])

    print(total)

part2()
