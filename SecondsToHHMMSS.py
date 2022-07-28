def make_readable(seconds):
    hours = 0
    minutes = 0
    while seconds >= 60:
        if seconds >= 3600:
            seconds -= 3600
            hours += 1
        else:
            seconds -= 60
            minutes += 1
    hours = addZero(hours)
    minutes = addZero(minutes)
    seconds = addZero(seconds)
    return f"{hours}:{minutes}:{seconds}"


def addZero(time):
    if time < 10:
        return "0" + str(time)
    return time


if __name__ == '__main__':
    print(make_readable(14613))
