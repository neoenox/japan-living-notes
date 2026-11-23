# ブログ記事の公開準備（下書き）

対象: [blog-initial-costs.md](../marketing/blog-initial-costs.md)（記事A）、[posting-kit.md](../marketing/posting-kit.md) の記事B（「Can a Foreigner Rent...」は見出しのみ）。
公開先は 12/2 に決める（[schedule.md](schedule.md)）。**このファイルは下準備のみ。公開操作は行わない**。

## 公開先の比較（決定前）

| 先 | 利点 | 確認が必要な点 | 状態 |
|---|---|---|---|
| note | 日本語読者に届きやすい。記事は英語のままで投稿可能か要確認 | 英語記事の検索性、商品リンクの可否、外部リンクの扱い | 未確認 |
| Medium | 英語記事との相性がよい | 自己宣伝・アフィリエイト_link_のルール、canonical、収益化の有無 | 未確認 |
| 自前サイト |  LINK と計測を自由に設計できる | ドメイン、HTTPS、運用コスト、公開までの作業量 | 未確認 |

「未確認」は、管理画面や規約を実際に見ていない項目。0や可と書かない。

## 公開前チェック（記事A）

- [x] 仲介手数料の上限（貸主＋借主で家賃1か月分＋税、借主の原則0.5か月分＋税）を一次情報で再確認した（2026-11-22、下の表）
- [ ] 例の金額（¥410,500、約5.1倍）が PDF / Excel / 本文と一致する（第1弾の費用図と同じ数値を使っている）
- [ ] 「目安」であること、法的助言でないことを冒頭と末尾に明記する
- [ ] 商品リンクは `https://payhip.com/b/4ak8D` の1つだけ。レビュー・購入者数・実績は書かない
- [ ] 画像を使う場合は `marketing/samples/` の既存画像を流用し、ライセンスと表示を確認する
- [ ] 記事内の数字を「未取得」のまま公開しない（取れていない値は削除する）

## 公開前チェック（記事B）

- [x] 本文を書き下ろした（2026-11-22、[blog-foreigner-renting.md](../marketing/blog-foreigner-renting.md)）。未公開。一次情報のURLと公開先は未確認
- [x] 在留カードの一次情報を確認（2026-11-22、下の表）。収入証明・緊急連絡先・保証会社は事業者と物件で異なるため、記事では「目安」として扱う
- [ ] 設定や文言が第1弾の第3章と矛盾しないように揃える（本文凍結中は触らない）
- [ ] 商品リンクは1つだけ。同じく実績は書かない

## 一次情報のURL（2026-11-22 18:35 JST 確認済み）

方法: ログインなしの HTTP GET（urllib）。 e-Gov のページはJavaScript描画のため、公式 API `https://laws.e-gov.go.jp/api/1/lawdata/<lawId>` の XML で条文を確認した。HTTP 200 と本文のキーワードを確認済み。

| 主張 | URL | 確認した本文の要点 |
|---|---|---|
| 仲介手数料は法律が上限を国土交通省告示に委任 | https://laws.e-gov.go.jp/law/327AC1000000176 | 宅地建物取引業法 第46条「報酬の額は、国土交通大臣の定めるところによる」。第46条自体に金額はない |
| 上限額（借主の原則0.5か月分） | https://www.mlit.go.jp/notice/noticedata/sgml/1970/26197000/26197000.html | 建設省告示第1552号（改正済）。貸借の媒介は双方の合計が「借賃の一月分に相当する金額以内」。居住用は一方から受ける額を「借賃の一月分の二分の一以内」とし、事前に承諾した場合のみ例外 |
| 転入届は14日以内 | https://laws.e-gov.go.jp/law/342AC0000000081 | 住民基本台帳法 第22条「転入をした日から十四日以内に」市町村長に届け出る |
| 原状回復は通常の使用による損耗を含まない | https://www.mlit.go.jp/jutakukentiku/house/jutakukentiku_house_tk3_000020.html | 「いわゆる経年変化、通常の使用による損耗等の修繕費用は、賃料に含まれるもの」 |
| 原状回復ガイドライン本文（PDF） | https://www.mlit.go.jp/jutakukentiku/house/torikumi/honbun2.pdf | ダウンロードページ https://www.mlit.go.jp/jutakukentiku/house/jutakukentiku_house_tk3_000021.html から取得。PDF 1,707,509 バイト、HTTP 200 |
| 在留カードの説明 | https://www.moj.go.jp/isa/applications/procedures/whatzairyu_00001.html | 出入国在留管理庁「在留カードとは？」。手続一覧 https://www.moj.go.jp/isa/applications/procedures/zairyucard.html も HTTP 200 |
| FRESC（外国人在留支援センター） | https://www.moj.go.jp/isa/support/fresc/fresc01.html | 出入国在留管理庁「外国人在留支援センター」。相談窓口 https://www.moj.go.jp/isa/support/fresc/fresc_2.html も HTTP 200 |

反映状況: 2026-11-22 に記事A/Bの本文へ一次情報リンクを反映済み。公開直前にリンクの生存を再確認する。

使い方: 記事に貼るのは上表のURLのみ。日本語の公式ページを指す場合はアンカーテキストを英語にしてよい。公開直前にリンクの生存を再確認する。数字・制度の解説は上記の範囲だけを書く（それ以外は「目安」または削除）。

## 本人が行う操作

- 公開先の規約確認と選択
- アカウント作成、記事の投稿、公開ボタン
- 公開後のURLと表示の確認（リンク切れ、文字化け、モバイル表示）

## 記録の形

| 日時 | 方法（ログインあり／なし・画面名） | 公開先 | URL | 確認した表示 |
|---|---|---|---|---|
| 未取得 | 未取得 | 未取得 | 未取得 | 未取得 |

公開したら [schedule.md](schedule.md) の Day 14 / Day 30 と [monitor-youtube-decision.md](monitor-youtube-decision.md) の「ブログ公開から30日」条件に反映する。YouTube再検討の条件成立時も、判断は pi が行う。
