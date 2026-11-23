# 公開状態の基準記録（2026-11-18）

このファイルは、Day 7・Day 14の振り返りで比較するための基準を記録する。公開情報と、管理画面が必要な未確認項目を分けて扱う。

## 確認済み: Payhip

2026-11-18 16:30（日本時間）頃に一般公開ページを確認した。

- ストア: https://payhip.com/JapanLivingNotes
- 第1弾: https://payhip.com/b/4ak8D
- 第2弾: https://payhip.com/b/6DW8M
- ストアの商品一覧に第1弾（$9.00）と第2弾（$7.00）が表示されている。
- 第1弾の公開説明は「PDF, 37 pages」「Initial Cost Calculator (Excel)」と一致している。
  - 2026-11-18 17:xx の差し替えで **35ページ**に変わった（章末の薄いページを整理したため）。公開説明も35ページに更新した。
- 第1弾の返金は、購入後7日以内にPayhipストアのContactから連絡する方式と表示されている。
- 第2弾の公開説明は「illustrated PDF, 24 pages」「5 copy-and-paste emails」と一致している。
- 商品ページ本文には`[Decide: ...]`と`[your email]`が表示されていない。

## 確認済み: Pinterest

- プロフィール: https://www.pinterest.com/JapanLivingNotes/
- プロフィールのWebサイト: http://payhip.com/JapanLivingNotes
- 公開ボード: https://www.pinterest.com/japanlivingnotes/japan-apartment-guide/
- プロフィールAbout: `Practical English guides for foreign residents in Japan: renting, moving in, and daily setup. Checklists and email templates included.`
- 一般公開のボードデータに表示される3画像は、次のローカル画像と一致した。
  - `marketing/pins/pin_costs.png`
  - `marketing/pins/pin_foreigners.png`
  - `marketing/pins/pin_emails.png`

一般公開ページからは、予約6件の各日時、各宛先、公開後のAlt textまでは確認できない。

## 管理画面で確認する未完了項目

- Pinterestの「予約投稿ピン」に6件が残っているか（→ 2026-11-18 19:2x に6件を確認）。
- 6件の宛先がすべて第1弾の商品ページか（→ 3件（costs / foreigners / emails）は `payhip.com/b/4ak8D` を確認。残り3件（listing / movein / moveout）は自動化では開けず未確認）。
- 第1弾の公開PDFをダウンロードし、`draft`、TODO、プレースホルダー、欠けたページがないか（→ 2026-11-18 差し替え後にSHA256照合済み。中身は `check_pdf.py` で検査済みのファイルと同じ）。
- PayhipストアのAbout Meへ[payhip-store-about.md](payhip-store-about.md)の文面を設定できるか（→ 公開ストアページにAbout欄自体が表示されていない。設定はストアビルダーのセクション追加になるため未実施）。
- PayhipのCustomersで、振り返り開始時の購入件数を確認する（→ 0件）。

## Day 7・Day 14に記録する数字

| 指標 | 基準値（2026-11-18） | Day 7 | Day 14 |
|---|---:|---:|---:|
| Pinterestインプレッション | 管理画面未取得 | 未取得 | 未取得 |
| Pinterest保存 | 管理画面未取得 | 未取得 | 未取得 |
| Pinterestアウトボウンドクリック | 管理画面未取得 | 未取得 | 未取得 |
| Payhip購入 | 0件（2026-11-18 18:5x にダッシュボードで確認） | 未取得 | 未取得 |
| Payhip商品ビュー（第1弾 / 第2弾） | 3 / 1（同上） | 未取得 | 未取得 |

0と記載せず、管理画面で確認できるまで「未取得」のままにする。11/25 は Pinterest Analytics と Payhip ダッシュボード／Customers から取得し、取得時刻と表示期間を添えて Day 7 列に記入する。

## Day 1（2026-11-19）

- 本日から本文を凍結する（11/19〜11/25 = Day 7）。例外は誤リンク、法令・期限の誤り、金額矛盾、文字化けのみ。
- 09:2x 時点の予約投稿ピン: プロフィール → 作成コンテンツ → 予約投稿ピン に6件。「他のユーザーには公開されません」の表示のまま。Day 1（costs）は 10:00 公開予定。
- ピンの宛先確認（`bsk` でログイン済みプロフィールを操作。閲覧のみ）:
  - ピンの詳細URL `https://www.pinterest.com/pin/<id>/` を直接開くと、予約中のピンでも「サイトにアクセス」の href を読める。
  - costs（pin `687995280623935762`）: `https://payhip.com/b/4ak8D?utm_source=Pinterest&utm_medium=organic`（Pinterestがutmを付与。宛先は第1弾で正しい）。
  - listing / movein / moveout は未確認のまま。「作成コンテンツ」画面には6件表示されるが、DOMとアクセシビリティツリーに載るピンリンクは3件のみで、3件のピンIDを取得できなかった。**公開後（11/22〜11/24）に公開ピンの詳細ページで確認する**（公開済みなら必要に応じて編集できる）。

### 10:08 追記: Day 1のピンは公開済み

- `https://www.pinterest.com/pin/687995280623935762/` をログインなしで取得して、HTTP 200、ページ内に「Japan apartment initial costs explained」とピンIDを確認した。所有者のログインなしで中身が読めるため、予約ではなく公開済みと判断した。
- 同じ取得で `payhip.com/b/4ak8D` へのリンクがページ内にあることも確認した。宛先は第1弾。
- ボード `https://www.pinterest.com/japanlivingnotes/japan-apartment-guide/` も、ログインなしの取得でピンIDを含んでいた（タイトル文字列はJS描画のため取得できない）。
- 予約6件のうちDay 1だけが公開。残り5件は11/20〜11/24の予定で、listing / movein / moveout の宛先は公開後に確認する。

## 中間確認（2026-11-20 12:06 JST、ログインあり）

方法: 利用者の Chrome にログイン済みの Payhip 管理画面を bsk で借用して読み取った（Dashboard と Customers）。Pinterest は 2026-11-20 13:54 JST にログイン済みの Analytics オーバービューを借用して読み取った。

- Payhip ダッシュボード「Your Products」: `Renting an Apartment in Japan` 3 views / 0 orders / $0.00 sales、`Moving In: Utilities & Setup in Japan` 1 views / 0 orders / $0.00 sales
- Payhip「Customers」: 0 Orders / "No orders have been made yet"（ナビゲーションのバッジ「1」は注文数ではない）
- Pinterest Analytics オーバービュー（2026-11-20 13:54 JST、ログインあり、表示期間 2026/10/21〜2026/11/20 = 過去30日、リアルタイム推定値）: インプレッション 15、エンゲージメント 0、アウトバウンドクリック 0、保存 0、合計オーディエンス／エンゲージしたオーディエンスは「-」。ピン別インプレッション: `costs` 4 と 4（重複2件）、`foreigners` 4、`emails` 3。トップボード「Japan apartment guide」15（ピン5件）。デイリーデータは UTC 記録。

この中間値をもって Day 7 列を埋めず、11/25 の取得時に改めて記録する。

2026-11-23 17:12 JST 追記（ログインなし、公開商品ページを bsk で閲覧）: 第1弾は "THE GUIDE (PDF, 35 pages)"、第2弾は "THE GUIDE (illustrated PDF, 24 pages)" と "5 COPY-AND-PASTE EMAILS" を確認。記録と一致。Payhip は未ログインのため配送ファイルのダウンロード・照合は未実施。
