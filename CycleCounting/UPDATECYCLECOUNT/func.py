import os
import sqlite3

path = r"S:\Warehouse dept\Inventory control\Reporting and dashboards\Cycle_Count\CycleCounting\DATABASE\cycle_couting.db"


def username():
    username = os.path.expanduser('~')
    print('##############################################')
    print("Hello username: " + os.path.split(username)[-1])
    print('##############################################')
    return username


def update_database(path, wh):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    for k, v in wh.items():
        for row in v:
            cur.execute(f'UPDATE "{k}" SET "Counted" = 1 WHERE "Storage Bin" = "{row}";')
            print(f'Database table "{k}" updated with Storage Bin: "{row}"') 
        conn.commit()
    cur.close()
    conn.close()

def update_cycle_counting(df):
    reg = 'A-[a-zA-Z]\d{2}-\d{3}-\d{2}.\d{2}|E[a-zA-Z]\d{3}-\d{4}|M[a-zA-Z]\d{3}-\d{4}|SAFE\d*'
    MKI = df[df.str.contains(reg)].reset_index(drop = True)
    reg = 'C-[a-zA-Z]\d{2}-\d{3}-\d{2}.\d{2}'
    JTS1 = df[df.str.contains(reg)].reset_index(drop = True)
    reg = 'B-[a-zA-Z]\d{2}-\d{3}-\d{2}.\d{2}|^BCSAH-\d-[A-Z].\d.\d'
    JTS2 = df[df.str.contains(reg)].reset_index(drop = True)
    wh = {'MKI':MKI, 'JTS1':JTS1, 'JTS2':JTS2}
    update_database(path, wh)
    
def db_connect(path):
    userhome = username()
    conn = sqlite3.connect(path)
    try:
        conn = sqlite3.connect(path)
        print(f'{userhome} is connected to Databse located in {path} using sqlite3 version {sqlite3.version}')
    except sqlite3.OperationalError  as e:
        print(f'Error occured while connecting to database: {e}')
    return conn
