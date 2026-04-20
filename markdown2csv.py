import pandas as pd
import io
import re

markdown_text = """
| 日期      | 小杨 | 小朱 | 鸭鸭 | 五五 | 六六 |
| --------- | ---- | ---- | ---- | ---- | ---- |
| 2026.4.15 | 22   | -125 | 0    | 176  | 0    |
| 2026.4.18 | 128  | -148 | 43   | -186 | -156 |
| 2026.4.19 | 44   | -52  | 35   | 79   | -118 |
"""

# 1. 移除 Markdown 的分隔行 (例如 |---|---|)
cleaned_md = re.sub(r'\|[-:| ]+\|', '', markdown_text)

# 2. 读取为 DataFrame，指定分隔符为 '|'
# 使用 \s*\|\s* 可以自动处理列前后的空格
df = pd.read_csv(io.StringIO(cleaned_md.strip()), sep=r'\s*\|\s*', engine='python')

# 3. 丢弃因为行首行尾 '|' 产生的空列
df = df.dropna(axis=1, how='all')

# 3. 保存为 CSV 文件
file_name = 'output.csv'
# index=False          : 不保存 Pandas 自动生成的数字行索引
# encoding='utf-8-sig' : 强烈建议使用 utf-8-sig，这样生成的 CSV 用 Excel 打开时中文才不会乱码
df.to_csv(file_name, index=False, encoding='utf-8-sig')

print(f"转换成功！文件已保存为: {file_name}")
