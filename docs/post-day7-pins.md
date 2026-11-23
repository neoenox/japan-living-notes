# 11/25以降のピン方針（下準備）

判断期限: 2026-11-24（[schedule.md](schedule.md) / [day7-decisions.md](day7-decisions.md) の項目1）。
このファイルは**判断材料の下書き**。投稿・予約・削除は本人が行う。数値が未取得の間は「未取得」と書き、0と書かない。

## 現状（2026-11-23 13:18 JST、ログインなし・ローカルの記録）

- 11/19 `costs`: 公開・宛先確認済み。
- 11/20 `foreigners`: 公開・詳細URL・宛先確認済み（[schedule.md](schedule.md) の表）。
- 11/21 `emails`: 公開・詳細URL・宛先確認済み。
- 11/22 `listing`: 公開・詳細URL・宛先確認済み（2026-11-23 13:18 JST に `tools/check_pin.py listing` で再確認）。
- 11/23 `movein`: **公開確認済み**（2026-11-23 13:33 JST）。ピンID `687995280624022670`、詳細URLは HTTP 200、タイトル・説明文一致、clickthrough は第1弾（[schedule.md](schedule.md) の11/23行）。公開画像の署名が変わっていたため `tools/check_pin.py` は誤判定したが、既知ID照合に修正して解消。
- 11/24 `moveout`: 予約中。2026-11-23 13:18 JST の手動確認で unpublished、ピンID・宛先とも未取得。
- 重複ピンは解消済み（2026-11-23 14:31 JST）。古い方3件（costs `687995280623952946`、foreigners `687995280623971495`、emails `687995280623989155`）を削除し、新しい方5件だけ残した。削除後に `tools/check_pin.py` で5件すべて published・宛先第1弾を確認（[day7-decisions.md](day7-decisions.md) の項目9）。削除は復元不可。
- 11/25 に取得するPinterest/Payhipの数字は**未取得**。参考の中間値は [day7-decisions.md](day7-decisions.md) に別掲（正式値ではない）。

推奨デフォルトは A（6枚で止める）。どのテーマが効いたか未取得で、新規画像は方向性が分かってから作る方が無駄がない（[strategy-2026-11-22.md](strategy-2026-11-22.md) の項目1）。

11/25 の進め方（2026-11-23 に合意）:

1. まず Pinterest Analytics と Payhip ダッシュボード／Customers から数字を取得し、[launch-baseline-2026-11-18.md](../marketing/launch-baseline-2026-11-18.md) の Day 7 列に記入する。
2. 数字は私（omp）がログイン済みブラウザから読み取る。管理画面が開かない時は「未取得」と書き、推測や 0 で埋めない。
3. 取得した数字を [strategy-2026-11-22.md](strategy-2026-11-22.md) のファネル表に当て、止まった場所を1つ選んでから、6枚で止めるか新規ピンを作るかを決める。
4. 新しいチェックリストは作らず、記録は既存ファイルに集約する。

## 選択肢

| 案 | 内容 | 前提・リスク |
|---|---|---|
| A. 6枚で止める | 11/24以降は新規投稿しない。Day 14 / Day 30 の数字だけ記録する | 追加作業なし。6枚の反映が遅い場合はDay 30まで待つ |
| B. 第1弾の新規ピンを作る | [pinterest-schedule.md](../marketing/pinterest-schedule.md) の「同じ画像の再投稿はしない」に従い、新しい図と文面で作る | 画像作成（ローカル）＋本人が予約。クリックが多いテーマが分かるまでは方向性が仮 |
| C. 第2弾へ切り替える | 第2弾 `https://payhip.com/b/6DW8M` へ誘導するピンを作る | 第2弾のピン表記は「Illustrated PDF」に修正済み（`8676393`）。既存6枚は第1弾宛てなので混在しないよう注意 |

Day 14 の判断表の「クリック合計25」は**仮の目安**であり、実測値ではない。表示数が極端に少ない場合は、この基準より先にインプレッションを見る（[pinterest-schedule.md](../marketing/pinterest-schedule.md) の振り返り判断に同じ）。

## 新規ピンの候補（文面案のみ・未投稿）

第1弾の既存テーマと重複を避ける候補。画像は既存の `iso.scene()` に無い構図が必要なら、新規図の作成を別途承認する。

| 案 | Title (EN) | Description (EN) | 既存の図との関係 |
|---|---|---|---|
| B1 | What happens at the viewing (内見)? | Photos, appliances, water pressure, and questions to ask the agent before you apply. #japanrental | `iso.scene(5)`（入口と鍵）を流用可だが、新規文面に合わせた図を推奨 |
| B2 | The contract: clauses to read first | Explanation of important matters, fixed-term vs standard leases, and special terms. #japanapartment | 図 `iso.scene(6)`（契約書）を流用可 |
| C1 | Your first 30 days in a Japan apartment | Gas, electricity, water, address report, garbage rules, and who to call when something breaks. #movingtojapan | `iso.scene(10)` / `iso.scene(11)` を流用可。第2弾宛て |
| C2 | The 14-day address report checklist | What to bring, what gets updated, and mail forwarding. #expatjapan | 第2弾の `figs2.bring()` を流用可。第2弾宛て |

ALT text と宛先は、予約前に本人が確認する。既存6枚と同じ画像の再投稿はしない。

## 記録の形（Day 7 / Day 14 で記入）

| 日時 | 方法（ログインの有無・画面名） | ピン | インプレッション | 保存 | アウトバウンドクリック | 宛先 |
|---|---|---|---|---|---|---|
| 未取得 | 未取得 | 未取得 | 未取得 | 未取得 | 未取得 | 未取得 |

値が取れない項目は空欄にせず「未取得」と書く。記録先は [launch-baseline-2026-11-18.md](../marketing/launch-baseline-2026-11-18.md)。

## 本人が行う操作

- Day 7 / Day 14 の数値の読み取り（Pinterest Analytics、Payhip ダッシュボード）
- 11/25以降のピンの採用・画像・文面の最終決定
- Pinterest への投稿・予約・ピン削除（重複ピンの扱いは [day7-decisions.md](day7-decisions.md) の項目9）
