import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import matplotlib.pyplot as plt
import ssl
import certifi

# Định nghĩa một hàm tạo SSLContext với chứng chỉ từ certifi
def create_ssl_context(*args, **kwargs):
    return ssl.create_default_context(cafile=certifi.where())

# Gán hàm này cho ssl._create_default_https_context
ssl._create_default_https_context = create_ssl_context
# Tải dữ liệu
(train_X, train_y), (test_X, test_y) = mnist.load_data()

# Chuẩn hóa dữ liệu
train_X = train_X.astype('float32') / 255
test_X = test_X.astype('float32') / 255

train_X = np.expand_dims(train_X, -1)
test_X = np.expand_dims(test_X, -1)

train_y = to_categorical(train_y, 10)
test_y = to_categorical(test_y, 10)

# Xây dựng mô hình
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Biên dịch mô hình
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Huấn luyện mô hình
history = model.fit(train_X, train_y,
                    epochs=10,
                    batch_size=128,
                    validation_split=0.2)

# Đánh giá mô hình
test_loss, test_accuracy = model.evaluate(test_X, test_y)
print("Test accuracy:", test_accuracy)

# Dự đoán
predictions = model.predict(test_X)
predicted_classes = np.argmax(predictions, axis=1)
actual_classes = np.argmax(test_y, axis=1)

# Hiển thị một vài kết quả
plt.figure(figsize=(12, 5))
for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.imshow(test_X[i].reshape(28, 28), cmap='gray')
    plt.title(f"Actual: {actual_classes[i]}, Predicted: {predicted_classes[i]}")
    plt.axis('off')
plt.show()

# Vẽ biểu đồ Loss
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.show()

# Vẽ biểu đồ Accuracy
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.legend()
plt.show()
