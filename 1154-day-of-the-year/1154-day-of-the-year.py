class Solution:
    def dayOfYear(self, date: str) -> int:
        Date = list(date)
        d1 = int(Date[9])
        d2 = 10*int(Date[8])
        m1 = int(Date[6])
        m2 = 10*int(Date[5])
        day = d1+d2
        month = m1+m2
        year = 1000*(int(date[0]))+100*(int(date[1]))+10*(int(date[2]))+(int(date[3]))
        if year % 4 == 0 and month >= 3 and year != 1900:
            day += 1
        if day == 29 and year % 4 == 0 and month == 2:
            return 31+day
        if month == 1:
            return day
        if month == 2:
            return 31+day
        if month == 3:
            return 59+day
        if month == 4:
            return 90+day 
        if month == 5:
            return 120+day
        if month == 6:
            return 151+day
        if month == 7:
            return 181+day
        if month == 8:
            return 212+day
        if month == 9:
            return 243+day 
        if month == 10: 
            return 273+day 
        if month == 11:
            return 304+day 
        if month == 12: 
            return 334+day