import pandas as pd

data = {'연령대코드': ['AGE_001', 'AGE_002', 'AGE_003', 'AGE_004', 'AGE_005', 'AGE_006', 'AGE_007', 'AGE_008'],
            '연령대': ['10대','20대','30대','40대','50대','60대','70대','비회원 or 외국인']}
df = pd.DataFrame(data)

df.to_csv('서울특별시 공공자전거 이용정보(월별) 연령대코드.csv')
print(df)