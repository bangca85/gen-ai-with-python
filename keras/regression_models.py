import numpy as np
from tensorflow.keras.datasets import boston_housing
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt
import ssl
import certifi

# Định nghĩa một hàm tạo SSLContext với chứng chỉ từ certifi
def create_ssl_context(*args, **kwargs):
    return ssl.create_default_context(cafile=certifi.where())

# Gán hàm này cho ssl._create_default_https_context
ssl._create_default_https_context = create_ssl_context

# Tải dữ liệu
(train_X, train_y), (test_X, test_y) = boston_housing.load_data()

# Chuẩn hóa dữ liệu
mean = train_X.mean(axis=0)
std = train_X.std(axis=0)

train_X = (train_X - mean) / std
test_X = (test_X - mean) / std

# Xây dựng mô hình
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(train_X.shape[1],)))
model.add(Dense(64, activation='relu'))
model.add(Dense(1))

# Biên dịch mô hình
model.compile(optimizer='rmsprop',
              loss='mse',
              metrics=['mae'])

# Huấn luyện mô hình
history = model.fit(train_X, train_y,
                    epochs=100,
                    batch_size=16,
                    validation_split=0.2)

# Đánh giá mô hình
test_loss, test_mae = model.evaluate(test_X, test_y)
print("Test MAE:", test_mae)

# Dự đoán
predictions = model.predict(test_X)

# Vẽ biểu đồ Loss
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Val Loss')
plt.legend()
plt.show()

# Vẽ biểu đồ MAE
plt.plot(history.history['mae'], label='Train MAE')
plt.plot(history.history['val_mae'], label='Val MAE')
plt.legend()
plt.show()
