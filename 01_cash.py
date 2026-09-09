import streamlit as st
import pandas as pd
import sqlite3
import time

st.title("Streamlit応用編 第1回：キャッシュ機能まとめ")

# ---------------------------------------------
# 1. CSVデータの読み込み (@st.cache_data)
# ---------------------------------------------
st.header("1. CSVの読み込み")
@st.cache_data
def load_data():
    df = pd.read_csv('data.csv')
    return df

try:
    data = load_data()
    st.write("data.csv の中身:")
    st.dataframe(data)
except FileNotFoundError:
    st.warning("data.csv が同じフォルダに見つかりません。")

# ---------------------------------------------
# 2. データベースの読み込み (スレッドエラー対策版)
# ---------------------------------------------
st.header("2. データベース(SQLite)の読み込み")
@st.cache_data
def load_db_data():
    conn = sqlite3.connect('database.db')
    df_db = pd.read_sql('SELECT * FROM users', conn)
    conn.close()
    return df_db

try:
    df_db = load_db_data()
    st.write("database.db の中身:")
    st.dataframe(df_db)
except Exception as e:
    st.warning(f"データベースの読み込みでエラーが発生しました: {e}")

# ---------------------------------------------
# 3. キャッシュの効果を時間で比較する
# ---------------------------------------------
st.header("3. キャッシュの効果測定")
st.write("※ わざと2秒間ストップする処理を入れています。")

@st.cache_data
def cached_function():
    time.sleep(2)
    return "✅ 【キャッシュあり】の処理が完了しました！"

def non_cached_function():
    time.sleep(2)
    return "❌ 【キャッシュなし】の処理が完了しました！"

# キャッシュありの計測
start_time_1 = time.time()
st.write(cached_function())
st.info(f"👉 キャッシュ使用時の処理時間: {time.time() - start_time_1:.2f}秒")

# キャッシュなしの計測
start_time_2 = time.time()
st.write(non_cached_function())
st.warning(f"👉 キャッシュ不使用時の処理時間: {time.time() - start_time_2:.2f}秒")

# ---------------------------------------------
# 4. キャッシュのクリア機能
# ---------------------------------------------
st.header("4. キャッシュのクリア")
st.write("ボタンを押すと記憶されたデータが消え、再読み込み時に再び2秒かかるようになります。")

# st.button は、ボタンが押されたときだけ True になります
if st.button("キャッシュをクリアする"):
    st.cache_data.clear()
    st.success("キャッシュをクリアしました！画面右上の「Rerun」かF5キーで再読み込みしてみてください。")