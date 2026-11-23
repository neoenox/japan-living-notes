# ローンチのスケジュール（2026-11-19〜12-18）

ピン6件の配信と、振り返りの日を1枚にまとめる。日付の区切りは日本時間。

- 基準値と数字の記録先: [marketing/launch-baseline-2026-11-18.md](../marketing/launch-baseline-2026-11-18.md)
- ピンの文面と判断基準: [marketing/pinterest-schedule.md](../marketing/pinterest-schedule.md)
- 未決事項: [TODO.md](TODO.md)

## 前提

- ピン6件は 11/19〜11/24 の 10:00 に1枚ずつ公開される（予約済み）。
- 本文（PDF）は 11/19〜11/25 の間、凍結する。例外は誤リンク、法令・期限の誤り、金額の矛盾、文字化けのみ。
- 数字は、管理画面で実際に見るまで「未取得」と書く。0と書かない。

## 毎朝の確認（11/19〜11/24、5分）

1. Pinterestの「予約投稿ピン」で、当日のピンが一覧から消えて公開に変わったか。
2. ピンの詳細URLをログインなしで開いて、宛先が `payhip.com/b/4ak8D` か。

| 日付 | ピン | 状態 |
|---|---|---|
| 11/19(木) | costs | 公開確認済み（10:08、宛先は第1弾） |
| 11/20(金) | foreigners | 公開確認済み（10:10 JST、ログインなし／omp のヘッドレス Chromium で詳細URLを直接取得）。詳細 `https://www.pinterest.com/pin/687995280623936667/` は HTTP 200、タイトル "How foreigners can rent an apartment in Japan"、宛先 `payhip.com/b/4ak8D?utm_source=Pinterest&utm_medium=organic`（第1弾） |
| 11/21(土) | emails | これから。下準備: ピンID `687995280623936675`（2026-11-20 10:21 JST、ログインなし／プロフィールJSONの `image_signature` とローカルの `pin_emails.png` を照合）。2026-11-20 10:58 JST にログインなしで詳細URLを取得、HTTP 200、clickthrough は `payhip.com/b/4ak8D?utm_source=Pinterest&utm_medium=organic`（第1弾）。タイトルは公開前の仮表示「Pin on Japan apartment guide」なので、公開後に `https://www.pinterest.com/pin/687995280623936675/` を開いて公開状態とタイトルを確認する |
| 11/22(日) | listing | 公開確認済み（2026-11-22 13:21 JST、ログインなし／omp が詳細URLを HTTPS で直接取得、クッキーなし）。ピンID `687995280624005769` は同 13:19 JST にログインなしのプロフィールJSONの `image_signature` とローカルの `pin_listing.png` を照合して特定。詳細 `https://www.pinterest.com/pin/687995280624005769/` は HTTP 200、ピンデータのタイトル "How to read a Japanese apartment listing"、説明文も予約時の文面と一致、clickthrough は `payhip.com/b/4ak8D?utm_source=Pinterest&utm_medium=organic`（第1弾）。公開ボードの画像も同じ署名 `e60f644100585b1233d01b2862a399b0`。ページの `<title>` は仮表示のまま |
| 11/23(月) | movein | **公開確認済み（2026-11-23 13:33 JST、ログイン済み Chrome の「すべてのピン」→ ピン詳細 ＋ ログインなしの詳細URL直取得）**。ピンID `687995280624022670`、詳細 `https://www.pinterest.com/pin/687995280624022670/` は HTTP 200、タイトル "Moving into your Japan apartment: the 14-day checklist"、説明文も予約文面と一致、clickthrough `https://payhip.com/b/4ak8D?utm_source=Pinterest&utm_medium=organic`（第1弾）。公開ピンの画像署名は `164fb820f217fb96aab8bca27fe4a031` で、ローカルの `pin_movein.png`（`0f12fa906c393d0931e9f6320a7d78ac`）と不一致。Pinterest側の画像再処理で署名が変わったため、`tools/check_pin.py` の署名照合では unpublished と誤判定した（タイトル照合に変更済み）。10:05 の予約チェックと 13:18 の再実行も同じ誤判定だった |
| 11/24(火) | moveout | 未公開。2026-11-22 13:23 JST にログインなしで確認: 公開ボードとプロフィールJSONに `pin_moveout.png` の署名 `24d40cb6a1180e1678c2e8342fa45eab` がなく、ピンIDも未取得。Pinterest検索にも出てこない。11/24 公開後に、プロフィールJSONの署名照合でIDを特定し、詳細URLの HTTP 200・タイトル・clickthrough（`payhip.com/b/4ak8D` か）を確認する。**2026-11-23 13:18 JST に手動で事前確認（ログインなし、`tools/check_pin.py moveout`）、まだ unpublished、ピンID・clickthrough とも未取得** |

