import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ダミーデータの作成
x = np.linspace(0, 10, 100)
y = np.sin(x)

# グラフの作成
fig, ax = plt.subplots()
ax.plot(x, y)

# Streamlitでグラフを表示
st.write('## Streamlitでグラフを表示')
st.pyplot(fig)


# ダミーデータの作成
df = pd.DataFrame({
    '列A': [1, 2, 3],
    '列B': [4, 5, 6]
})

# データフレームの表示
st.dataframe(df)

# ラジオボタン
選択肢 = st.radio(
    "好きなフルーツを選んでください",
    ('リンゴ', 'オレンジ', 'バナナ'))

# プッシュボタン
if st.button('クリックして下さい'):
    st.write('ボタンがクリックされました！')

# コンボボックス
選択 = st.selectbox(
    '好きな動物を選んでください',
    ('犬', '猫', '鳥'))

st.sidebar.title('サイドバーのタイトル')

# サイドバーにラジオボタンを配置
サイドバー選択肢 = st.sidebar.radio(
    "サイドバーで選択してください",
    ('オプション1', 'オプション2', 'オプション3'))