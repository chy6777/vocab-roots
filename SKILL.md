---
name: vocab-roots
description: 把 Excel(.xlsx) 或 CSV 格式的英语单词表转换为带"词根词缀解析"列的版本，逐词标注 前缀/词根/后缀 (word root, prefix, suffix annotation)。当用户提到"词根词缀"、"添加词根"、"单词表加词根"、word list 加 root/affix、或需要给词汇表做构词法分析时使用。
---

# 词汇表添加词根词缀

将 Excel 或 CSV 格式的英语单词表转换为新增一列"词根词缀解析"的 CSV，
每个单词标注其 前缀(如 re- 再)、词根(如 ject 投掷)、后缀(如 -tion 名词)，
辅助记忆。本技能目录下有两个脚本：

- `add_roots.py`：核心脚本，按内置前缀/后缀/词根字典对单词做拆分解析
- `excel_to_csv.py`：先把 Excel 转成 CSV（依赖 pandas + openpyxl）

## 工作流

1. **输入是 Excel(.xlsx)**：先转 CSV
   ```
   python excel_to_csv.py 输入.xlsx [输出.csv] [工作表名或序号]
   ```
   缺省输出同名 `.csv`。多个工作表可用 `sheet_name=None`，但脚本默认单表，
   多表时请让用户确认要处理哪个表，或遍历每张表分别转换。

2. **运行核心脚本**（输入必须是 CSV，UTF-8 或带 BOM 均可）
   ```
   python add_roots.py 输入.csv [输出.csv] [单词列序号] [新列名]
   ```
   - 参数可选：输出文件缺省为 `输入名_词根词缀版.csv`；
     单词列序号缺省 0（第一列）；新列名缺省"词根词缀解析"。
   - 新列总是插入在单词列**后面**。

3. **验证**：脚本会打印总单词数、生成解析数、覆盖率。
   输出为 `utf-8-sig` 编码，Excel 直接打开不乱码。

## 注意事项

- 依赖：`pandas`、`openpyxl`（读 xlsx 用）。缺包先 `pip install openpyxl`。
- 无法拆分的基础词与短词（会/能/不能列为词根词缀的）解析列留空，属正常。
- 解析格式示例：`前缀 re-(再/回) + 词根 ject(投/掷) + 后缀 -ion(名词) → 组合记忆`
- 若输出文件被占用（PermissionError），脚本自动改输出到 `_new.csv` 结尾的文件。
- 如单词表没有表头行，可先自行加一行表头，或告诉用户脚本按首行作为表头处理。
- 该脚本假设单词在独立单元格中；不要用于整句/段落文本。