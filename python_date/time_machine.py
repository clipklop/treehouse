import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

# Remember, you can't set "years" on a timedelta!
# Consider a year to be 365 days.

## Example
# time_machine(5, "minutes") => datetime(2015, 10, 21, 16, 34)


def time_machine(i, string):
    return starter + datetime.timedelta(days=(i * 365)) if string == 'year' \
        else starter + datetime.timedelta(**{string: i})


time_machine(20, 'minutes')
