# Changelog / 更新履歴

🇬🇧 **English** | 🇯🇵 **日本語**

All notable changes to this project will be documented in this file.
このプロジェクトの注目すべき変更はすべてこのファイルに記録されます。

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
フォーマットは [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) に基づいており、
このプロジェクトは [Semantic Versioning](https://semver.org/spec/v2.0.0.html) に準拠しています。

## [Unreleased]

### Added

- Add "+" button next to target group selector to create a new vertex group directly from the panel

### Fixed

- Disable merge button in Edit Mode to prevent errors
- Fix error when merging after vertex groups are externally deleted or renamed
- Fix source groups list not updating when vertex groups are added, deleted, or renamed on the same object
- Fix last vertex group being incorrectly highlighted when changing target group while in range selection mode

### Improved

- Improve merge performance for meshes with many vertices
- Improve internal stability of object tracking and timer handling
- Remove near-zero weights (< 0.000001) after subtraction to keep vertex groups clean

### 追加

- マージ先グループの横に「+」ボタンを追加し、パネルから直接新しい頂点グループを作成可能に

### 修正

- 編集モード中にマージボタンを無効化し、エラーを防止
- 頂点グループが外部で削除・リネームされた後にマージするとエラーになる問題を修正
- 同一オブジェクト上で頂点グループを追加・削除・リネームしてもソースグループ一覧が更新されない問題を修正
- 範囲選択モード中にマージ先グループを変更すると、最後の頂点グループが選択状態になる問題を修正

### 改善

- 頂点数の多いメッシュでのマージ性能を改善
- オブジェクト追跡とタイマー処理の内部安定性を向上
- 減算時にゼロに近い微小ウェイト（0.000001未満）を自動削除し、頂点グループをクリーンに保つように

## [0.4.0] - 2025-06-26

### Added

- Add Japanese language support

### 追加

- 日本語に対応

## [0.3.0] - 2025-06-12

### Added

- Add range selection mode for selecting multiple vertex groups at once

### Improved

- Set target vertex group as active after merging, so the merge result is immediately visible
- Reset range selection mode after merging vertex groups

### 追加

- 範囲選択モードを追加

### 改善

- マージ後、対象の頂点グループをアクティブにしてマージ結果をすぐに確認できるように
- マージ後に範囲選択モードをリセットするように

## [0.2.1] - 2025-05-18

### Fixed

- Fix vertex group names being translated in UI list

### 修正

- 頂点グループ名の一覧において、頂点グループ名が翻訳されてしまう問題を修正

## [0.2.0] - 2025-05-18

### Added

- Add option to keep source groups after merging instead of deleting them
- Add subtract operation mode for vertex group merging

### 追加

- マージ後に頂点グループを削除せず維持するオプションを追加
- ウェイトを減算でマージできる機能を追加

## [0.1.0] - 2025-04-28

Initial release.
初版リリース。

### Added

- Merge multiple vertex groups into a single target vertex group
- Add (sum) merge mode with optional weight clamping
- Support for selecting source and target vertex groups from a UI list

### 追加

- 複数の頂点グループを選択して1つの頂点グループにマージする機能
- 加算方式でのマージ（合計ウェイトのクランプオプション付き）
- UIリストからソース・ターゲット頂点グループを選択可能
