# Vertex Group Merger
## 概要
複数の頂点グループを選択して1つの頂点グループにマージするためのBlenderアドオンです。ウェイト値は加算方式または減算方式でマージでき、合計ウェイトの調整やソースグループの保持などのオプションも利用できます。  
Vertex Weight Mix(頂点ウェイト合成)モディファイアーを何個も設定することなくサクッとマージできます。

## 機能
- **加算モード**: ソースグループのウェイトをターゲットグループに加算
- **減算モード**: ソースグループのウェイトをターゲットグループから減算
- **ウェイト制御**: 合計ウェイトが1.0を超えないように調整するオプション
- **グループ保持**: マージ後にソースグループを保持するオプション
- **範囲選択モード**: 複数の頂点グループを範囲選択で効率的に選択

## 使用方法
1. 頂点グループを持つメッシュオブジェクトを選択
2. 3Dビューの右側パネル（Nキーで表示）内の「Edit」タブを開く
3. マージ先となる頂点グループを「Target Group」で選択
4. ラジオボタンで操作モード（Add または Subtract）を選択
5. マージ元となる頂点グループをリストから選択
6. 必要に応じて「Maintain Total Weight ≤ 1.0」オプションを設定
7. ソースグループを保持したい場合は「Keep Source Groups」オプションを設定
8. 「Merge Selected Groups」ボタンをクリック

## 操作モード
- **Add（加算）**: ソースグループのウェイトをターゲットグループのウェイトに加算します（デフォルト動作）
- **Subtract（減算）**: ソースグループのウェイトをターゲットグループのウェイトから減算します
  - 結果的にウェイトが0になった頂点は、ターゲットグループから自動的に削除されます

## オプション
- **Maintain Total Weight ≤ 1.0**: 最終的な頂点ウェイトが1.0を超えないようにします
- **Keep Source Groups**: マージ処理後にソースグループを保持します（頂点グループを削除せずにマージできます）

## 範囲選択モード
範囲選択モードを有効にすると、複数の頂点グループを効率的に選択できます。

### 使用方法
1. **範囲選択モードの有効化**: ソースグループリストの上部にある「Range Selection Mode」チェックボックスをオンにします
2. **開始点の選択**: 範囲選択したい最初の頂点グループのチェックボックスをクリックします
3. **範囲の選択**: 範囲選択したい最後の頂点グループのチェックボックスをクリックします
4. **結果**: 開始点から終了点までのすべての頂点グループが、最後にクリックしたチェックボックスの状態（ON/OFF）に統一されます

### 動作例
- **範囲をONにする場合**: Group_01をクリック（OFF→ON）してからGroup_05をクリック（OFF→ON）すると、Group_01〜Group_05がすべてONになります
- **範囲をOFFにする場合**: Group_03をクリック（ON→OFF）してからGroup_07をクリック（ON→OFF）すると、Group_03〜Group_07がすべてOFFになります

### 自動リセット機能
- **オブジェクト変更時**: 別のオブジェクトを選択すると、範囲選択モードが自動的に解除されます
- **マージ完了後**: マージ操作が完了すると、範囲選択モードが自動的に解除されます

## 要件
Blender 3.6.0以上

## インストール方法
1. Blenderの「編集」→「プリファレンス」→「アドオン」を開きます
2. 「インストール」ボタンをクリックします
3. ダウンロードした`vertex_group_merger.zip`を選択します
4. アドオン一覧で「Vertex Group Merger」を有効化します

## ライセンス
GPL v3 License (LICENSE参照) 個人・商用問わず自由に利用できます。