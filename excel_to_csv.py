import sys
import pandas as pd


def excel_to_csv(excel_path, csv_path=None, sheet_name=0):
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    if csv_path is None:
        out = excel_path.rsplit('.', 1)[0] + '.csv'
    else:
        out = csv_path
    df.to_csv(out, index=False, encoding='utf-8-sig')
    print(f'已转换: {excel_path} -> {out}')
    return out


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('用法:')
        print('  python excel_to_csv.py 输入.xlsx [输出.csv] [工作表名或序号]')
        print('示例:')
        print('  python excel_to_csv.py 考研词汇统计_整理版.xlsx')
        print('  python excel_to_csv.py data.xlsx result.csv Sheet2')
        sys.exit(1)
    excel = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else None
    sheet = sys.argv[3] if len(sys.argv) > 3 else 0
    excel_to_csv(excel, out, sheet)