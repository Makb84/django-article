from . import jalali
# from . import jalali_date
from django.utils import timezone

def persian_numbers_convertor(mystr):
    """
    Convert Latin digits in a string to Persian (Eastern Arabic-Indic) digits.
    """
    numbers = {
        "0": "۰",
        "1": "۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
    }

    for e, p in numbers.items():

        mystr = mystr.replace(e, p)

    return mystr




def jalali_conventor(time):
    """
    Convert a given datetime object to a Persian (Jalali) formatted string.
    """    

    jmonths = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
    
    # Convert time to the local timezone
    time = timezone.localtime(time)

    # Convert time to Persian (Jalali) tuple
    time_to_str = "{},{},{}".format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()

    time_to_list = list(time_to_tuple)

    # show months with name
    for index, month in enumerate(jmonths):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break

    # Format the output string
    output = "{} {} {}, ساعت {}:{}".format(
        
        time_to_list[2],
        time_to_list[1],
        time_to_list[0],
        time.hour,
        time.minute,
    )

    # Convert Latin digits in the output to Persian digits
    return persian_numbers_convertor(output)
