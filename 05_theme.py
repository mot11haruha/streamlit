"""
=========================================================
【第5回の重要ポイント：テーマのカスタマイズ】

1. config.toml による全体設定（推奨）
   - アプリ起動時に読み込まれる静的なデザイン定義。
   - プロジェクト直下の「.streamlit/config.toml」に配置する。
   - 配色（メイン色、背景色、文字色）やフォントを一元管理可能。

2. st.sidebar（サイドバー）
   - 画面左側の格納式パネルに入力部品を配置する機能。
   - 「st.sidebar.radio(...)」のように記述するだけで配置できる。

3. CSSインジェクションによる動的切り替え
   - st.markdown に <style> を渡し、選択に応じてスタイルを即時反映。
   - 現在のStreamlit仕様に合わせて、全体の背景・コンテナクラスへ適用。
=========================================================
"""

import streamlit as st

st.title("Streamlit応用編 第5回：テーマのカスタマイズ")

# ========================================================
# 1. サイドバーでテーマ切り替えを選択
# ========================================================
# 【解説】 st.sidebar について
# 通常の st.radio はメイン画面に出ますが、「st.sidebar.radio」と書くことで
# 画面左側の折りたたみ可能なサイドバー領域にウィジェットを設置できます。
selected_theme = st.sidebar.radio(
    "表示テーマを選択してください",
    options=["ライトモード", "ダークモード"]
)

# ========================================================
# 2. 選択に応じた動的CSSの適用
# ========================================================
# 【解説】 動的なスタイルの切り替え
# 選択された値（selected_theme）に応じて、埋め込むCSS文字列を分岐させます。
# ※ Streamlitのルート要素（.stApp）を指定して背景色と文字色を書き換えます。
if selected_theme == "ライトモード":
    custom_css = """
    <style>
    .stApp {
        background-color: #FFFFFF;
        color: #212529;
    }
    .custom-box {
        background-color: #F8F9FA;
        padding: 16px;
        border-radius: 8px;
        border: 1px solid #DEE2E6;
    }
    </style>
    """
else:
    custom_css = """
    <style>
    .stApp {
        background-color: #1E293B;
        color: #F8FAFC;
    }
    .custom-box {
        background-color: #334155;
        padding: 16px;
        border-radius: 8px;
        border: 1px solid #475569;
    }
    </style>
    """

# CSSをアプリに反映（unsafe_allow_html=True は必須）
st.markdown(custom_css, unsafe_allow_html=True)

# ========================================================
# 3. テーマ確認用のUI要素
# ========================================================
st.write(f"現在選択されているテーマ: **{selected_theme}**")

# カスタムクラスを適用したボックスの表示
st.markdown(
    f'<div class="custom-box">これは {selected_theme} が適用されたコンテナ要素です。</div>',
    unsafe_allow_html=True
)

st.write("") # スペース用の空行

# テーマ色確認用の標準ウィジェット
col1, col2 = st.columns(2)
with col1:
    st.text_input("テキスト入力欄", value="テスト文字列")
    st.button("アクションボタン")

with col2:
    st.slider("スライダー値の確認", min_value=0, max_value=100, value=40)
    st.checkbox("チェックボックス", value=True)