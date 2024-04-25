import csv


def main():
    file_path = 'gemma-context4-google'

    reports = []
    with open(file_path, 'r') as file:
        file_content = file.read()
        all = file_content.split(
            "+------------------------------------------------------------------------------------------------------------------------+")
        for report in all:
            splitted = report.split("+--------------------------------------+")
            if len(splitted) != 2:
                continue
            else:
                reports.append((splitted[0], splitted[1]))

    with open('report.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)

        for report in reports:
            parsed = parseRuntimeStats(report[0])
            for stat in parseResponeReport(report[1]):
                parsed.append(stat)
            writer.writerow(parsed)

    with open('report.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row[3])


def parseRuntimeStats(runtimestats):
    stats = runtimestats.split("|")
    answerStartTime = stats[1].split(":")[1].strip()
    answerFinishTime = stats[2].split(":")[1].strip()
    promptLength = stats[3].split(":")[1].strip()
    answerLength = stats[4].split(":")[1].strip()
    tokenPrSecondPrefill = stats[5].split(":")[1].strip()
    tokenPrSecondDecode = stats[6].split(":")[1].strip()
    parsed = [answerStartTime, answerFinishTime, promptLength, answerLength, tokenPrSecondPrefill, tokenPrSecondDecode]
    return parsed


def parseResponeReport(responeReport):
    report = responeReport.split("|")
    date = report[1].split(":")[1].strip()
    modelId = report[2].split(":")[1].strip()
    prompt = report[3].split(":")[1].strip()
    context = report[4].split(":", 1)[1].strip()

    answer = report[5].split(":")[1].strip()
    parsed = [date, modelId, prompt, context, answer]
    return parsed


if __name__ == '__main__':
    main()
