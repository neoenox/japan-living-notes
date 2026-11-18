# Japan Living Notes

日本に住む外国人向けの英語PDFガイドを作って、Payhipで販売するための作業リポジトリ。

- 第1弾: "Renting an Apartment in Japan"（37ページ、$9、Excel計算シート付き）
- 作業手順: [docs/WORKFLOW.md](docs/WORKFLOW.md)
- 仕組み（PDFと画像ができるまで）: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- 販売ページの文面: [sales-page-en.md](sales-page-en.md)
- 集客用の文面: [marketing/posting-kit.md](marketing/posting-kit.md)
- 第2弾の構成案: [moving-in-guide-outline.md](moving-in-guide-outline.md)

## 再生成

```bash
pip install markdown playwright openpyxl pymupdf pillow
python tools/make_pdf.py rental   # PDF（movein も可）
python tools/make_calc.py   # Excel
python tools/make_cover.py  # Payhip用の表紙
python tools/make_pins.py   # Pinterest用ピン画像
```

注意: 数字・制度の記述は一般的な目安。出典を確認してから更新すること。GitHub Actionsは使用しない（無効）。
