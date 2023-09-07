# Imports
#~~~~~~~~~~~~~~~



#~~~~~~~~~~~~~~~
# Acquire (52,442 PROPERTIES TOTAL AT START = TRUE)
#~~~~~~~~~~~~~~~
# How did I acquire the data

def get_zillow():
    '''This function imports zillow 2017 data from MySql codeup server and creates a csv
    
    argument: df
    
    returns: zillow df'''
    filename = "zillow.csv"
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
    else:
        query = """
        SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, lotsizesquarefeet, fips, transactiondate, garagecarcnt, garagetotalsqft
        FROM properties_2017
        JOIN propertylandusetype USING (propertylandusetypeid)
        JOIN predictions_2017 USING (parcelid)
        WHERE propertylandusetypeid like '261';
        """
        connection = get_db_url("zillow")
        df = pd.read_sql(query, connection)
        df.to_csv(filename, index=False)
    return df

#~~~~~~~~~~~~~~~
# Prep 
#~~~~~~~~~~~~~~~
# How did I prep the data
def prep_zillow(df):
    '''takes the zillow dataframe, drops nulls, drops transactiondate, changes column names, 
    and replaces null values in garage columns

    argument: df

    returns: clean_df
    '''
    # rename columns
    df.rename(columns={'fips': 'county', 'bedroomcnt': 'bedrooms', 'garagecarcnt': 'garage_fits', 'bathroomcnt': 'bathrooms', 'garagetotalsqft': 'garage_area', 'calculatedfinishedsquarefeet': 'finished_area', 'lotsizesquarefeet': 'lot_area', 'taxvaluedollarcnt': 'home_value'}, inplace=True)
    
    # garage_fits change nan, dtype=int, fill nulls for garage_area
    df.garage_fits = df.garage_fits.fillna(0).astype(int)
    df.garage_area = df.garage_area.fillna(0)
    
    # take care of null vals for yearbuilt, finished_area, lot_area, and home_value
    df.dropna(axis=0,inplace=True)
    # change yearbuilt type to int
    df.yearbuilt = df.yearbuilt.astype(int)
    # drop transactiondate
    df = df.drop(columns='transactiondate')
    # start with county, change unique values
    df.county = df.county.map({6037: 'LA', 6059: 'Orange', 6111: 'Ventura'})
    # change bedroom dtype to int and drop values 0 and everything above 8
    df.bedrooms = df.bedrooms.astype(int)
    df.drop(df[df['bedrooms'] > 8].index, inplace=True)
    df.drop(df[df['bedrooms'] == 0].index, inplace=True)
    return df


# Drop Outliers

# How did I separate into counties (This AFTER SPLIT)

# SPLIT

def split_data(df):
    '''
    split continuouse data into train, validate, test; No target variable

    argument: df

    return: train, validate, test
    '''

    train_val, test = train_test_split(df,
                                   train_size=0.8,
                                   random_state=1108,
                                   )
    train, validate = train_test_split(train_val,
                                   train_size=0.7,
                                   random_state=1108,
                                   )
    
    print(f'Train: {len(train)/len(df)}')
    print(f'Validate: {len(validate)/len(df)}')
    print(f'Test: {len(test)/len(df)}')
    

    return train, validate, test

# THEN IMPUTE

# Visuals

# Stat Functions

#~~~~~~~~~~~~~~~
# Model
#~~~~~~~~~~~~~~~

# Baseline?

# Model 1 ONLY USE BEDROOMS, BATHROOMS, AND HOME_VALUE

# Model 2

# Model 3

# Test Best




