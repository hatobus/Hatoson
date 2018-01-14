import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()

 # load up the entries as environment variables
load_dotenv(dotenv_path)

# botアカウントのトークンを指定
API_TOKEN = os.environ.get("SLACK_API_KEY")

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "ポッポ〜（意味不明）"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']
