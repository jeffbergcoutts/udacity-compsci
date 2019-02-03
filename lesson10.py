days_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    return False

def days_between_dates(y1, m1, d1, y2, m2, d2):
    if y2 < y1:
        return "dates not valid"
    elif y2 == y1:
        if m2 < m1:
            return "dates not valid"
        elif m2 == m1:
            if d2 < d1:
                return "dates not valid"
            else:
                return d2 - d1
        elif m2 > m1:
            # add up all the days between the 2 months
            days_in_first_month = days_of_months[m1 - 1] - d1
            return days_in_first_month + sum(days_of_months[m1:m2-1]) + d2
    elif y2 > y1:
        days_in_first_month = days_of_months[m1 - 1] - d1
        rest_of_days_in_year = sum(days_of_months[m1:])
        days_in_years_inbetween = sum(days_of_months) * ((y2-1)-y1)
        days_in_final_year = sum(days_of_months[:m2-1])
        return days_in_first_month + rest_of_days_in_year + days_in_years_inbetween + days_in_final_year + d2


print days_between_dates(2012, 2, 15, 2019, 2, 18)
