def studentReg(ages_train, net_worths_train):
    ### import the sklearn regression module, create, and train your regression
    ### name your regression reg

    ### your code goes here!
    from sklearn import linear_model
    regression = linear_model.LinearRegression()
    reg = regression.fit(ages_train, net_worths_train)

    return reg