import sqlite3

# データベースに接続
conn = sqlite3.connect('instance/users.db')
cursor = conn.cursor()

# 更新対象のモデル名と新しい表示名のマッピング
updates = {
    "要件定義書のヒアリングAI": "1.要件定義書のヒアリングAI",
    "ビジネス向け要件定義書": "2.ビジネス向け要件定義書",
    "エンジニア向け要件定義書": "3.エンジニア向け要件定義書",
    "金額提示相談AI": "4.金額提示相談AI"
}

# 各モデル名の表示名を更新
for name, display_name in updates.items():
    cursor.execute(
        "UPDATE model_name SET display_name = ? WHERE name = ?",
        (display_name, name)
    )
    print(f"Updating {name} to {display_name}")

# 変更を保存
conn.commit()
print("Database updated successfully")

# データベース接続を閉じる
conn.close()
