# app_engine_django

## install environment

```bash
# 開発環境をインストール
pipenv lock
pipenv sync --dev

```

## check audity

```bash
pipenv check
```


## deploy

現在gaeがPipfile, Pipfile.lockをサポートしていないため
生成時のみ使う。

gaeデプロイの場合
エントリポイントを指定しない限り、requirements.txt ファイルに gunicorn を含めないでください。


# Dでバックグラウンド起動。(デーモンとして起動)
# デバッグ目的ならDいらない。
# --configでgunicornの設定ファイルの指定, 非同期処理なのでuvicornがいる。
GUNICORN_CMD_ARGS="--bind=127.0.0.1 --workers=3" gunicorn config.asgi -k uvicorn.workers.UvicornWorker --config ./gunicorn-cfg.py -D

--ssl-keyfile ./keys/127.0.0.1-key.pem --ssl-certfile ./keys/127.0.0.1.pem --port 443 


プロジェクト配下で下記のようにする。
そうで無いとdjangoが落ちたら、再起動かからない。

```shell
# Dでバックグラウンド起動。(デーモンとして起動)
# デバッグ目的ならDいらない。
# --configでgunicornの設定ファイルの指定, 非同期処理なのでuvicornがいる。
# gunicornの引数は絶対パス区切り
GUNICORN_CMD_ARGS="--bind=127.0.0.1 --workers=3" gunicorn config.asgi -k uvicorn.workers.UvicornWorker --config ./gunicorn-cfg.py -D 

--ssl-keyfile
--ssl-certfile
--port 443
# wsgiでやる場合。
GUNICORN_CMD_ARGS="--bind=127.0.0.1 --workers=3" gunicorn config.wsgi --config ./gunicorn-cfg.py  -D 
# したで削除
pkill gunicorn
```

gunicorn -w 1 -k uvicorn.workers.UvicornWorker package_name.module_name:app

[django systemctlの設定](https://chuna.tech/detail/95/)

```shell
# 
pip install --user -r requirements.txt
# requirements.txt更新
pipenv lock -r >> requirements.txt
```

https://buildersbox.corp-sansan.com/entry/2021/05/21/110000
