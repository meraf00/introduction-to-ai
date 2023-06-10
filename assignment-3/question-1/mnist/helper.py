import math


def flatten(array):
    flat = []

    for item in array:
        try:
            iter(item)
            flat.extend(flatten(item))
        except:
            flat.append(item)

    return flat


def reshape(array, rows, cols):
    flat_array = flatten(array)

    if rows * cols != len(flat_array):
        raise Exception(f"Can't reshape array to ({rows}, {cols})")

    reshaped = [[0] * cols for _ in range(rows)]    

    for row in range(rows):
        for col in range(cols):
            reshaped[row][col] = flat_array[row * cols + col]

    return reshaped


def sigmoid_scaler(x):
    return 1 / (1 + math.exp(-x))


def sigmoid_vector(X):
    flat = flatten(X)

    for i in range(len(flat)):
        flat[i] = sigmoid_scaler(flat[i])

    return flat


def predict(sample_x, weight):
    # calculate z = sum(w * x + b)
    # here bias (b) is also included in weight
    z = 0
    for x, w in zip(sample_x, weight):
        z += w * x

    # sigmoid(z)
    return sigmoid_scaler(z)


def cross_entropy_loss(predicted_value, actual_value):
    y = actual_value
    y_pred = predicted_value

    if y == 1:
        return -math.log(y_pred + 0.000001)

    else:
        return -math.log(1 - y_pred + 0.000001)


def cost_function(datas, target, weight, bias):
    cost = 0

    for x, y in zip(datas, target):
        y_pred = predict(x, weight, bias)

        cost += cross_entropy_loss(y_pred, y)

    return cost / len(datas)


def gradient_decent(X, label, weight=None, learning_rate=0.1):
    n_features = len(X[0])

    # initialize weight with zero (equal length to x's features)
    if weight == None:
        weight = [0] * n_features

    loss = 0

    for x, y in zip(X, label):
        y_pred = predict(x, weight)
        loss += cross_entropy_loss(y_pred, y)

        # dw = (y_pred - y) * x
        # weight = weight - learning_rate * dw
        err = y_pred - y
        for i in range(n_features):
            dw_i = err * x[i]
            weight[i] -= learning_rate * dw_i

    return weight, loss / len(X)


def train(x_train, y_train, learning_rate, epoch, verbose=False):
    weight = [0] * len(x_train[0])

    history = []

    for i in range(epoch):
        weight, loss = gradient_decent(x_train, y_train, weight, learning_rate)

        history.append(loss)

        if verbose:
            print(f"Epoch [{i}]\n\t- Cross entropy loss: {loss}")

    return weight, history
