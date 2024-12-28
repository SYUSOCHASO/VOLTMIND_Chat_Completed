from app import db, ModelName
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/users.db'
db.init_app(app)

with app.app_context():
    # 更新対象のモデル名と新しい表示名のマッピング
    updates = {
        "要件定義書のヒアリングAI": "1.要件定義書のヒアリングAI",
        "ビジネス向け要件定義書": "2.ビジネス向け要件定義書",
        "エンジニア向け要件定義書": "3.エンジニア向け要件定義書",
        "金額提示相談AI": "4.金額提示相談AI"
    }
    
    # 各モデル名の表示名を更新
    for name, display_name in updates.items():
        model = ModelName.query.filter_by(name=name).first()
        if model:
            print(f"Updating {name} to {display_name}")
            model.display_name = display_name
    
    # 変更を保存
    db.session.commit()
    print("Database updated successfully")
