# VITOTHON
FreeBSD の `jail` を使用したネットワークとサーバ構築の練習ツールです。

作成時の環境
```
VirtualBox: 7.0
HostOS: macOS BigSur
GuestOS: FreeBSD 13.1-RELEASE
```

# ディレクトリ構成
```
.
├── README.md # これ
├── equipment.py # VITOTHON で使用
├── mkrouter.sh # ルータ用 jail 作成スクリプト
├── mkserver.sh # サーバ用 jail 作成スクリプト
├── nwdiag # ネットワーク図描画用フォルダ
├── shcommand.py # VITOTHON で使用
├── test.py
├── test2.py
├── test3.py
├── unjail.py # jail 削除スクリプト
└── vitothon.py VITOTHON で使用
```
# 参考文献
- zenn: https://zenn.dev/fikastudio