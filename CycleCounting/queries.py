import sqlite3
import pandas as pd
import datetime

db_path = r"S:\Warehouse dept\Inventory control\Reporting and dashboards\Cycle_Count\CycleCounting\DATABASE\cycle_couting.db"

#Get Bin's type and return warehouse
def return_warehouse(bin):
    warehouse = None
    my_dict = {
        'MKI':['A100', 'A110', 'A300', 'A310', 'A320', 'A330', 'A450', 'A500', 'A510', 'A710', 'A720', 'A730', 'A740','A750'],
        'JTS2':['B110', 'B300', 'B500','B510', 'B520','B750', 'B230'],
        'JTS1':['C110', 'C300', 'C330'],
        }
    for k,v in my_dict.items():
        if bin in v:
            warehouse = k
            break
    return warehouse
    
#Filter out data from database and sort
def GET_FROM_DATABASE(count, bin, level):
    warehouse = return_warehouse(bin)
    conn = sqlite3.connect(db_path)
    cmd = f'SELECT * FROM "{warehouse}" WHERE "Counted" = 0'
    df = pd.read_sql(cmd, conn).reset_index()
    filt = (df['Type'] == bin)
    df = df.loc[filt]
    filt = df['Storage Bin'].str[-2].eq(str(level))
    df = df[filt]
    df = df[['Storage Bin','Counted']].sort_values(by=['Counted', 'Storage Bin']).head(count)
    df.set_index('Storage Bin')
    conn.close()
    return df

#Calculate % and updated UI labels
def UPDATE_BUNS_LABELS(bin):
    warehouse = return_warehouse(bin)
    conn = sqlite3.connect(db_path)
    cmd = f'SELECT * FROM "{warehouse}" WHERE Type = "{bin}"'
    df = pd.read_sql(cmd, conn)
    series = pd.Series(df['Counted'])
    total = len(series)
    counted = (series != 0).sum()
    result = round((counted / total)*100, 2)
    return result

#Update UI Warehouse labels by calculating quantity per day
def UPDATE_WH_LABELS(warehouse):
    MKI = 203552
    JTS1 = 135254
    JTS2 = 204451
    year = datetime.date.today().year
    timestamp = pd.Timestamp(datetime.datetime(year, 12, 31))
    res = timestamp.today()
    days_left = int((timestamp - res).days)
    conn = sqlite3.connect(db_path)
    cmd = f'SELECT * FROM "{warehouse}"'
    df = pd.read_sql(cmd, conn)
    series = pd.Series(df['Counted'])
    if warehouse == 'MKI':
        total = MKI
    elif warehouse == 'JTS1':
        total = JTS1
    elif warehouse == 'JTS2':
        total = JTS2
    counted = (series != 0).sum()
    conn.close()
    return int((total - counted) / days_left)
