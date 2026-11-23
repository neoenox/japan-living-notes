# 次にやること（スコープ外に切り出したもの）

2026-11-18 の作業で「今日はやらない」と決めたもの。実行条件つきで残す。終わったら消すのではなく、日付と結果を書いて消し込む。

## 次版（Day 7 = 2026-11-25 以降）

- [ ] p27（第8章 8.4）が薄いページになっている。章末の短い節を前節に統合するか、章末に「次の章」への導入を置いて埋める。**ピン進行中（11/19〜11/24）は本文を触らない**（例外は誤リンク・法令/期限の誤り・金額矛盾・文字化けのみ）
  - 2026-11-22 18:11 JST 下準備（ログインなし、一時ディレクトリでドライラン。本物の本文・配布PDFは未変更）: 8.4 の2項目を 8.3 の末尾に次の1行で統合する案を試した: `**If there is a problem:** ask the management company for a written answer. Local consumer centers and multilingual support are listed in Appendix H.` 再生成は成功し、ページ数は **34**（現行35）、薄いページは消えて 8.3 の本文は26ページに1,543字で載る。採用するなら 11/25 以降に本文へ適用 → `check_pdf.py <PDF> 34` → `sales-page-en.md` の「35ページ」を34に更新 → 本人承認 → 差し替え → `releases.md` に追記。
- [x] `check_pdf.py` の空ページ判定（本文250字未満かつ図版10未満）は、章扉ページを除外する条件を入れると誤検知が減る（現状は drawings 数で偶然回避している）
  - 2026-11-19 対応: 1ページ目（表紙）と章扉（文字間の空いた `C H A P T E R n` で始まるページ）を判定から除外した。除外件数は1行で報告する。`Renting-an-Apartment-in-Japan.pdf` で章扉10ページが除外され、p27 だけが NG として残ることを確認（p27 は上記の次版対応待ち）
  - 2026-11-19 19:58 JST 対応・確認（ログインなし、ローカル）: 全ソースレビューの Important 4件を修正。`check_pdf.py` は図版ページにも最低40字、表紙/章扉の除外にも最低100字＋図版1個を要求し、読込不能/0ページは `NG`＋`RESULT` を出して終了、古い一覧画像を削除。`mk2.py` の emails サンプルを p33→p31 に直し、whois/emails ともにページ内マーカー不一致で停止。再生成したHTML/PNG/ExcelはHEADと同一、PDFテキストは賃貸が同一（第2弾は既知の p8/p9/p20/p21 drift のみ）、mk2再生成画像はコミット済み画像とバイト一致。2PDFのcheck_pdfは賃貸p27のみNG・第2弾は通過。合成PDF（文字0＋図版12、CHAPTER-only、正当な章扉、0ページ、壊れたPDF）で新ガードの判定と古いシート削除を確認。配布PDF・本文は未変更
  - 2026-11-20 09:43 JST 対応・確認（ログインなし、ローカル）: 残レビュー提案12件のうち10件を修正。`iso.scene` は9を明示分岐に昇格し未知番号は `ValueError`、`art.py` は `iso.adj` に統一、`make_cover` は viewBox を引数化、`check_pdf` はページ数未指定の明記・非 http(s) の `SKIP`・URL上限20件・一覧画像のストリーム化、`figs2.columns([])` と `make_pins` の枚数をガード、未使用定数と例外時のブラウザ未クローズを解消。#4（networkidle 置換）と #8（`main()`／`__main__` ガード）は当時、Chrome＋Google Fonts の再生成検証が必要なため11/25以降に繰り延べたが、下記のとおり 11/21 に実施済み。編集前後の出力バイト比較（SVG文字列・check_pdf 標準出力と一覧画像）は全項目で一致、新ガードは使い捨てテストで確認。本文・配布PDF・画像は未変更
  - 2026-11-21 00:06 JST 対応・確認（ログインなし、ローカル、コミット `4927906`）: 繰り延べていた #4 と #8 を実施。`wait_until='networkidle'` をフォントの明示待ちに置き換え、`mk2.py` / `make_calc.py` / `make_cover.py` / `make_cover_movein.py` / `make_pdf.py` / `make_pins.py` の副作用を `main()` 配下へ移動。全スクリプトが import 時に書き込まないこと、compile 成功、再生成結果（ピン・表紙PNGはバイト一致、賃貸PDFテキストは同一、第2弾は既知の p8/p9/p20/p21 drift のみ、Excelの値と数式は同一）を確認。配布物はHEADに戻しており未変更
