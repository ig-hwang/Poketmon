import pandas as pd

# 예시 데이터 생성
data = {
    'user_id': [1, 1, 2, 2, 2, 3],
    'event_name': ['login', 'purchase', 'login', 'purchase', 'login', 'login'],
    'timestamp': [
        '2025-07-26', '2025-07-26',
        '2025-07-26', '2025-07-27',
        '2025-07-27', '2025-07-27'
    ]
}

df = pd.DataFrame(data)
df['timestamp'] = pd.to_datetime(df['timestamp'])

# 일자별 사용자별 요약
summary = df.groupby(['user_id', df['timestamp'].dt.date, 'event_name']) \
            .size().unstack(fill_value=0).reset_index()

summary.columns.name = None
print("일자별 사용자 요약:")
print(summary)

# 저장
summary.to_csv('user_summary_output.csv', index=False)