import sqlite3
from pathlib import Path
import csv

def initialize_database() -> None:
    # このコードは改変しないこと
    root_path = Path(__file__).parent

    db_path = root_path / 'my_movies.db'
    conn = sqlite3.connect(db_path)

    init_sql_path = root_path / 'init.sql'
    conn.executescript(init_sql_path.read_text())

    conn.close()


def main():
    initialize_database()

    # 以下から書き始めること！

    # CSVファイルの作成と初期化
    cfile = open("output.csv", "w")
    cfile.truncate(0)
    cfile.close()

    # 生成されたDBファイルに接続
    root_path = Path(__file__).parent
    db_path = root_path / "my_movies.db"
    conn_db = sqlite3.connect(db_path)
    cursor_db = conn_db.cursor()

    # クエリを生成
    query = "SELECT genre, SUM(income) as total \
            FROM my_movies \
            GROUP BY genre ORDER BY total DESC"

    # 戻り値をCSVに出力
    for record in cursor_db.execute(query):
        with open("output.csv", "a", newline="") as cfile:
            cline = csv.writer(cfile)
            cline.writerow(record)

if __name__ == '__main__':
    main()
