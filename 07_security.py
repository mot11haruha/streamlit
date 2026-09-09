"""
=========================================================
Streamlit応用編 第7回：認証とセキュリティ（統合版）
=========================================================

【実行とデプロイの必須チェック事項】
1. ローカルでの実行準備:
   このコードはOAuth機能のために外部ライブラリを使用します。
   ターミナルで以下を実行し、インストールしてください。
   $ pip install authlib

2. Streamlit Cloudへのデプロイ準備:
   GitHubにPushする前に、必ず `requirements.txt` を開き、
   末尾に `authlib` を追記してください。
   (例)
   streamlit
   pandas
   authlib

=========================================================
【学習ポイント】
- フォーム認証：st.text_input(type="password")で伏せ字化。
- シークレット管理：st.secretsを使って機密情報を安全に読み込む。
- OAuth認証：authlibを使い、Google等の外部アカウントでログイン。
=========================================================
"""

import streamlit as st
from authlib.integrations.requests_client import OAuth2Session

st.set_page_config(page_title="認証とセキュリティ", layout="centered")
st.title("Streamlit応用編 第7回：認証とセキュリティ")
st.write("タブを切り替えて、各セキュリティ機能の挙動を確認できます。")

tab1, tab2, tab3 = st.tabs(["1. フォーム認証", "2. シークレット管理", "3. OAuth認証"])

# ========================================================
# タブ1：シンプルなログイン機能
# ========================================================
with tab1:
    st.header("1. シンプルなログインフォーム")
    st.write("ユーザー名とパスワードを直接入力させる基本の認証方式です。")
    
    USER_CREDENTIALS = {"admin": "secret123", "guest": "guestpass"}
    
    username = st.text_input("ユーザー名")
    password = st.text_input("パスワード", type="password")
    
    if st.button("ログイン"):
        if USER_CREDENTIALS.get(username) == password:
            st.success(f"ようこそ、{username}さん！認証に成功しました。")
        else:
            st.error("ユーザー名またはパスワードが間違っています。")

# ========================================================
# タブ2：機密情報の管理 (st.secrets)
# ========================================================
with tab2:
    st.header("2. 機密情報の管理 (st.secrets)")
    st.write("`.streamlit/secrets.toml` に保存したAPIキーなどの機密情報を安全に読み込みます。")
    
    try:
        google_key = st.secrets["api_keys"]["google"]
        st.success("secrets.toml からAPIキーの読み込みに成功しました！")
        st.write(f"取得したキー: `{google_key[:5]}...`")
    except FileNotFoundError:
        st.warning("`.streamlit/secrets.toml` が見つかりません。")
    except KeyError:
        st.warning("`secrets.toml` 内に `[api_keys]` の `google` が設定されていません。")

# ========================================================
# タブ3：Google OAuth認証
# ========================================================
with tab3:
    st.header("3. Google OAuth認証")
    st.write("外部サービス（Google）のアカウントを利用したログイン機能です。")
    
    # st.secretsからOAuth用のキーを取得（設定されていない場合はダミー文字が入ります）
    client_id = st.secrets.get("google_client_id", "YOUR_CLIENT_ID")
    client_secret = st.secrets.get("google_client_secret", "YOUR_CLIENT_SECRET")
    authorization_endpoint = "https://accounts.google.com/o/oauth2/auth"
    token_endpoint = "https://accounts.google.com/o/oauth2/token"
    redirect_uri = "http://localhost:8501/"
    
    try:
        client = OAuth2Session(client_id, client_secret, redirect_uri=redirect_uri)
        authorization_url, state = client.create_authorization_url(authorization_endpoint)
        
        st.markdown(f"**[🔗 Googleアカウントでログインする]({authorization_url})**")
        
        # リダイレクト後のコード取得処理（最新の st.query_params を使用）
        if "code" in st.query_params:
            code = st.query_params["code"]
            st.success(f"Googleからの認証コードを取得しました: `{code[:10]}...`")
            st.info("※実際のアプリでは、このコードを使ってアクセストークンを取得し、ログイン処理を完了させます。")
            
    except Exception as e:
        st.error(f"OAuthの設定エラー: {e}")