- [x] 第2弾の配布PDFと現在の本文は**不一致ではない**（2026-11-22 に検証。下記のとおり差し替え不要）。もともとは「p8, p9, p20, p21 に段落の差がある」と記録されていたが、内容差ではなく改ページ位置の差だった
  - 2026-11-19 確認: ログインなし。`make_pdf.py movein` でローカル再生成し、Git管理の配布PDFとページごとのテキストを比較して差分4ページを特定。再生成したPDFは元に戻しており、配布物は未変更
  - 2026-11-22 18:05 JST 再確認（ログインなし、ローカルのみ）: 前提を再検証した。配布PDF p8 にも `moving-in-guide-en.md` と生成HTML `tools/guide-movein.html` にも「Two types: city gas (都市ガス) and propane gas (プロパン, LP gas)...」の段落がある。11/19 の「本文にはない」という記述はそのままだが、11/25 に再生成してページ単位で比較し、差がレイアウト由来なら本文を戻さず差し替えもしないこと。段落の欠落を前提に修正しない。
  - 2026-11-22 18:11 JST 結論（ログインなし、一時ディレクトリで再生成してページ単位に比較。配布物・本文は未変更）: 再生成PDFも24ページで、差分は p8→p9 への「2.3 Gas」見出しと「Two types...」以下の移動、および用語集の「ブレーカー」行が p21→p20 へ移動しただけ。欠落・追加・文言差はなし。したがって本文に段落を戻す必要も、PDFを差し替える必要もない。11/19 の「本文にない」という前提は誤りだった。

## 集客・販売

- [ ] PayhipストアのAbout Me：公開ストアページにはAbout欄が表示されていない。ストアビルダーでセクションを追加するか、追加しないかを決める（文面は `marketing/payhip-store-about.md` に用意済み）
- [ ] 11/25以降のピン方針（期限11/24）: 判断材料を `docs/post-day7-pins.md` にまとめた。数値は未取得のまま
  - 2026-11-23 16:40 JST 合意（grilling）: 11/25 はまず Pinterest Analytics と Payhip ダッシュボード／Customers から数字を取得して `launch-baseline-2026-11-18.md` の Day 7 列に記入する。数字は omp がログイン済みブラウザから読み取り、開かない時は「未取得」と書いて推測・0で埋めない。取得後にファネル表で止まった場所を選び、ピン継続を決める。新しいチェックリストは作らず既存ファイルに集約する（`docs/day7-decisions.md` / `docs/post-day7-pins.md` に反映済み）
- [ ] Pinterestの予約6件のうち、movein / moveout の宛先が `payhip.com/b/4ak8D` か確認する（costs / foreigners / emails / listing / movein は確認済み。残り1件は 11/24 の公開後に確認）
  - 2026-11-23 13:33 JST 確認（ログイン済み Chrome の「すべてのピン」→ ピン詳細、およびログインなしの詳細URL直取得）: `movein` は公開済み。ピンID `687995280624022670`、詳細 `https://www.pinterest.com/pin/687995280624022670/` は HTTP 200、タイトル・説明文一致、clickthrough `https://payhip.com/b/4ak8D?utm_source=Pinterest&utm_medium=organic`（第1弾）。公開画像署名 `164fb820f217fb96aab8bca27fe4a031` がローカル `0f12fa906c393d0931e9f6320a7d78ac` と不一致だったため、`tools/check_pin.py` の署名照合は unpublished と誤判定した。タイトル照合に変更して誤判定を解消（`docs/schedule.md` に記録済み）
  - 2026-11-23 13:18 JST 確認（ログインなし、`python tools/check_pin.py listing movein moveout`）: `listing` は published・pin_id `687995280624005769`・clickthrough 第1弾。`movein` と `moveout` は unpublished と判定されたが、上記のとおり `movein` は署名照合の誤判定だった。10:05 の予約タスク実行（Windows タスク スケジューラ、ログに `RESULT ... movein status=unpublished`）も同じ誤判定
  - 2026-11-22 13:21 JST 確認（ログインなし、詳細URLを直接取得）: listing（ピンID `687995280624005769`）は HTTP 200、タイトル "How to read a Japanese apartment listing"、clickthrough は `payhip.com/b/4ak8D?utm_source=Pinterest&utm_medium=organic`（第1弾）。ピンIDはプロフィールJSONの `image_signature` と `pin_listing.png` の照合で特定。`docs/schedule.md` に記録済み
  - 2026-11-22 13:23 JST 確認（ログインなし）: movein / moveout はまだ未公開。公開ボード・プロフィールJSON・Pinterest検索のいずれにも画像署名がなく、ピンIDは未取得。宛先は「未取得」のまま。11/23・11/24 の公開後に同じ手順で確認する（`docs/schedule.md` に記録済み）
