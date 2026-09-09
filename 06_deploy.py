"""
=========================================================
【第6回の重要ポイント：デプロイと共有】

デプロイ（公開）には、主に以下の2つの準備が必要です。
1. GitHubにコードをアップロードする
2. 必要なライブラリの一覧（requirements.txt）を用意する

今回はこれまでの総復習として、Streamlitのレイアウト機能
（st.tabs, st.checkbox）を駆使した「デプロイ手順書アプリ」になっています。
=========================================================
"""

import streamlit as st

st.set_page_config(page_title="デプロイ手順書", layout="centered")
st.title("Streamlit応用編 第6回：デプロイと共有")
st.write("作成したアプリをWeb上に公開するための手順書・チェックリストです。")

# 【解説】 st.tabs について
# 複数の画面をタブで切り替えられるようにする、非常に便利なレイアウト機能です。
tab1, tab2, tab3 = st.tabs(["1. 必須ファイルの準備", "2. GitHubへアップロード", "3. Streamlit Cloudで公開"])

# ========================================================
# タブ1：必須ファイルの準備
# ========================================================
with tab1:
    st.header("1. 必須ファイルの準備")
    st.write("Streamlit Cloudのサーバーが「どのパッケージをインストールすればいいか」を知るために、以下のファイルが必要です。")
    
    st.info("💡 `requirements.txt` をプロジェクトのフォルダ内に作成してください。")
    
    st.write("**【requirements.txt の中身の例】**")
    st.code("""
    streamlit
    pandas
    """, language="text")
    
    st.write("※ これまで作ったアプリを動かすのに必要な `import 〇〇` のリストを書きます。")
    
    check1 = st.checkbox("requirements.txt を作成した", key="chk1")

# ========================================================
# タブ2：GitHubへアップロード
# ========================================================
with tab2:
    st.header("2. GitHubへアップロード")
    st.write("コードを無料で保存・管理できる「GitHub」にアプリのファイルをアップロードします。")
    
    with st.expander("📝 コマンドライン（ターミナル）でのアップロード手順"):
        st.code("""
        git init
        git add .
        git commit -m "初めてのStreamlitアプリ"
        git branch -M main
        git remote add origin <あなたのリポジトリURL>
        git push -u origin main
        """, language="bash")
        
    st.write("※ VS Codeの「ソース管理」機能（左側の枝分かれアイコン）を使うと、コマンドを打たずにクリックだけでアップロードすることも可能です。")
    
    check2 = st.checkbox("GitHubのリポジトリにコードと requirements.txt をPushした", key="chk2")

# ========================================================
# タブ3：Streamlit Cloudで公開
# ========================================================
with tab3:
    st.header("3. Streamlit Cloudで公開")
    st.write("GitHubとStreamlit Cloudを連携させて、世界に公開します。")
    
    st.markdown("""
    1. [Streamlit Community Cloud](https://share.streamlit.io/) にアクセスしてログイン。
    2. **「New app」** をクリック。
    3. 自分のGitHubリポジトリを選択。
    4. 実行するメインのファイル（例: `01_cache.py` や `app.py`）を指定。
    5. **「Deploy!」** をクリック。
    """)
    
    check3 = st.checkbox("Deployボタンを押し、風船が飛ぶ（成功）画面を見た！", key="chk3")

st.divider()

# 全てのチェックボックスにチェックが入った時だけ、お祝いメッセージを出す
if check1 and check2 and check3:
    st.success("🎉 デプロイ完了おめでとうございます！発行されたURLを共有すれば、誰でもあなたのアプリを使えます。")
    st.balloons() # 画面に風船を飛ばすStreamlitの隠し機能