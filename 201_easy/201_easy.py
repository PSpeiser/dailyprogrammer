import datetime
inputs = ['2015-02-21', '2015-02-22', '2016-01-01']
for input in inputs:
    target_date = datetime.datetime.strptime(input, '%Y-%m-%d')
    days = (target_date - datetime.datetime.today()).days + 1 # add 1 because days only contains full 24h days
    print("{0} days until {1}".format(days, input))