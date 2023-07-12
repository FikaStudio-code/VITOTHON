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

### 独自 flavour `jail` を作成する
このリポジトリには、サーバ（汎用的に使用）とルータ用の `jail` を作成するスクリプトは用意しています。これ以外に独自で `jail` を作成したい（例えば、Web サーバ用 `jail`）場合は、zenn[^1] の記事を参考にしてください。ルータ用 `jail` を作成する記事が特に参考になると思います。

### ネットワーク図を描く
`nwdiag`[^2] を使用して `jail` ネットワーク図を作成しています。詳しくは、`nwdiag` のドキュメントを参考にしてください。また、VITOTHON の動作に `nwdiag` は必要ではありません。`jail` ネットワークを作成する上で、図があった方が便利だったので追加しているだけです。

## リポジトリ構成
```
.
├── README.md
├── nwdiag     # ネットワーク図描画用フォルダ
├── shell      # jail 作成スクリプト
├── src        # VITOTHON 本体
└── test
```

## Reference
[^1]:https://zenn.dev/fikastudio
[^2]:http://blockdiag.com/ja/nwdiag/index.html