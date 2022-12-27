# mypkg
* ロボットシステム学の練習リポジトリ
* これは、ROS2のパッケージです。

![test](https://github.com/tkzwtkmo419/mypkg/actions/workflows/test.yml/badge.svg)

# スクリプトの説明

* talker.pyからInt型のメッセージを送信して、listener.pyでInt型のメッセージを受信、表示するもの。
* 今回は、10秒間ノードを実行して、出力すべきものを出力するプログラム
* 具体例　　grep　"Listen: 10" の場合

```
$../test/test.bash
[listener-2] ...: Listen: 10
```

## テスト環境
* Ubuntu 22.04

## 必要なソフトウェア
* Python3.10

## ライセンス

* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます
* © 2022 Takazawa takumi