- [ ] `initial-cost-calculator.xlsx` は、Payhipで配布中のファイルとリポジトリの版でSHA256が違う（サイズは同じ）。次にExcelを触るときに、どちらを正とするか決める

- [ ] PDF内部（付録）に第2弾への導線を入れるか決める（入れるなら再ビルド＋再承認）
- [ ] ブログ記事 `marketing/blog-initial-costs.md` の公開（公開先を決める。note / 自前 / Medium。公開前チェックは `docs/blog-publishing-prep.md`）
- [ ] 拡散対策：Payhipの透かし、購入者識別、価格戦略の見直し（リポジトリの暗号化では防げない領域）
- [ ] Day 7（11/25）と Day 30 に、Pinterestの表示・保存・アウトバウンドクリックとPayhip購入件数を記録する（`launch-baseline-2026-11-18.md` の表に追記）

## セキュリティ・運用

- [ ] GitHubアカウントの2FAを確認する
- [ ] トークンを fine-grained PAT（当該リポジトリ限定・有効期限つき）に置き換える
- [ ] リポジトリの collaborator が0件であることを確認する
- [ ] 年1回、配布版PDFを age で暗号化して別媒体（外付け/クラウド）に退避する（リポジトリは平文のまま）

## 第3弾の候補

- [ ] 医療・保険 / 銀行と携帯 / 税金・年金 / 賃貸＋入居のセット販売（比較用の構成案は `docs/next-product-outlines.md`。数値・制度は未確認）

## 予約済みの監視（Muse）

- 2026-11-20 10:00 JST 以降に、Day 2のピン `foreigners` の宛先をログインなしで確認するタスクを Muse のサイドチャットに登録した（2026-11-19 登録）。
  - 見るもの: 公開ボード `https://www.pinterest.com/japanlivingnotes/japan-apartment-guide/` のピン "How foreigners can rent an apartment in Japan"（ローカルの `marketing/pins/pin_foreigners.png`）。詳細URL `https://www.pinterest.com/pin/<id>/` をログインなしで取得し、HTTP 200・タイトル・宛先 `payhip.com/b/4ak8D`（utm付き可）を確認する。
  - 条件（どれか成立した時だけ報告）: (1) ピンが公開され、ログインなしで詳細が読めた; (2) 詳細ページの「サイトにアクセス」href が `payhip.com/b/4ak8D` でない、または見つからない; (3) 11/20 12:00 JST までに公開されない。
  - 報告の形: 日時・確認方法（ログインなし／どのURL）・ピンID・宛先の結果を3行以内。プラン・提案・下書きは書かない。未達・数字が取れないときは通知せず静かに終了する。
  - 結果が戻ったら `docs/schedule.md:23` の状態列に日時と方法を追記。`foreigners` の宛先は2026-11-18にログイン済み画面で確認済み（`marketing/launch-baseline-2026-11-18.md:35`）なので、今回は独立再確認。
  - 結果の回収も予約済み: Museの日時指定タスク「Japan Living Notes / Muse結果の回収」を 2026-11-20 12:15 JST に登録（タスク数11件→12件を確認）。10:05タスクの結果を同じサイドチャットから読み、ピンIDと宛先、または「未取得」を3行以内で報告する。結果が戻ったらompが `docs/schedule.md:23` の状態列に日時と方法を追記する。

## 予約済みの監視（omp / 2026-11-22 登録）

