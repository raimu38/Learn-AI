import os
from typing import Dict
from google.adk.agents import Agent

# Function Tool: ユーザーからの入力を正確にファイルに保存する
#
# パラメータとして 'src' と 'filename' を受け取り、
# - 'memo' で始まる場合のみ処理
# - カレントディレクトリ以下へのファイル操作のみ許可
# - 存在する場合は追記モード、存在しない場合は新規作成モードで処理

def getAndWriteToFile(src: str, filename: str) -> Dict[str, str]:
    """
    'memo' で始まるテキストを指定ファイルにMarkdown形式で書き込む Function Tool。

    Parameters:
      src (str): ユーザー入力全体（'memo'から始まる）
      filename (str): 書き込み先ファイルパス（カレントディレクトリ以下のみ許可）

    Returns:
      dict: 処理結果
        - status: 'success' | 'skipped' | 'error'
        - message: エラー時の説明、または 'OK'
        - file: 書き込み先ファイルの絶対パス
        - action: 'write' | 'append'
    """
    prefix = "memo"
    if not src.startswith(prefix):
        return {"status": "skipped", "message": "Input does not start with 'memo'."}

    # メモ部分を切り出して行末に改行を付与
    content = src[len(prefix):].lstrip() + "\n"
    cwd = os.getcwd()

    # 絶対パスを生成して範囲をチェック
    abs_path = os.path.abspath(filename)
    if not abs_path.startswith(cwd + os.sep):
        return {"status": "error", "message": "Invalid path: outside working directory.", "file": abs_path}

    # ファイルの存在有無でモードを選択
    mode = 'a' if os.path.exists(abs_path) else 'w'
    try:
        with open(abs_path, mode, encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        return {"status": "error", "message": str(e), "file": abs_path}

    action = 'append' if mode == 'a' else 'write'
    return {"status": "success", "message": "OK", "file": abs_path, "action": action}

# Agent 定義: メモ書き込み専用エージェント
root_agent = Agent(
    name="memo_agent",
    model="gemini-2.0-flash-exp",
    description="ユーザーの 'memo' 入力を受け取り、指定ファイルに正確に保存するエージェント",
    instruction=(
        "You are an agent that records any user input starting with 'memo' to a file. "
        "When user says 'memo <text>', ask for a filename if not provided, ensure the file path is under the current working directory, "
        "and then call the function with 'src' and 'filename' parameters. Do not allow paths outside the current directory."
    ),
    tools=[getAndWriteToFile],
)
