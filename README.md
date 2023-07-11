# VITOTHON
FreeBSD の `jail` を使用したネットワークとサーバ構築の練習ツールです。

作成時の環境
```
VirtualBox: 7.0
HostOS: macOS BigSur
GuestOS: FreeBSD 13.1-RELEASE
```

## 使用方法
### VITOHON を使用する
VITOTHON を使用する方法は 2 つあります。  
1. アプライアンスを使用する  
VITOTHON のアプライアンスは http://www.fikastudio.net/VITOTHON.ova にて公開しています。リンクからダウンロードして、VirtualBox などでインポートしてください。zenn[^1] に VITOTHON を構築する様子を記事にしているので、内部構成などはそちらを参照してください。
2. ソースコードを使用する FreeBSD 環境に配置する
このリポジトリを使用している FreeBSD 環境に配置して使用してください。使用する上で必要な準備は zenn[^1] の記事を参考にしてください。

### ネットワーク図を描く
### 

## ディレクトリ構成
```
.
├── README.md
├── equipment.py  # VITOTHON で使用
├── mkrouter.sh   # ルータ用 jail 作成スクリプト
├── mkserver.sh   # サーバ用 jail 作成スクリプト
├── nwdiag        # ネットワーク図描画用フォルダ
├── shcommand.py  # VITOTHON で使用
├── test.py
├── test2.py
├── test3.py
├── unjail.py     # jail 削除スクリプト
└── vitothon.py   # VITOTHON で使用
```

## 参考文献
[^1]:https://zenn.dev/fikastudio