- 2026-11-23 10:05 JST に、Day 5 のピン `movein` の公開・宛先をログインなしで確認するジョブを、本セッションのバックグラウンドジョブ `bg_1` として登録した（2026-11-22 登録）。スクリプトは一時ディレクトリの `pin_check_1123.py`（使い捨て）。
  - 2026-11-22 18:41 JST 予約: 11/23 10:05 JST の `movein` 確認を本セッションのバックグラウンドジョブ `bg_1` として登録した。一時スクリプトではなく常設の `tools/check_pin.py movein` を使い、10:05〜10:30 の間60秒ごとに再試行する。出力は `SCHEDULED` / `RESULT` 行で通知され、結果が来たら日時・方法・ピンID・宛先を `schedule.md` の11/23行とこの項目に追記する。セッション終了でジョブは停止するため、結果が来なければ同じコマンドを手動で実行する。前回登録分はセッション終了時に停止済み。
  - 2026-11-22 19:41 JST 再登録: 前のセッション終了で `bg_1` が停止していたため、本セッションで `bg_2` として再登録した。起動確認は `SCHEDULED 2026-11-22 19:41:43 JST waiting 51796s until 2026-11-23 10:05 JST`。直前にログインなしで `tools/check_pin.py movein` を実行し、`status=unpublished`・ピンID/宛先とも未取得を確認済み（19:41:37 JST）。10:05〜10:30 は同じコマンドを60秒ごとに自動再試行する。bash の `python` は WindowsApps のリダイレクトで終了コード9009になるため、インタプリタは絶対パス `C:\Users\neoen\AppData\Local\Programs\Python\Python312\python.exe` を使う。
  - 2026-11-23 00:33 JST 再設定（ログインなし、ローカル）: セッション再起動で `bg_2` も停止していたため、Windows タスク スケジューラに1回限りのタスク `JapanLivingNotes-PinCheck-Movein-20261123` を作成した（次回実行 2026/11/23 10:05 JST、状態「準備完了」、確認済み）。実行内容は一時フォルダの `pin_check_movein_20261123.cmd` で、`tools/check_pin.py movein` の出力を同フォルダの `pin_check_movein_20261123.log` に追記する。セッション終了でも動く点が bg ジョブと違う。00:33:19 JST に手動で再確認したが `movein` はまだ未公開で、ピンID・宛先とも未取得。10:06 JST にログを読み取るジョブ `bg_3` を本セッションに登録済み（こちらはセッション依存）。結果を `schedule.md` とこの項目に記録したら、タスクと一時ファイルを削除する。
  - 2026-11-22 18:08 JST 対応・確認（ログインなし、ローカルの一覧と公開ページ）: 使い捨てスクリプトの代わりに常設の `tools/check_pin.py` を作成した。ローカルの `pin_*.png` のMD5を画像署名としてプロフィールJSONの公開ピンと照合し、詳細ページの HTTP 200・タイトル・説明文・clickthrough（`payhip.com/b/4ak8D` か）を1行で出力する。11/23 と 11/24 は `python tools/check_pin.py movein moveout` で確認し、結果を `schedule.md` とこの項目に追記する。動作確認: `listing` は published・pin_id `687995280624005769`・clickthrough 第1弾で exit 0、未公開の `movein` は「未取得」で exit 1。バックグラウンドジョブはセッション終了で停止するため当てにしない。
  - 見るもの: `marketing/pins/pin_movein.png` の画像署名 `0f12fa906c393d0931e9f6320a7d78ac` をログインなしのプロフィールJSONで照合してピンIDを特定。詳細 `https://www.pinterest.com/pin/<id>/` を取得し、HTTP 200、タイトル "Moving into your Japan apartment: the 14-day checklist"、説明文、`data-test-id="clickthrough-link"` の href（`payhip.com/b/4ak8D` か）を確認する。
  - 実行条件: 10:05 JST に開始し、10:30 JST まで60秒ごとに再試行。公開されなければ ID・宛先とも「未取得」と報告する。
  - 報告: `SCHEDULED` / `RESULT` / `ERROR` で始まる行がジョブから通知される。結果が戻ったら日時・方法・ピンID・宛先を `docs/schedule.md` の 11/23 行に追記し、このファイルの宛先確認項目を更新する。
  - 制約: セッションが終了するとバックグラウンドジョブも停止する。結果が来ていなければ、同じ手順を手動で実行して記録する。
