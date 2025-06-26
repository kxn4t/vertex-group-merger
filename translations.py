# Translation dictionary for Vertex Group Merger addon
# Format: {locale: {(context, message): translation, ...}, ...}

translations_dict = {
    "ja_JP": {
        # Operator labels and descriptions
        ("*", "Merge selected vertex groups into specified target group"): "選択した頂点グループを指定したマージ先グループにマージ",
        ("*", "Merge Vertex Groups"): "頂点グループをマージ",
        
        # Property labels and descriptions
        ("*", "Target Group"): "マージ先グループ",
        ("*", "Selected groups will be merged into this group"): "選択した頂点グループはこのグループにマージされます",
        ("*", "Maintain Total Weight ≤ 1.0"): "合計ウェイトを1.0以下に維持",
        ("*", "Adjust merged weights so total does not exceed 1.0"): "マージ後のウェイトの合計が1.0を超えないように調整",
        ("*", "Keep Source Groups"): "マージ元グループを保持",
        ("*", "Keep source groups after merging (do not delete them)"): "マージ後もマージ元グループを保持（削除しない）",
        ("*", "Operation Mode"): "操作モード",
        ("*", "How to merge vertex groups"): "頂点グループのマージ方法",
        ("*", "Add"): "加算",
        ("*", "Add source groups to target"): "マージ元グループのウェイトをマージ先に加算",
        ("*", "Subtract"): "減算",
        ("*", "Subtract source groups from target (vertices with zero weight will be removed)"): "マージ元グループのウェイトをマージ先から減算（ウェイトがゼロになった頂点は削除されます）",
        ("*", "Range Selection Mode"): "範囲選択モード",
        ("*", "Enable range selection for vertex group checkboxes"): "頂点グループの範囲選択を有効化",
        
        # Panel UI strings
        ("*", "Select a mesh object with vertex groups"): "頂点グループを持つメッシュオブジェクトを選択してください",
        ("*", "Select Source Groups"): "マージ元グループを選択",
        ("*", "Range Selection Mode Active"): "範囲選択モード有効",
        ("*", "Click another checkbox to select range"): "別のチェックボックスをクリックして範囲を選択",
        ("*", "Click a checkbox to start range selection"): "チェックボックスをクリックして範囲選択を開始",
        ("*", "Merge Selected Groups"): "選択した頂点グループをマージ",
        ("*", "Switch to Weight Paint Mode"): "ウェイトペイントモードに切り替え",
        
        # Error messages
        ("*", "Target group not found"): "マージ先グループが見つかりません",
        ("*", "No source groups selected"): "マージ元グループが選択されていません",
        
        # Success messages (complete sentences with placeholders)
        ("*", "Groups {source} merged into {target}"): "{source}を{target}にマージしました",
        ("*", "Groups {source} subtracted from {target}"): "{source}を{target}から減算しました",
        ("*", "{count} vertices removed with zero weight"): "{count}個の頂点がウェイトゼロで削除されました",
        ("*", "(source groups kept)"): "（マージ元グループは保持されました）",
    }
}