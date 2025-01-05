# 必要なライブラリ
- poetry(パッケージ管理)
```command
pip3 install poetry
```
poetryの初期化
```command
poetry init
```

- fastapiとuvicornをパッケージに追加
```command
poetry add fastapi
poetry add uvicorn
```


# APIのデプロイ先について
## 各種クラウドがAPI開発に必要な機能を提供
- サーバーの選択：頻度による使い分けはあり
-- EC2(サーバー)
-- Lanbda(サーバーレス)

- APIゲートウェイの使用
-- APIの管理や実行を容易にする仕組み
-- 
- ~~今回はDeta Cloudを使用~~

## SQL Alchemy
poetry add sqlalchemy
## SQLite
※macはデフォルトでインストール済み

