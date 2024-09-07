import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 가정: 데이터는 이미 준비되어 있다고 가정
tobacco_price = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
smoking_rate = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

# 데이터 준비
X = np.array(tobacco_price).reshape(-1, 1)
y = np.array(smoking_rate)

# 경사하강법 모델 생성
model = LinearRegression()
model.fit(X, y)

# 결과 확인
print("기울기(가격 대비 흡연율 변화율):", model.coef_[0])
print("y 절편:", model.intercept_)

# 그래프 그리기
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Predicted')
plt.xlabel('Tobacco Price')
plt.ylabel('Smoking Rate')
plt.title('Tobacco Price vs Smoking Rate')
plt.legend()
plt.grid()
plt.show()

# 새로운 가격에 대한 예측
new_price = 20
predicted_smoking_rate = model.predict([[new_price]])
print(f"새로운 담배 가격 {new_price}원일 때 예측 흡연인구: {predicted_smoking_rate[0]:.2f}%")