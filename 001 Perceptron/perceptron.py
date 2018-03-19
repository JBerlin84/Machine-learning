import random
import array

class Perceptron:
    weight1 = random.randrange(-1,1)
    weight2 = random.randrange(-1,1)
    weightbias = random.randrange(-1,1)
    bias = 1
    learningRate = 0.1

    def activate(self, sum):
        if sum > 0:
            return 1
        else:
            return 0

    def feedforward(self, input1, input2):
        sum = input1*self.weight1+input2*self.weight2+self.bias*self.weightbias
        return self.activate(sum)
    
    def train(self, input1, input2, ans):
        guess = self.feedforward(input1, input2)
        error = ans - guess
        self.weight1 += self.learningRate*error*input1
        self.weight2 += self.learningRate*error*input2

perceptron = Perceptron()
input1 = array.array('f')
input2 = array.array('f')
answers = array.array('f')

xmin = -1
xmax = 1
ymin = 1
ymax = -1

def f(x):
    return 0.3*x+0.4

def setup():
    # Generate test data
    for i in range(1000):
        input1.append(random.uniform(xmin,xmax))
        input2.append(random.uniform(ymin, ymax))
        if input2[i] < f(input1[i]):
            answers.append(-1)
        else:
            answers.append(1)

def main():
    print(len(input1))
    print(len(input2))
    print(len(answers))
    for i in range(1000):
        perceptron.train(input1[i], input2[i], answers[i])
    print("All data is trained")

setup()
main()