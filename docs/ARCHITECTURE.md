# 仕組み（PDFと画像ができるまで）

作業手順は [WORKFLOW.md](WORKFLOW.md)。ここでは、コードがどう動いているかを説明する。

## 全体の流れ

```
英語の本文 (Markdown)         tools/guides.py の設定
  rental-guide-en.md            題名・扉の説明・図・ひと言コラム
  moving-in-guide-en.md                 │
        │                                │
        └──────────► tools/make_pdf.py ◄─┘
                         │  1. Markdown を HTML に変換
                         │  2. 章ごとに「扉」「章バー」「図」「コラム」を差し込む
                         │  3. 表紙・目次を前に付ける
                         │  4. CSS（紙面デザイン）を付けて HTML を書き出す
                         │  5. Chrome（Playwright）で PDF に印刷
                         ▼
                   *.pdf（Payhip に載せる）
```

## 1. 本文 → HTML（make_pdf.py）

- 本文は Markdown。`## Chapter N: タイトル` が章の区切り、`## Appendix A: …` が付録の区切り。
- `☐ 項目` の行は、チェックボックス付きの行（`<div class='ck'>`）に変換する。
- 引用ブロック（メール文面）の中の箇条書きは、前後に空行を足して、きれいに崩れないようにする。
- HTML に変換したあと、`<h2>` ごとに分割し、章（`Chapter N`）ごとに次を差し込む。
  - **扉（opener）**: 濃紺の全面ページ。章番号、題名、説明、立体イラスト、3つの数字タイル。
  - **章バー（chbar）**: 本文ページの上部に出る小さな見出し。
  - **図（FIGS）**: 章ごとに、設定で指定した図（SVG）。
  - **コラム（CALLOUT）**: 章の終わりの「TIP」「CAUTION」の囲み。
- 先頭に、**表紙**と**目次・免責**を付ける。

## 2. ガイドの設定（tools/guides.py）

ガイドごとに、関数（`rental()`、`movein()`）が次のキーを持つ辞書を返す。`make_pdf.py` は引数（`rental` / `movein`）で選ぶ。

| キー | 意味 |
|---|---|
| `md`, `out` | 本文ファイルと出力PDF名 |
| `cover_title`, `cover_sub`, `badges` | 表紙の文字 |
| `titles`, `summary`, `tiles` | 章の題名、扉の説明、扉の下の3つの数字 |
| `figs` | 章番号 → 図（SVGの文字列） |
| `callout` | 章番号 → ("tip" か "warn", 見出し, 本文) |
| `scene_map`, `tags` | 章番号 → 使う立体イラストの番号、ラベル文字（例: "30 DAYS"） |
| `n_ch`, `ap_last`, `toc_extra` | 章の数、付録の最後の文字、目次の付録の行 |

新しいガイドを作るときは、本文のMarkdownを書き、`guides.py` に関数を足し、`CONFIGS` に登録する。

## 3. 立体イラスト（tools/iso.py）

- **等角投影（アイソメ）** を自前で計算している。`Iso` クラスの `P(x, y, z)` が、3次元の点を画面の2次元に変換する。
- 部品: `box`（3つの面を明るさを変えて塗る直方体）、`cyl`（円柱）、`sphere`、`flat`（平らな面）、`text_floor` / `text_left`（面に貼る文字）、`shadow`（影）。
- **描く順番（painter's algorithm）**: 各部品に並べ替え用のキー（`x + y + 高さ` のような値）を付け、小さい順に描く。奥のものが先、手前のものが後になる。
- `scene(n)` が、章の扉用のミニチュア（番号ごとに1つ）を返す。0〜9は賃貸ガイド用、10（電気・水道・ガス・Wi-Fi）と11（ゴミ箱）はMoving In用。
- `cover_art()` は表紙の街並み。`mini(kind)` は家具つきの間取り（1R、1DK、1LDK、2LDK）。

## 4. 本文の図（tools/figs2.py と tools/art.py）

- `figs2.py` が本文の図を作る。立体感のあるカード（`card`）、番号の球（`ball`）、アイコン（`glyph`）を共通部品として使う。
  - 賃貸ガイド用: 流れ、関係者、費用（立体の棒グラフ）、書類、マイソク、入居、解約までの流れ。
  - 汎用: `columns`（日程の列）、`presence`（誰が家にいる必要があるか）、`bring`（持ち物カード）。
- `fig(...)`（枠と見出し）とアイコンは `art.py` の共通部品。`plan_1k_iso()` は1Kの立体断面図（等角投影の自前の描画）。

## 5. 画像（表紙、サンプル、ピン）

| スクリプト | 出力 | 方法 |
|---|---|---|
| `tools/make_cover.py`, `tools/make_cover_movein.py` | `cover.png`, `cover-movein.png` | `tools/cover.py` の共通レンダラでHTMLをChromeで開いてスクリーンショット |
| `tools/make_pins.py` | `marketing/pins/*.png`（1000×1500） | HTML（`scene(n)` ＋見出し）をスクリーンショット |
| `marketing/mk2.py` ほか | `marketing/samples/card_*.png` | PDFの該当ページを高解像度で切り出し、紺の枠に載せる |

## 6. フォントとネットワーク

- Fraunces（見出し）、Inter（本文）、Noto Sans JP と Noto Serif JP（日本語）を、Google Fonts から読み込む。
- PDF作成と画像作成のときは、ネットワークが必要（`wait_until='load'` で読み込み、続けて `document.fonts.ready` でフォントの準備を待つ。2026-11-21 に `networkidle` から置き換えた）

## 7. ページの作り（CSS）

- A4。通常ページの下にページ番号（`@page` の `@bottom-center`）。
- 表紙と扉は、名前つきページ `full`（余白なし、ページ番号なし）。
- `page-break-inside: avoid` で、表、図、引用、コラムが、ページの途中で割れないようにする。

## 8. 確認の仕組み

- PDFをPyMuPDFで画像にして、全ページの一覧画像で確認する（文字の切れ、図の欠け、半分空きのページ）。
- 図や扉の変更後は、必ず画像で見る。

## 9. 配布と集客（外部サービス）

- Payhip: 商品の登録、ファイル配信、決済（PayPal、Stripe）。ブラウザ操作で登録する。保存ボタンを押したあとは、ページを開き直して反映を確認する。
- Pinterest: ボード「Japan apartment guide」に、ピンを1日1〜2枚ずつ公開する。
- GitHub: このリポジトリ（非公開、Actions無効）。
