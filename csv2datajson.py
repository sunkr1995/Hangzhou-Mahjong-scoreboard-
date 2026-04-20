import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    data = {
        "users": [],
        "records": []
    }
    
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        headers = next(reader)
        
        # 1. 提取用户列表（跳过第一列"日期"）
        user_names = headers[1:]
        for name in user_names:
            if name.strip():
                data["users"].append({
                    "name": name.strip(),
                    "participateInRanking": True # 默认所有人都参与排名
                })
        
        # 2. 提取每日得分记录
        for row in reader:
            if not row or not row[0].strip(): 
                continue
                
            date = row[0].strip()
            scores = {}
            for i, name in enumerate(user_names):
                score_str = row[i+1].strip()
                if score_str: # 确保有分数才记录
                    scores[name.strip()] = int(score_str)
            
            data["records"].append({
                "date": date,
                "scores": scores
            })
            
    # 写入 JSON 文件
    with open(json_file_path, mode='w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
    print(f"转换成功！数据已保存至 {json_file_path}")

# 执行转换
csv_to_json('output.csv', 'data.json')
