from datetime import date, datetime,timedelta,timezone
from dateutil.relativedelta import relativedelta

class TimeDetails:
    """
    Offset from UTC: Each time zone is defined by its difference from UTC. For example:
    UTC+0: This is essentially UTC itself.
    UTC+3: This time zone is 3 hours ahead of UTC.
    UTC-5: This time zone is 5 hours behind UTC.
    """
    def TimeDelta(self):
        """
        timedelta:
        The timedelta class from the datetime module represents a duration or difference between two dates or 
        times. You can use it to perform operations such as adding or subtracting time from a given datetime 
        object.
        """
        # Current time
        now = datetime.now()
        print("Current time:", now)

        # Create a timedelta of 6 hours
        delta = timedelta(hours=-6)
        print("timedelta(hours=-6):", delta)

        # Subtract 6 hours from the current time
        past_time = now + delta
        print("Time 6 hours ago:", past_time)
        

    def TimeZone(self):
        """
        The timezone class from the datetime module represents a fixed offset from UTC. You can use it 
        to create a timezone-aware datetime object.
        """
        # Create a timezone object for UTC-6 hours
        tz = timezone(timedelta(hours=-6))

        # Current time in UTC
        now_utc = datetime.now(timezone.utc)
        print("Current UTC time:", now_utc)

        # Convert current UTC time to the new timezone
        local_time = now_utc.astimezone(tz)
        print("Local time in UTC-6:", local_time)
        

    def Details(self):
        """
        Local Time: Within a time zone, the local time is calculated by adding or subtracting the time zone's 
        offset from UTC.

        Daylight Saving Time (DST): Some regions adjust their clocks forward by one hour during the summer 
        months to make better use of daylight. This means the time zone's offset from UTC can change depending 
        on the time of year.
  
        Example of Time Zones
        Eastern Standard Time (EST) is UTC-5. During the summer, this time zone becomes Eastern Daylight Time (EDT), which is UTC-4 because of DST.
        Central European Time (CET) is UTC+1. During DST, it changes to Central European Summer Time (CEST), which is UTC+2.
        """
        

    def pytz_TimeZone(self):
        """
        pytz provides accurate and up-to-date time zone information, including handling daylight saving
        time changes.
        pytz.timezone('US/Eastern'): Creates a timezone object for Eastern Time in the US.
        """
        import pytz

        # Create a timezone object for US/Eastern
        eastern = pytz.timezone('US/Eastern')

        # Get the current UTC time
        now_utc = datetime.now(pytz.utc)

        # Convert the current UTC time to Eastern Time
        now_eastern = now_utc.astimezone(eastern)

        print("Current time in UTC:", now_utc)
        print("Current time in Eastern Time:", now_eastern)
        
        # ------------------Timezone Object Creation:--------------------------------
        # Create a timezone object for Eastern Time (ET)
        ET = pytz.timezone('US/Eastern')
        print("pytz.timezone('US/Eastern') = ", ET)

        # Create a datetime object for July 1, 2024, with Eastern Time zone information
        start_date_i = datetime(2024, 7, 1, tzinfo=ET)

        print("Datetime with timezone:", start_date_i)
        """
        ET = pytz.timezone('US/Eastern') creates a timezone object for the Eastern Time Zone, including both standard time and daylight saving time rules.
        Assigning Timezone Information:

        datetime(2024, 7, 1, tzinfo=ET) creates a datetime object for July 1, 2024, and attaches the ET timezone object to it.
        """


    def relativedelta_Month_opp(self):
        # relativedelta accurately accounts for the different number of days in each month and leap years.
        """
        relativedelta is part of the dateutil library and provides more advanced relative date manipulations.
        
        relativedelta(months=1): Represents a time difference of one month.
        Usage: Used with datetime objects to add or subtract a month accurately, taking into account 
        variations in month lengths and leap years.
        Examples: Demonstrates adding and subtracting months, as well as handling special cases like 
        end-of-month dates.
        """
        # Current date
        now = datetime.now()
        print("Current date:", now)

        # RelativeDelts
        R_delta = relativedelta(months=1)
        print(R_delta)
        
        # Subtracting one month
        past_date = now - relativedelta(months=1)
        print("Date one month ago:", past_date)
        
        """
        Part of: dateutil library (third-party).
        Focus: Relative, calendar-based adjustments (months, years, etc.).
        """

    def only_timedelta(self):
        # timedelta is a class in Python's built-in datetime module. It represents a fixed duration of time and is suitable for simple arithmetic operations with dates and times.
        #timedelta doesn’t handle months or years directly, so you have to approximate or handle these durations manually.
        # Current date and time
        now = datetime(2024, 9, 16, 12, 0, 0)
        print("Current date and time:", now)

        # Create a timedelta of 1 month (approximated as 30 days)
        delta = timedelta(days=30)
        one_month_ago = now - delta
        print("Date and time 1 month ago:", one_month_ago)

        """
        Part of: datetime module (built-in).
        Focus: Fixed time intervals (days, seconds, etc.).
        Limitation: Does not handle months or years in a calendar-aware way.
        """

if __name__=='__main__':
    obj = TimeDetails()
    
    # obj.TimeDelta()
    
    # obj.TimeZone()
    
    # obj.pytz_TimeZone()
    
    # obj.relativedelta_Month_opp()
    
    obj.only_timedelta()
    
    



    