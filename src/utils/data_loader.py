import pandas as pd

def load_complaints_data(file_path):
    """
    加载客诉数据CSV文件
    :param file_path: 数据文件路径（如 data/sample.csv）
    :return: pandas.DataFrame
    """
    try:
        df = pd.read_csv(file_path)
        print(f"成功加载数据，共 {len(df)} 条记录")
        return df
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 不存在")
        return None