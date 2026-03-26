import pandas as pd

def loading(file_path):
    df = pd.read_csv(file_path, index_col='Name')
    return df

def cleaning(df):

    df = df.drop_duplicates()
    df = df.reset_index().drop_duplicates(subset='Name').set_index('Name')

    return df

def stats(df):
    df['Salary']=df['Salary'].fillna(df['Salary'].median())

    df['Age']=df['Age'].fillna(df['Age'].median())

    count = df.isna().sum()
    print(f'---Count of NaN after filling age and salary---\n{count}')

    oldandrich = (df[(df['Age']>=40) & (df['Salary']>= 90000.0)])
    print(f'---Rich and old workers---\n{oldandrich}')

    meansalary = df.groupby('Position')['Salary'].mean()
    print(f'---Mean salary by position---\n{meansalary}')

    unique_positions = df['Position'].unique().tolist()
    print(f'---Unique positions---\n{unique_positions}')

    return df

def search_employee(df):
    userinput = input('Enter your name: ')
    result = df[df.index.str.contains(userinput, case=False, na=False)]

    if not result.empty:
        print(result)
    else:
        print(f"Employee '{userinput}' not found!")

def main():
    file_name = 'data.csv'
    df = loading(file_name)
    df = cleaning(df)
    while True:
        print('\n--- MENU ---')
        print('1. Basic Statistics')
        print('2. Search Employee')
        print('3. Save and Exit')

        choice = input('Enter your choice: ')
        if choice == '1':
            stats(df)
        elif choice == '2':
            search_employee(df)
        elif choice == '3':
            df.to_csv('data_cleaned.csv', index=True)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()