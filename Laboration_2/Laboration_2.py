from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
import pandas as pd
from sklearn import tree

def predict_accuracy(filename):

    X = filename.iloc[:,2:]
    y = filename.iloc[:,1]

    knn = KNeighborsClassifier(n_neighbors = 3)
    knn.fit(X.values, y)

    instances = X.values.tolist()
    y_true = y.tolist()
    y_predicted = knn.predict(instances)
    accuracy = accuracy_score(y_true,y_predicted,normalize=True)
    print(f"Accuracy is {accuracy}")


def uppgift_1_1():
    FILE = "Laboration_2/1-titanic-small.csv"

    df = pd.read_csv(FILE)

    X = df.iloc[:,2:]
    y = df.iloc[:,1]

    knn = KNeighborsClassifier(n_neighbors = 3)
    knn.fit(X.values, y)

    new_instances_3 = [[49 , 0] , [35 , 2] , [12 , 1]]
    y_true = [1,0,1]
    y_predicted = knn.predict(new_instances_3)
    accuracy = accuracy_score(y_true,y_predicted,normalize=True)
    print(f"Accuracy is {accuracy}")

    predict_accuracy(df)

def uppgift_1_2():
    FILE = "Laboration_2/2-titanic2attr.csv"
    titanic2attr = pd.read_csv(FILE)
    titanic2attr = titanic2attr.dropna()

    predict_accuracy(titanic2attr)

def uppgift_1_3():
    FILE = "Laboration_2/3-titanic.csv"
    
    titanic3 = pd.read_csv(FILE)
    titanic3 = titanic3.dropna()

    le = preprocessing.LabelEncoder()

    for num in range(10):
        if num == 3 or num == 7 or num == 8 or num == 9:
            le.fit(titanic3.iloc[:,num])
            list(le.classes_)
            titanic3[titanic3.columns[num]] = le.transform(titanic3[titanic3.columns[num]])
    
    predict_accuracy(titanic3)

def uppgift_2():
    FILE = "Laboration_2/3-titanic.csv"
    titanic3 = pd.read_csv(FILE)
    
    df_shape = titanic3.shape
    print(f"\nShape is {df_shape}")
    
    df_type = titanic3.dtypes
    print(f"\nType is {df_type}")
    
    df_describe = titanic3.describe()
    print(f"\nType is {df_describe}")

    sex_list = titanic3[titanic3.columns[3]]
    survived_list = titanic3[titanic3.columns[1]]

    print(len(sex_list)==len(survived_list))
    
    female = 0
    f_survived = 0 
    f_died = 0
    male = 0
    m_survived = 0 
    m_died = 0
    index = 0
    for item in sex_list:
        status = survived_list[index]
        if item == "female":
            female += 1
            if status == 0:
                f_survived += 1
            else:
                f_died += 1
        else:
            male +=1
            if status == 0:
                m_survived += 1
            else:
                m_died += 1
        index += 1
    
    print(female)
    print(male)
    print(f_died,f_survived,m_died,m_survived)
    print(f_died + m_died , f_survived + m_survived)

    print((f_survived + m_survived) /(male + female) )
    print(f_died / (female))
    print(m_died / (male))
    print(f_died / (female + male))
    print(m_died / (male + female))

def uppgift_3_1():
    FILE = "Laboration_2/3-titanic.csv"

    df = pd.read_csv(FILE)
    df = df.dropna()

    le = preprocessing.LabelEncoder()

    for num in range(10):
        if num == 3 or num == 7 or num == 8 or num == 9:
            le.fit(df.iloc[:,num])
            list(le.classes_)
            df[df.columns[num]] = le.transform(df[df.columns[num]])

    X = df.iloc[:,2:]
    y = df.iloc[:,1]

    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=1)

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test,y_pred)
    print(accuracy)

def uppgift_3_2():
    FILE = "Laboration_2/3-titanic.csv"

    df = pd.read_csv(FILE)
    df = df.dropna()

    le = preprocessing.LabelEncoder()

    for num in range(10):
        if num == 3 or num == 7 or num == 8 or num == 9:
            le.fit(df.iloc[:,num])
            list(le.classes_)
            df[df.columns[num]] = le.transform(df[df.columns[num]])

    X = df.iloc[:,2:]
    y = df.iloc[:,1]

    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=1)

    regressor = RandomForestClassifier()
    regressor.fit(X_train,y_train)
    y_pred = regressor.predict(X_test)
    accuracy = accuracy_score(y_test,y_pred)
    print(accuracy)

def extra_uppgift_5():
    FILE = "Laboration_2/3-titanic.csv"

    df = pd.read_csv(FILE)
    df = df.dropna()

    le = preprocessing.LabelEncoder()

    for num in range(10):
        if num == 3 or num == 7 or num == 8 or num == 9:
            le.fit(df.iloc[:,num])
            list(le.classes_)
            df[df.columns[num]] = le.transform(df[df.columns[num]])

    X = df.iloc[:,2:]
    y = df.iloc[:,1]

    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=1)

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test,y_pred)
    print(accuracy)
    precision = precision_score(y_test,y_pred)
    print(precision)

    regressor = RandomForestClassifier()
    regressor.fit(X_train,y_train)
    y_pred = regressor.predict(X_test)
    accuracy = accuracy_score(y_test,y_pred)
    print(accuracy)
    precision = precision_score(y_test,y_pred)
    print(precision)
    f1 = f1_score(y_test,y_pred,zero_division=1)
    print(f1)

def main():
    # uppgift_1_1()
    # uppgift_1_2()
    # uppgift_1_3()
    uppgift_2()
    # uppgift_3_1()
    # uppgift_3_2()
    # extra_uppgift_5()

if __name__ == "__main__":
    main()