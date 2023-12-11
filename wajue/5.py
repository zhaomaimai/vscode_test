import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def perceptron_train(X, y, learning_rate=0.1, epochs=1000):
    num_features = X.shape[1]
    weights = np.zeros(num_features)
    bias = 0

    for epoch in range(epochs):
        for i in range(X.shape[0]):
            z = np.dot(X[i], weights) + bias
            a = sigmoid(z)
            error = y[i] - a

            weights += learning_rate * error * X[i]
            bias += learning_rate * error

    return weights, bias

def perceptron_predict(X, weights, bias):
    z = np.dot(X, weights) + bias
    a = sigmoid(z)
    predictions = np.round(a)
    return predictions

def calculate_accuracy(predictions, true_labels):
    accuracy = np.mean(predictions == true_labels)
    return accuracy

# 从文件读取数据
filename = "iris-人工神经网络.txt"
data = np.loadtxt(filename, delimiter=',')

# 将数据集分成特征（X）和标签（y）
X = data[:, :-1]  # 特征
y = data[:, -1]   # 标签

# 训练感知器
weights, bias = perceptron_train(X, y)

# 在训练集上进行预测
predictions_train = perceptron_predict(X, weights, bias)

# 计算训练准确率
accuracy_train = calculate_accuracy(predictions_train, y)

print("训练后的权重:", weights)
print("训练后的偏置:", bias)
print("在训练集上的预测:", predictions_train)
print("训练准确率:", accuracy_train)
