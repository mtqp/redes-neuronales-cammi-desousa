%Examples
neuralType = 'traingd';           %Gradient descent backpropagation

%Parameters set dynamically
epochs = SET_THIS;
etta = SET_THIS;
neuralType = SET_THIS;
epsilon = SET_THIS;

%Skeleton
net = feedforwardnet(hiddenNodes);  %Set neuronal net with N hidden nodes
net.trainFcn = neuralType;
net.trainParams.goal = epsilon      %Set epsilon
net.trainParams.epochs = epochs;    %Set epochs
net.trainParams.lr = etta;          %Set etta