## 日別カレンダー

| 日付 | Day | 自動で起きること | こちらでやること |
|---|---|---|---|
| 11/20(金) | 2 | foreigners が10:00に公開 | 毎朝の確認 |
| 11/21(土) | 3 | emails が公開 | 毎朝の確認 |
| 11/22(日) | 4 | listing が公開 | 毎朝の確認＋宛先の確認 |
| 11/23(月) | 5 | movein が公開 | 毎朝の確認＋宛先の確認 |
| 11/24(火) | 6 | moveout が公開 | 毎朝の確認＋宛先の確認。**11/25以降のピンを決める** |
| 11/25(水) | 7 | — | 数字の記録、凍結の解除、次の判断（下記） |
| 12/2(水) | 14 | — | 数字の記録と、続けるか変えるかの判断 |
| 12/18(金) | 30 | — | 総括、価格、次の商品 |

## Day 7（11/25・水）

数字を取って、基準表に追記する。

- Pinterest: インプレッション、保存、アウトバウンドクリック（合計と、ピン別）
- Payhip: 購入件数、商品ビュー（第1弾・第2弾）

終わったら、次を決める。判断材料は [day7-decisions.md](day7-decisions.md) にまとめた。決めたことは [TODO.md](TODO.md) に結果を書いて消し込む。

1. 11/25以降のピンをどうするか（6枚で終わるため、ここで止めるか、新しく作るか）
2. PayhipストアのAbout欄を作るか（文面は [marketing/payhip-store-about.md](../marketing/payhip-store-about.md)）
3. 配布するExcelをどちらの版に揃えるか（[releases.md](releases.md) にSHA256の不一致を記録済み）
4. PDF付録に第2弾への導線を入れるか（入れるなら再ビルドと差し替えの承認が要る）
5. p27の薄いページを直すか（凍結が解けるので、次版の作業として着手できる）

## Day 14（12/2・水）

数字を取って、[marketing/pinterest-schedule.md](../marketing/pinterest-schedule.md) の判断表に当てる。

- クリック合計が25未満: ピンの見出しと画像を変えて作り直す
- 25以上で購入0: 商品ページを直す
- 25以上で購入1以上: 反応のあったテーマでピンを増やす

あわせて、ブログ記事（[marketing/blog-initial-costs.md](../marketing/blog-initial-costs.md)）の公開先を決めて出す。

## Day 30（12/18・金）

- 数字をまとめ、次版に反映する内容を決める。
- 価格を見直す。販売ページの計画は、購入5件で $12、反応を見て $15。実際の件数と、商品ページの表示回数で判断する。
- 次の商品（医療・保険、銀行と携帯、税金・年金、セット販売）から1つ選ぶ。

## 決める期限

| 期限 | 決めること |
|---|---|
| 11/24 | 11/25以降のピン |
| 11/25 | About欄、Excelの正版、付録の導線、p27の修正着手 |
| 12/2 | ブログの公開先、Pinterestを続けるか |
| 12/18 | 価格、次の商品 |
