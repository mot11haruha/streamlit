"""
=========================================================
【第4回の重要ポイント：レイアウトのカスタマイズ】

1. st.columns（横並びレイアウト）
   - 数値を入れると均等分割: st.columns(2) -> 1:1 の比率
   - リストを入れると比率指定: st.columns([3, 1, 1]) -> 3:1:1 の比率
   - 各カラムは「with col1:」のようにブロック化して中身を記述

2. st.expander（折りたたみ）
   - クリックで開閉する領域を作成し、画面の情報過多を防止
   - 「with st.expander("タイトル"):」の中に隠したい要素を記述

3. st.markdown によるカスタムCSS
   - <style> タグを使って文字色や背景色、枠線を直接装飾
   - 「unsafe_allow_html=True」の指定が必須
=========================================================
"""

import streamlit as st

st.title("Streamlit応用編 第4回：レイアウトのカスタマイズ")

# ========================================================
# 1. 均等な2カラムレイアウト
# ========================================================
st.write("### 1. 画面を均等に2分割する (1:1)")

# 【解説】 st.columns(2) について
# 画面を横方向に2等分し、左側を col1、右側を col2 という変数に割り当てます。
col1, col2 = st.columns(2)

# 【解説】 with col1: について
# このブロック（字下げされた領域）内に書いた要素だけが「左カラム」に表示されます。
with col1:
    st.header("左側（カラム 1）")
    st.write("左側のエリアに配置されたテキストです。")
    st.button("左側のボタン", key="btn_left")

# 【解説】 with col2: について
# このブロック内に書いた要素が「右カラム」に表示されます。
with col2:
    st.header("右側（カラム 2）")
    st.write("右側のエリアに配置されたテキストです。")
    st.button("右側のボタン", key="btn_right")

st.divider()

# ========================================================
# 2. 幅の比率を指定した3カラムレイアウト
# ========================================================
st.write("### 2. カラムごとの幅（比率）を調整する (3:1:1)")

# 【解説】 比率の指定方法
# リスト形式 [3, 1, 1] で渡すと、全体の幅を「3 : 1 : 1」の比率で自動計算して3分割します。
# メインコンテンツを広くし、サイド情報やボタンを小さく配置したい時に使います。
col_main, col_sub1, col_sub2 = st.columns([3, 1, 1])

with col_main:
    st.header("メイン (幅3)")
    st.write("横幅が広いため、グラフやデータ表、長文の表示に適した領域です。")

with col_sub1:
    st.header("操作 (幅1)")
    st.write("幅1の細い領域です。")

with col_sub2:
    st.header("情報 (幅1)")
    st.write("幅1の細い領域です。")

st.divider()

# ========================================================
# 3. 折りたたみセクション（アコーディオン表示）
# ========================================================
st.write("### 3. 折りたたみセクション (st.expander)")

# 【解説】 st.expander について
# 初期状態では閉じられており、ユーザーがタイトルをクリックした時だけ中身が開きます。
# 補足情報や長い規約文、詳細設定などを目立たなく配置する際に役立ちます。
with st.expander("詳細情報を確認するにはここをクリック"):
    st.write("ここは普段は隠れている詳細情報のエリアです。")
    st.info("補足メモやツールの使い方など、必要な人だけが見ればよい情報を格納します。")

st.divider()

# ========================================================
# 4. カスタムCSSの適用
# ========================================================
st.write("### 4. カスタムCSSで装飾する")

# 【解説】 st.markdown と CSS
# HTMLの <style> タグを埋め込んでスタイルを定義します。
# ※「unsafe_allow_html=True」を付けないと、HTML/CSSタグがただの文字列として画面に表示されてしまいます。
st.markdown(
    """
    <style>
    /* 緑色のタイトル用クラス */
    .custom-header {
        font-size: 22px;
        color: #2E7D32;
        font-weight: bold;
        text-align: center;
        margin-bottom: 8px;
    }
    /* 薄い背景枠のコンテナ用クラス */
    .custom-container {
        background-color: #F1F8E9;
        padding: 16px;
        border-radius: 8px;
        border: 1px solid #C8E6C9;
        color: #1B5E20;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 定義したクラス名（custom-header）を呼び出して表示
st.markdown('<div class="custom-header">CSSを適用したカスタムヘッダー</div>', unsafe_allow_html=True)

# 定義したクラス名（custom-container）で囲んで背景付きブロックを作成
with st.container():
    st.markdown('<div class="custom-container">カスタムCSSによって背景色と角丸の枠線を付けたエリアです。</div>', unsafe_allow_html=True)