import os
import duckdb

def create_table_from_csv(csv_file, conn):
    table_name = os.path.splitext(os.path.basename(csv_file))[0]
    conn.execute(f'CREATE TABLE "{table_name}" AS SELECT * FROM read_csv_auto(\'{csv_file}\')')

def create_tables_from_csv_directory(csv_directory, db_file):
    conn = duckdb.connect(db_file)
    for filename in os.listdir(csv_directory):
        if filename.endswith('.csv'):
            csv_file = os.path.join(csv_directory, filename)
            create_table_from_csv(csv_file, conn)
    conn.close()

if __name__ == "__main__":
    csv_directory = './rawdata'
    db_file = 'data.db'
    create_tables_from_csv_directory(csv_directory, db_file)
