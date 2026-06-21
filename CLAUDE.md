# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 起動コマンド

```powershell
streamlit run app.py
```

ブラウザで `http://localhost:8501` が自動的に開く。終了は `Ctrl + C`。

## 依存関係のインストール

```powershell
pip install -r requirements.txt
```

## API キー設定

`.env` ファイルを作成して `GEMINI_API_KEY=your_key` を記載するか、アプリ起動後にサイドバーから直接入力する。

## アーキテクチャ

`app.py` 1ファイルで完結するシングルページ Streamlit アプリ。

**データフロー:**
1. サイドバーの `st.radio` でツールを選択 → `tool` 変数に文字列が入る
2. サイドバー下部の API キー入力 → `genai.configure()` でモデルを初期化
3. 各ツールは `if/elif` ブロックで分岐し、ユーザー入力を受けてプロンプトを組み立て `generate()` を呼ぶ
4. 結果を `st.markdown` または `st.text_area` で表示し、`st.download_button` でダウンロード提供

**主要な関数:**
- `get_api_key()` — `.env` から `GEMINI_API_KEY` を読み込む
- `init_model(api_key)` — `gemini-2.0-flash` モデルを初期化して返す
- `generate(model, prompt)` — プロンプトを送信してテキストを返す

## ツール一覧と分岐キー

| `tool` の値 | 概要 |
|---|---|
| `"📝 ブログ記事生成"` | テーマ・文体・長さを指定して記事生成 |
| `"📧 メール作成・編集"` | タブで新規作成 / 既存編集を切り替え |
| `"📋 文章要約"` | 長さ・形式を選んで要約 |
| `"🔍 文章校正・言い換え"` | 校正 / 言い換えモードを選択 |
| `"📱 SNS 投稿文生成"` | プラットフォーム別に複数バリエーション生成 |
| `"🎨 文体変換"` | 変換前後を横並びで表示 |

## 新しいツールを追加する手順

1. サイドバーの `st.radio` の `options` リストに新しいツール名を追加
2. `app.py` 末尾に `elif tool == "新ツール名":` ブロックを追加
3. ブロック内で入力 UI → プロンプト組み立て → `generate()` 呼び出し → 結果表示の流れで実装
