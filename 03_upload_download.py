"""
=========================================================
【第3回の重要ポイント：ファイルのアップロードとダウンロード】

1. st.file_uploader（アップロード）
   - 何もアップロードされていない時は「None（空っぽ）」になります。
   - そのため、必ず「if uploaded_file is not None:（ファイルがある時だけ）」
     という条件分岐とセットで使います。

2. st.download_button（ダウンロード）
   - ボタンを押すと、指定したデータをパソコンに保存させることができます。
   - pandasのデータをCSVとしてダウンロードさせるには、
     一度文字データに変換し、さらに「encode('utf-8')」で
     コンピューター用のデータ（バイト列）にする必要があります。
=========================================================
"""

import streamlit as st
import pandas as pd

st.title("Streamlit応用編 第3回：ファイルのアップロードとダウンロード")

# ========================================================
# 1. 基本的なファイルアップロード ＆ ダウンロード
# ========================================================
st.write("### 1. 1つのファイルをアップロードして処理する")
st.write("パソコン内にあるCSVファイルをドラッグ＆ドロップしてみてください。")

# 【解説】 st.file_uploader について
# type="csv" と指定することで、CSVファイル以外は選べないように制限できます。
# 読み込まれたファイルデータは変数（uploaded_file）に入ります。
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type="csv")

# 【解説】 ファイルがアップロードされた場合のみ（Noneじゃない時のみ）実行する
if uploaded_file is not None:

    # アップロードされたファイルをpandasで読み込む
    # ※ index_col=0 をつけると、一番左の列を見出し（インデックス）として扱います
    df = pd.read_csv(uploaded_file, index_col=0)

    st.write("✅ アップロードされたデータ:")
    st.dataframe(df)

    # 簡単なデータ処理（describe関数でデータの平均や最大値などの統計情報を計算）
    processed_df = df.describe()

    st.write("📊 処理結果（統計情報）:")
    st.dataframe(processed_df)

    # 【解説】 ダウンロード用のデータ準備
    # to_csv() でCSV形式のテキストにし、encode('utf-8') でダウンロード可能な形式に変換します。
    csv_data = processed_df.to_csv().encode("utf-8")

    # 【解説】 st.download_button について
    # label: ボタンに表示する文字
    # data: ダウンロードさせる中身（さっき変換したもの）
    # file_name: ユーザーが保存する時のデフォルトのファイル名
    # mime: ファイルの種類（CSVの場合は 'text/csv'）
    st.download_button(
        label="この処理結果をダウンロードする",
        data=csv_data,
        file_name="processed_data.csv",
        mime="text/csv",
    )

st.divider()

# ========================================================
# 2. 複数ファイルのアップロード
# ========================================================
st.write("### 2. 複数のファイルを同時にアップロードする")

# 【解説】 accept_multiple_files=True を追加すると、複数ファイルを選択可能になります。
# 複数なので、変数（uploaded_files）の中身は「ファイルのリスト（配列）」になります。
uploaded_files = st.file_uploader(
    "複数のCSVファイルをアップロードしてください",
    type="csv",
    accept_multiple_files=True,
    key="multi_uploader",  # 上のアップローダーと区別するためのID
)

# 【解説】 リストの中にファイルが存在する場合
if uploaded_files:
    # for文を使って、リストの中のファイルを1つずつ取り出して処理します
    for file in uploaded_files:
        df_multi = pd.read_csv(file)

        # file.name で元のファイル名を取得できます
        st.write(f"📁 アップロードされたファイル: **{file.name}**")
        st.dataframe(df_multi)
