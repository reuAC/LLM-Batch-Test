# LLM-Batch-Test
[ [中文](https://github.com/reuAC/LLM-Batch-Test/blob/reuAC/README_JP.md) | [English](https://github.com/reuAC/LLM-Batch-Test/blob/reuAC/README_EN.md) | 日本語 ]

runer.py    : 大規模モデルを一度実行します。
runer2.py   : 大規模モデルを一度実行し、モデルのフィードバックを取得します。
runer3.py   : 大規模モデルをループで連続的に実行し、継続的な対話ができ、モデルのフィードバックを取得します。
web.py  : 大規模モデルとの継続的な対話が可能なウェブページを作成し、System Promptをリアルタイムで変更し、モデルのフィードバックを取得します。
make.py : パラメーターを指定して実行します。例: `python make.py -qdir=質問フォルダ -output=出力ファイル名.csv -n=各質問を何回聞くか &`質問フォルダ内のすべての .txt ファイルを巡回し、各行を質問として扱い、大規模モデルに入力します。モデルは各質問に n 回回答し、結果を集計して表形式で出力します。