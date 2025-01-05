# 会議室予約アプリ

## 概要

このアプリは、会議室の予約を簡単に管理するためのツールです。バックエンドにはPythonのフレームワークであるFastAPIを使用し、フロントエンドはStreamlitを使用して構築されています。データベースにはSQLiteを使用しており、シンプルで軽量な設計が特徴です。

---

## 技術スタック

- **バックエンド**: Python
- **フレームワーク**: FastAPI
- **パッケージ管理**: Poetry
- **データベース**: SQLite
- **フロントエンド**: Streamlit
- **開発環境**: Mac

---

## セットアップ手順

### 1. 必要なツールのインストール

以下のツールがインストールされていることを確認してください。

- Python (>= 3.10)
- Poetry
- SQLite

他必要なパッケージは随時、portryに追加

### 2. リポジトリのクローン

```bash
git clone <リポジトリのURL>
cd <プロジェクトディレクトリ>
```

### 3. 依存関係のインストール

```bash
poetry install
```

### 4. バックエンドの起動

FastAPIサーバーを起動します。

```bash
poetry run uvicorn app.main:app --reload
```

サーバーが正しく起動すると、以下のURLでAPIドキュメントを確認できます。

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### 5. フロントエンドの起動

Streamlitアプリケーションを起動します。

```bash
poetry run streamlit run frontend/app.py
```



---

## 主な機能
1. **利用者登録**
   - 新規の利用者を登録できる。
2. **会議室登録**
   - 新規の会議室を登録できる。
3. **会議室一覧表示**
   - 登録されている会議室の一覧を表示。
4. **会議室の予約**
   - ユーザーが希望する日時で会議室を予約。
5. **予約状況の確認**
   - 各会議室の予約状況を簡単に確認可能。


---

## ディレクトリ構成

```
project_root/
├── app/
│   ├── main.py          # FastAPIのエントリーポイント
│   ├── cruds.py         # データベースのCRUD操作
│   ├── schemas.py       # スキーマ定義
│   ├── models.py        # データベースモデル
│   ├── database.py      # データベース接続設定
│   └── routers/         # APIのルーティング
│
├── frontend/
│   └── app.py           # Streamlitアプリケーション
├── poetry.lock          # Poetryのロックファイル
├── pyproject.toml       # Poetryの設定ファイル
└── README.md            # 本ドキュメント
```

---

## 開発時の注意点

- **ローカル環境**: 開発はMacを想定しています。他のOSを使用する場合、環境設定が異なる可能性があります。
- **パッケージ管理**: 必ずPoetryを使用して依存関係を管理してください。
- **データベース**: SQLiteは軽量で使いやすいですが、大規模なアプリケーションでは他のRDBMS（例: PostgreSQL）への移行を検討してください。

---

## 今後の改良案

- ユーザー認証機能の追加
- 利用者、会議室、予約の削除機能
- 会議室予約のステータスの追加（利用中、利用終了等）
- データベースの移行（例: PostgreSQL）

---

## 参考文献
Udemy
講師：  今西 航平 様
[Python初学者のネクストステップ！FastAPIによるWeb API開発講座](https://technoprojp.udemy.com/course/python-fastapi/learn/lecture/30217672#overview)


[FastAPI公式ドキュメント](https://fastapi.tiangolo.com/ja/)

