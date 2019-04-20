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
    while True:
        cities = ['chicago', 'new york city', 'washington']
        city = input('\nCITY:\nenter the city to be  analyzed (option from chicago, new york city, or washington):\n').casefold()
        if city in cities:
            break
        else:
            print('{} input entered for {}! please make another attempt!'.format('incorrect', 'city'))

    while True:
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        month = input("\nMONTH:\nenter the month to filter by (option from all, january, february, march, april, may, june),\n'all' to apply no month filter:\n").casefold()
        if month in months:
            break
        else:
            print('incorrect input entered for month! please make another attempt!')

    while True:
        days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        day = input("\nDAY:\nenter the day to filter by (option from  all, sunday, monday, tuesday, wednesday, thursday, friday, saturday),\n'all' to apply no day filter:\n").casefold()
        if day in days:
            break
        else:
            print('incorrect input entered for day! please make another attempt!')

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
    cities_df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    cities_df['Start Time'] = pd.to_datetime(cities_df['Start Time'])
    # extract month from Start Time to create new column
    cities_df['month'] = cities_df['Start Time'].dt.month
    # extract day of week from Start Time to create new column
    cities_df['day_of_week'] = cities_df['Start Time'].dt.weekday_name

    # filter by month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        cities_df = cities_df[cities_df['month'] == month]

    # filter by day of week
    if day != 'all':
        # filter by day of week to create the new dataframe
        cities_df = cities_df[cities_df['day_of_week'] == day.title()]

    return cities_df

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_file_info(cities_df):
    """Displays information on the accessed csv_file."""

    print('\nDisplaying the file information content ...\n')
    start_time = time.time()

    object_type = type(cities_df)
    print('The type of object:', object_type)
    print()

    object_columns = cities_df.columns
    print('Columns in object:\n', object_columns)
    print()

    object_elements = cities_df.dtypes
    print('Types of elements in object:\n', object_elements)
    print()

    object_shape = cities_df.shape
    print('Shape of object:', object_shape)
    print()

    object_dimension = cities_df.ndim
    print('Dimension of object:', object_dimension)
    print()

    object_size = cities_df.size
    print('Size of object:', object_size)
    print()

    user_request = input('\ndo you want to view the data\n')
    if user_request.lower() == 'yes':
        nrows = cities_df.shape[0]
        print('\nINITIAL VIEW:\nthe first 5 rows are:\n')
        print(cities_df[0:5])

        totalViewed = 5
        user_request_2 = input('\ndo you want to view more data? enter?\n')
        while(user_request_2.lower() == 'yes'):
            if totalViewed >= nrows:
                print('you have viewed all data')
                break
            print('\nNEXT VIEW:\nthe next 5 rows are:\n')
            print(cities_df[totalViewed : totalViewed + 5])
            user_request_2 = input('\ndo you want to view more data?\n')
            totalViewed += 5
            print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def time_stats(cities_df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # extract month from the Start Time column to create a month column
    cities_df['month'] = cities_df['Start Time'].dt.month
    # find the most common month
    common_month = cities_df['month'].value_counts().idxmax()
    common_month_count = cities_df['month'].value_counts().max()
    print('start month:', common_month)
    print('start month count:', common_month_count)
    print()

    # extract day of week from the Start Time column to create a day of the week column
    cities_df['day_of_week'] = cities_df['Start Time'].dt.weekday_name
    # find the most common day of the week
    common_day_of_week = cities_df['day_of_week'].value_counts().idxmax()
    common_day_of_week_count = cities_df['day_of_week'].value_counts().max()
    print('start day of week:', common_day_of_week)
    print('start day of week count:', common_day_of_week_count)
    print()

    # extract hour from the Start Time column to create an hour column
    cities_df['hour'] = cities_df['Start Time'].dt.hour
    # find the most common hour
    common_hour = cities_df['hour'].value_counts().idxmax()
    common_hour_count = cities_df['hour'].value_counts().max()
    print('tart hour:', common_hour)
    print('start hour count:', common_hour_count)
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(cities_df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # knowing the frequently used start station
    common_start_sta = cities_df['Start Station'].mode()[0]
    common_start_sta_count = cities_df['Start Station'].value_counts().max()
    print('start station:', common_start_sta)
    print('start station count:', common_start_sta_count)
    print()

    # knowing the frequently used end station
    common_end_sta = cities_df['End Station'].mode()[0]
    common_end_sta_count = cities_df['End Station'].value_counts().max()
    print('end station:', common_end_sta)
    print('end station count:', common_end_sta_count)
    print()

    # display most frequent combination of start station and end station trip
    start_end_trip = cities_df['Trip Duration'].mode()[0]
    start_end_trip_count = cities_df['Trip Duration'].value_counts().max()
    print('start and end stations trip: {}'.format(start_end_trip))
    print('start and end stations trip count: {}'.format(start_end_trip_count))
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(cities_df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = cities_df['Trip Duration'].sum()
    print('total:', str(total_travel_time) + ' secs')
    print()

    # display count travel time
    count_travel_time = cities_df['Trip Duration'].count()
    print('count:', count_travel_time)
    print()

    # display mean travel time
    average_travel_time = cities_df['Trip Duration'].mean()
    print('average:', str(average_travel_time) + ' secs')
    print()

    # display standard deviation travel time
    std_travel_time = cities_df['Trip Duration'].std()
    print('standard deviation:', str(std_travel_time) + ' secs')
    print()

     # display minimum travel time
    min_travel_time = cities_df['Trip Duration'].min()
    print('minimum:', str(min_travel_time) + ' secs')
    print()

    # display maximum travel time
    max_travel_time = cities_df['Trip Duration'].max()
    print('maximum:', str(max_travel_time) + ' secs')
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(cities_df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    object_columns = cities_df.columns

    # display counts of user types
    user_types = cities_df['User Type'].value_counts()
    print('count of user types:\n', user_types)
    print()

    # display counts of gender
    print('\nCalculating gender Stats...\n')
    if('Gender' in object_columns):
        sex = cities_df['Gender'].value_counts()
        print('Count of Gender:\n', sex)
        print()
    else:
        print('{} column not provided in the washington_csv file.'.format('gender')) 

    # display earliest, most recent, and most common year of birth
    print('\nCalculating birth year Stats...\n')
    if('Birth Year' in object_columns):
        # print earliest year of birth
        earliest_birth_year = cities_df['Birth Year'].min()
        print('Earliest year of birth:', earliest_birth_year)
        print()

        # print latest year of birth
        latest_birth_year = cities_df['Birth Year'].max()
        print('Latest year of birth:', latest_birth_year)
        print()

        # print most common year of birth
        popular_birth_year = cities_df['Birth Year'].mode()[0]
        print('popular year of birth:', popular_birth_year)
        print()
    else:
        print('whoa! the birth year column also not included in the washington_csv file.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        cities_df = load_data(city, month, day)

        data_file_info(cities_df)
        time_stats(cities_df)
        station_stats(cities_df)
        trip_duration_stats(cities_df)
        user_stats(cities_df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
