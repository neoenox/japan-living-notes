# 第3弾の構成案（下書き）

目的: 12/18 の判断（[schedule.md](schedule.md)）までに、候補4つを同じ形式で比較できるようにする。
このファイルは**構成案のみ**。本文・制度の数字・価格は未確定。**公式資料で確認するまで数値を書かない**。11/25 までは公開ガイドの本文凍結中なので、既存PDF/本文は触らない。

## 共通の進め方

1. 読者の質問を1文で決める。
2. 公式的一次情報（省庁・自治体・事業者）で、書く予定の数字と期限を確認する。確認できないものは「目安」と書くか、入れない。
3. 既存2冊との重複を消す（下の「重複」列を参照）。
4. 本文 Markdown → `tools/guides.py` に設定関数を追加 → `tools/make_pdf.py <key>` で生成 → `tools/check_pdf.py` → 本人承認 → `docs/releases.md` に記録。
5. 図は既存の `tools/iso.py` / `tools/figs2.py` で足りるか先に確認する。新規図が必要なら別途作業として見積もる。

## 候補1: 医療・保険

- 読者の質問: 「海外から来て、病気になったときに何をすればいい？」
- 章案（EN）: Quick start / National Health Insurance / Finding a clinic / Medicine and pharmacies / Emergencies / When you leave Japan
- 必要な確認: 加入対象と手続きの期限、窓口、保険証・マイナンバーカードの扱い、緊急時の通報番号。いずれも自治体・厚生労働省・公式案内で確認する。
- 重複: 第2弾の「National Health Insurance and pension」に概要あり。詳細を書く場合は、第2弾では「別冊を見る」に留めるか、第3弾側に集約する。
-  Loader: `iso.scene(10)`（ライフライン）は不適。診察室・薬局の図は新規が必要。

## 候補2: 銀行と携帯

- 読者の質問: 「口座とSIMを、日本語が不自由なまま作れる？」
- 章案（EN）: Quick start / Bank account documents / Cash, cards and transfers / Mobile contracts / SIM-only options / Changing address and closing accounts
- 必要な確認: 銀行ごとの必要書類、在留カード・住所登録の要件、携帯契約の本人確認、解約と乗り換えの手順。事業者ごとに異なるため、断定せず「確認が必要」と書く。
- 重複: 第2弾第4章に「Updating your bank」「Mobile phones」の概要あり。詳細編として独立させる。
- Loader: 既存の `iso.scene(3)`（本人確認書類）と `figs2.doccards()` が使える。

## 候補3: 税金・年金

- 読者の質問: 「日本で働いたら、税金と年金はどうなる？」
- 章案（EN）: Quick start / Resident tax / Income tax / Pension basics / Filing and deadlines / Leaving Japan
- 必要な確認: 課税関係・納期・免税・抜け道は、国税庁・自治体・日本年金機構の最新資料で確認する。制度改正が入りやすいため、 edition と確認日を明記する。
- 重複: 既存2冊には未記載。第2弾の「Health insurance and pension」の年金部分をここに集約できる。
- Loader: `iso.scene(8)`（カレンダー）と `figs2.columns()` が流用可。

## 候補4: 賃貸＋入居のセット販売

- 読者の質問: 「借りるときと入ったあと、両方まとめて買えない？」
- 構成: 既存2冊をまとめるだけなので本文は新規執筆不要。商品ページ、価格、セット割、ファイル構成、返金方針を決める作業。
- 必要な確認: Payhipで複数ファイルを1商品に登録できるか、既存購入者への適用範囲、価格と説明文の整合（既存ページの価格計画は [sales-page-en.md](../sales-page-en.md) に記載）。
- 重複: なし（既存PDFの再パッケージ）。再ビルドや本文変更は不要。
- 判断材料: [day7-decisions.md](day7-decisions.md) のYouTube再検討条件3（セット商品または相談メニュー）に紐づく。価格・割引率は未決定。

## 比較の観点（12/18 に記入）

| 候補 | 一次情報の確認 | 新規図 | 本文の新規量 | 既存冊との重複処理 | 公開までの承認 |
|---|---|---|---|---|---|
| 医療・保険 | 未実施 | 要 | 大 | 第2弾と要調整 | 未取得 |
| 銀行と携帯 | 未実施 | 不要 | 大 | 第2弾と要調整 | 未取得 |
| 税金・年金 | 未実施 | 不要 | 大 | 第2弾と要調整 | 未取得 |
| セット販売 | 未実施 | 不要 | なし | なし | 未取得 |

「未取得」は確認していない項目。推測で埋めない。
