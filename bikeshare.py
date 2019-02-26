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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # create city variable and a while loop to keep prompting user until a valid city from the CITY_DATA dictionary is entered. Also change the city input to lowercase.
    city = ''
    while city not in CITY_DATA:
        city = input('Would you like to see data for Chicago, New York City, or Washington?').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    #create a months list including only months from january to june and 'all'.
    MONTHS =['all','january', 'february', 'march', 'april', 'may', 'june']
    #create a month variable to be used in the while loop.
    month = ''
    # create a while loop to keep prompting user until a valid month from the months list is entered. Also change the month input to lowercase.
    while month not in MONTHS:
        month = input('Filter data by which month - January, February, March, April, May, June? or all?').lower()  
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #create a days list including the 7 days of the week and 'all'.
    DAYS = ['all','sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    #create a day variable to be used in the while
    day = ''
    # create a while loop to keep prompting user until a valid day from the days list is entered. Also change the day input to lowercase.
    while day not in DAYS:
        day = input('Filter data by which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday? or All?').lower()
        

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # convert the start time column to datetime 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month from the start Time column to create an month column
    df['month'] = df['Start Time'].dt.month
    # find the most common month 
    most_common_month = df['month'].mode()[0]
    # display the most common month 
    print('Most Common Month:', most_common_month)

    # TO DO: display the most common day of week
    # convert the start time column to datetime 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract day of week from the start Time column to create a day of week column
    df['day_of_week'] = df['Start Time'].dt.day
    # find the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    # display the most common day of week
    print('Most Common Day of Week:', most_common_day)

    # TO DO: display the most common start hour
    # convert the start time column to datetime 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from the start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour of day
    most_common_hour = df['hour'].mode()[0]
    # display the most common hour of day 
    print('Most Common Hour:', most_common_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # find the most common start station
    most_common_start_station = df['Start Station'].mode()[0]
    # display the most common start station
    print('Most Common Start Station:', most_common_start_station)

    # TO DO: display most commonly used end station
    # find the most common end station
    most_common_end_station = df['End Station'].mode()[0]
    # display the most common start station
    print('Most Common End Station:', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    # find the sum of the most common start station and end station
    most_common_trip = df["Start Station"] + " to " + df["End Station"]
    # display the most common trip
    print("Most Common Trip:", most_common_trip.mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # convert the start time column to datetime 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # convert the end time column to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])
    # create and calculate travel time column
    df['travel_time'] = df['Start Time'] - df['End Time']
    # convert the travel time column to datetime 
    df['travel_time'] = pd.to_datetime(df['travel_time'])
    # extract hour from the travel Time column to create an travel hour column
    df['travel_hour'] = df['travel_time'].dt.hour
    # Calculate the sum of Travel Time 
    total_travel_time = df['travel_hour'].sum()
    # display total travel time
    print('Total Travel Time:', total_travel_time)
    
    
    # TO DO: display mean travel time
    # Calculate the mean of Travel Time 
    average_travel_time = df['travel_hour'].mean()
    # display the mean travel time
    print('Average Travel Time:', average_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # find count of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Types:', user_types)


    # TO DO: Display counts of gender
  
    #create conditional statement to only display gender data if the 'Gender' column is found else display no gender data for Washington since no gender data is available in the Washington csv.
    if 'Gender'in df:
        gender = df['Gender'].value_counts()
        print('Counts of Gender:', gender)
    else:
        print('No Gender data for Washington.')
    # TO DO: Display earliest, most recent, and most common year of birth
    # Earliest year of birth
    #create conditional statement to only display no birth year data if the 'Birth Year' column is found else display no birth year data for Washington since no birth year data is available in the Washington csv.
    if 'Birth Year' in df:
        earliest_year = min(df['Birth Year'])
        print('Earliest Year of Birth:', earliest_year)
    
    # Most recent year of birth 
        recent_year = max(df['Birth Year'])
        print('Most Recent Year of Birth:', recent_year)
    # Most common year of birth
        common_year = df['Birth Year'].mode()[0]
        print('Most Common Year of Birth:', common_year)         
    else:
        print('No Birth Year data for Washington.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# the show_raw_data() function should keep asking user if they like to display 5 more records from the selected city biking dataset.
def show_raw_data(df):
    i = 0
    while True:
        x = input('Yes or No? Would you like to view a few rows of the dataset?').lower()
        if x != 'yes':
            break
        else:
            i += 5
            print(df.head(i))
           
 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

            


            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
