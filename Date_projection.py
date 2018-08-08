def which_date(start_date,time):
    """
    This function takes as input a string depicting a date in YYYY/mm/dd
    format and a string stating a time period in the form of "X day(s)" or
    "Y week(s)". Output should be a string in form YYYY/mm/dd with the date
    that is X days or Y weeks after the initial date.
    """
    
    from datetime import datetime, date, timedelta

    #start_date = input('Please provid the date in YYYY/mm/dd format: ')
    #time = input('Please provid the time period in the form of "X day(s)" or "Y week(s)": ')

    # convert date string to datetime format
    start_date = datetime.strptime(start_date, "%Y/%m/%d")
    start_date = datetime.date(start_date)

    # split duration number by days or weeks and convert the string type to integer
    nDays = 0
    if time.endswith(("days", "day")):
        nDays = int(time.split(' ')[0])
    
    nWeeks = 0
    if time.endswith(("weeks", "week")):
        nWeeks = int(time.split(' ')[0])
    
    # convert the duration integer to datetime
    duration = timedelta(days=nDays, weeks=nWeeks)
    
    # reconver the datetime to string
    end_date = (start_date + duration).strftime('%Y/%m/%d')
    return end_date
    
def test():
    """
    Here are a few tests to check if your code is working correctly! This
    function will be run when the Test Run button is selected. Additional
    tests that are not part of this function will also be run when the Submit
    Answer button is selected.
    """
    assert which_date('2016/02/10','35 days') == '2016/03/16'
    assert which_date('2016/12/21','3 weeks') == '2017/01/11'
    assert which_date('2015/01/17','1 week') == '2015/01/24'
    print("All tests completed.")


if __name__ == "__main__":
    test()
