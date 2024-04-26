import csv
import os
import sys


def main():
    if len(sys.argv) != 2:
        files = (os.listdir(os.path.join(os.path.dirname(__file__), "input")))
    else:
        files = [sys.argv[1]]

    reports = []
    for log in files:
        print(f"Parsing: {log}")
        with open(f"input/{log}", 'r') as file:
            file_content = file.read()
            all = file_content.split(
                "+------------------------------------------------------------------------------------------------------------------------+")
            for report in all:
                splitted = report.split("+--------------------------------------+")
                if len(splitted) != 2:
                    continue
                else:
                    reports.append((splitted[0], splitted[1]))

        with open(f'output/{log.split(".")[0]}.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)

            for report in reports:
                parsed = parse_runtime_stats(report[0])
                for stat in parse_response_report(report[1]):
                    parsed.append(stat)
                writer.writerow(parsed)

    return 0


def parse_runtime_stats(runtimestats):
    stats = runtimestats.split("|")
    answerStartTime = stats[1].split(":", 1)[1].strip()
    answerFinishTime = stats[2].split(":", 1)[1].strip()
    promptLength = stats[3].split(":", 1)[1].strip()
    answerLength = stats[4].split(":", 1)[1].strip()
    tokenPrSecondPrefill = stats[5].split(":", 1)[1].strip()
    tokenPrSecondDecode = stats[6].split(":", 1)[1].strip()
    parsed = [answerStartTime, answerFinishTime, promptLength, answerLength, tokenPrSecondPrefill, tokenPrSecondDecode]
    return parsed


def parse_response_report(responeReport):
    report = responeReport.split("|")
    date = report[1].split(":", 1)[1].strip()
    modelId = report[2].split(":", 1)[1].strip()
    prompt = report[3].split(":", 1)[1].strip()
    context = report[4].split(":", 1)[1].strip()
    answer = report[5].split(":", 1)[1].strip()
    parsed = [date, modelId, prompt, context, answer]
    return parsed


if __name__ == '__main__':
    exit(main())
