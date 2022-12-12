import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello, Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    # while loop for prompting the users
    while True:
        city = input("Please choose a city to explore: chicago, new york city, or washington:\n").lower()
        if city not in CITY_DATA:
            print("\n city was not found, please choose from the list")
            continue  
        else:
            print(f"\n you chose  {city.title()}.")
            break

    # get user input for month (all, january, february, ... , june)
    months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
    
    while True:
        month = input(
        "Please choose a month to filter by (january, february, march, april, may, june), or select all: ").lower()
        if month not in months:
            print("Enter a Valid Month")
            continue
        else:
            print(f"\n you chose  {month.title()}.")
            break
            

    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    
    days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    
    while True:
        day = input(
        "Please choose a day to filter by (sunday, monday, tuesday, wednesday, thursday, friday, saturday), or select all: ").lower()
        if day not in days:
            print("Enter a Valid Month")
            continue
        else:
            print(f"\n you chose  {day.title()}.")
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    #convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Start Month'] = df['Start Time'].dt.month
    df['Start Day'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Start Month'] == month]
    if day != 'all':
        df = df[df['Start Day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("most common month : ", df['Start Month'].mode()[0])

    # display the most common day of week
    print("most common day of week : ", df['Start Day'].mode()[0])

    # display the most common start hour
    print("most common start hour : ", df['Start Time'].dt.hour.mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("most commonly used start station : ", df['Start Station'].mode()[0])

    # display most commonly used end station
    print("most commonly used end station : ", df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    print("most frequent combination of start station and end station trip: \nStart Station: ", df[["Start Station","End Station"]].mode()['Start Station'][0],"\nEnd Station : ",df[["Start Station","End Station"]].mode()['End Station'][0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time: ", df["Trip Duration"].sum())

    # display mean travel time
    print("The mean travel time: ", df["Trip Duration"].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("counts of user types:\n", df['User Type'].value_counts())

    # Display counts of gender
    print("counts of gender:\n", df['Gender'].value_counts())


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = int(df['Birth Year'].min())
        print(f"Earliest birth year is: {earliest_birth_year}")

        recent_birth_year = int(df['Birth Year'].max())
        print(f"Most recent birth year is: {recent_birth_year}")

        common_birth_year = int(df['Birth Year'].mode()[0])
        print(f"Most common birth year is: {common_birth_year}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def prompt(df):
    """ iterating these prompts and displaying the next 5 lines of raw data at each iteration
    Arg:
    df - Pandas DF
    """
    x = 0
    answer = input("nWould you like to see the first 5 rows? Enter yes or no:\n").lower()
    while True:
        if answer == 'no':
            break
        print(df[x:x+5])
        answer = input("nWould you like to see next 5 rows? Enter yes or no:\n").lower()
        x += 5
        
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        prompt(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
