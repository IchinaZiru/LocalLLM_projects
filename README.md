# Local Reverse Engineering Pipeline: C++ → UML → PDF

---

これは **Tree-sitter + Python + OpenWebUI + StarCoder2 + PlantUML** を組み合わせて  
C++ ソースコードを構文解析し、クラス図を自動生成して PDF にする  
**ローカル逆解析パイプライン** のテンプレートです。

---

##  Features

-  **Tree-sitter** で構文木（AST）を生成
-  **Python Chunker** でクラス/struct構造だけを抽出
-  **StarCoder2** で構造の意味付けとPlantUMLコード生成
-  **PlantUML** でクラス図をPNG/PDFで出力
-  オフラインで動くため企業秘密やレガシー資産解析に最適

---

##  Directory Structure
```plaintext
root/
├── build/                 # Tree-sitter のビルド成果物
├── node_modules/          
├── puml/                  # 生成された .puml や PNG, PDF を置くディレクトリ
├── scripts/               # 解析用スクリプト群
│   ├── parse.js           # ASTを生成する Node.js スクリプト
│   ├── extract_classes.py # ASTからclass/structを抽出する Chunker
│   ├── create_prompt.py   # LLMに投げるプロンプトを生成する
│   ├── list_node_types.py # ASTノード種類を確認する補助スクリプト
├── src/                   # 解析対象のソースコード
│   └── Bank_System.cpp
├── tree-sitter-c/         # Cパーサー
├── tree-sitter-cpp/       # C++パーサー
├── ast.json               # Tree-sitterで生成したAST(JSON)
├── classes.json           # Chunkerで抽出した構造(JSON)
├── package.json           # npm プロジェクト設定
├── package-lock.json      
```

## Quick Start

### Install

```bash
npm init -y
npm install tree-sitter tree-sitter-cpp
```
> plantuml.jarを puml/ に配置。

### Generate AST
```bash
node scripts/parse.j
```

### Extract Classes/Structs
```bash
python scripts/extract_classes.py
```

### Create Prompt for LLM
```bash
python scripts/create_prompt.py
```

### Run LLM

### Render with PlantUML
```bash
# PNG
java -jar puml/plantuml.jar puml/class_diagram.puml

# PDF
java -jar puml/plantuml.jar -tpdf puml/class_diagram.puml
```

## Requirements
-Node.js
-Python3
-Java (OpenJDK 17+)
-PlantUML
-OpenWebUI + Ollama + StarCoder2

