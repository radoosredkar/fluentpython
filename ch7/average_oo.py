class Averager():
    def __init__(self) -> None:
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        average = total / len(self.series)
        print(average)
        return average


def make_averager():
    series = []
    total = 0
    count = 0

    def average(new_value):
        nonlocal total, count
        series.append(new_value)
        count += 1
        total += new_value
        aver = total / count
        print(aver)
        return aver

    return average


def main():
    avg = Averager()
    avg(10)
    avg(30)
    avg(5)

    avg = make_averager()
    avg(10)
    avg(30)
    avg(5)


if __name__ == '__main__':
    main()
