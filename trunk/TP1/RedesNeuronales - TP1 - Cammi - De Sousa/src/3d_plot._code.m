

%testing
xT = testingInput(1,:);
yT = testingInput(2,:);
zT = netTestingOutput;

xR = testingInput(1,:);
yR = testingInput(2,:);
zR = testingOutput;

figure

scatter3(xT,yT,zT, 'g.','x');
hold on;
scatter3(xR,yR,zR, 'r.','+');


%training plot
netTrainingOutput = net(trainingInput);

xT = trainingInput(1,:);
yT = trainingInput(2,:);
zT = netTrainingOutput;

xR = trainingInput(1,:);
yR = trainingInput(2,:);
zR = trainingOutput;

figure

scatter3(xT,yT,zT, 'g.','x');
hold on;
scatter3(xR,yR,zR, 'r.','+');