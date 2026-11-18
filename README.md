# Japan Living Notes

日本に住む外国人向けの英語PDFガイドを作って、Payhipで販売するための作業リポジトリ。

- 第1弾: "Renting an Apartment in Japan"（35ページ、$9、Excel計算シート付き）
- 第2弾: "Moving In: Utilities & Setup in Japan"（24ページ、$7）
- 作業手順: [docs/WORKFLOW.md](docs/WORKFLOW.md)
- 仕組み（PDFと画像ができるまで）: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- 販売ページの文面: [sales-page-en.md](sales-page-en.md)
- 第2弾の販売ページ文面: [sales-page-movein-en.md](sales-page-movein-en.md)
- 集客用の文面: [marketing/posting-kit.md](marketing/posting-kit.md)
- Pinterest 6日間の投稿計画: [marketing/pinterest-schedule.md](marketing/pinterest-schedule.md)
- 公開状態の基準記録: [marketing/launch-baseline-2026-11-18.md](marketing/launch-baseline-2026-11-18.md)
- 配布物の記録（版・ページ数・SHA256）: [docs/releases.md](docs/releases.md)
- 次にやること: [docs/TODO.md](docs/TODO.md)
- 第2弾の構成案: [moving-in-guide-outline.md](moving-in-guide-outline.md)

## 再生成

```bash
# リポジトリのどこから実行してもよい（パスはファイルの位置から決まる）
pip install markdown playwright openpyxl pymupdf pillow
python tools/make_pdf.py rental   # PDF（movein も可）。どのフォルダからでも実行できる
python tools/check_pdf.py Renting-an-Apartment-in-Japan.pdf 35   # アップロード前の確認
python tools/check_pdf.py Moving-In-Utilities-and-Setup-in-Japan.pdf 24
python tools/make_calc.py   # Excel
python tools/make_cover.py  # Payhip用の表紙
python tools/make_cover_movein.py  # 第2弾の表紙
python tools/make_pins.py   # Pinterest用ピン画像
```

重要: PDFをPayhipに上げる前は、必ず `docs/WORKFLOW.md` の「6a」の確認フロー（自動チェック＋本人の確認）を通す。

注意: 数字・制度の記述は一般的な目安。出典を確認してから更新すること。GitHub Actionsは使用しない（無効）。
