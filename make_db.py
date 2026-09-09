import sqlite3

# データベースに接続（ファイルがなければ自動で新規作成されます）
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# テスト用のテーブルを作る
cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT,"
    " age INTEGER)"
)

# テスト用のデータをいくつか入れる
cursor.executemany(
    "INSERT INTO users (name, age) VALUES (?, ?)",
    [("Taro", 25), ("Jiro", 30), ("Hanako", 22)],
)

# 変更を保存して閉じる
conn.commit()
conn.close()

print("database.db の作成が完了しました！")