"""Jag tog 15 timmar och jag tänkte att det skulle ta 10 timmar"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn import tree

# FILE = "Djur.csv"
# FILE = "Grilla.csv"
# FILE = "Test.csv"
FILE = "People.csv"

def menu():
    """Funktionen skriver ut menyval och få in användarens inmatning
    inmatning kontrolleras """
    while True:
        print("[1] Read CSV file"+
            "\n[2] Print current data"+
            "\n[3] Add manual data"+
            "\n[4] Build decision tree"+
            "\n[5] Add new observation"+
            "\n[6] Classify test data"+
            "\n[7] Exit program")
        try:
            choice = int(input("Your choice: "))
        except ValueError:
            print("\nPlease choose between 1-7!\n")
        else:
            if 0 < choice <= 7:
                return choice
            print("\nPlease choose between 1-7!\n")

def load_csv_file(file_name):
    """Funktionen öppnar endast csv-filen och returnerar data i dataframe
    parameter : sträng
    returvärde : dataframe
    """
    if file_name.endswith('.csv') is not True:
        print(f"\nError when reading file: File '{file_name}' does not exist")
        return pd.DataFrame()
    try:
        data_frame = pd.read_csv(file_name, dtype='category', sep=",")
    except FileNotFoundError:
        print(f"\nError when reading file: File '{file_name}' does not exist")
        data_frame = pd.DataFrame()
    return data_frame

def add_data(data_frame):
    """Funktionen lägger till ny data i dataframe
    parameter : dataframe
    returvärde : dataframe
    """
    if data_frame.empty:
        print("\nNo data in the frame to add to")
        return data_frame
    df_list = []
    for index, name in enumerate(data_frame.columns):
        if index == 0:
            new_data = input(f"Data identifier ({name}): ")
        else:
            requirement = data_frame[name].cat.categories.tolist()
            print(name + (f"\nPossible values: {requirement}"))
            incorrect = True
            while incorrect:
                new_data = input("Input value: ")
                if new_data in requirement:
                    incorrect = False
        df_list.append(new_data)
    data_frame.loc[len(data_frame.index)] = df_list
    return data_frame

def build_decision_tree(data_frame):
    """Funktionen skapar en beslutträd
    parameter : dataframe
    returvärde : beslutträd
    """
    if data_frame.empty:
        print("\nError no data to create tree from")
        return None
    df_coded = pd.DataFrame()
    for _ , name in enumerate(data_frame.columns):
        df_coded[f'{name}'] = data_frame[f'{name}'].astype('category').cat.codes
    x_value = df_coded.iloc[:,1:-1]
    y_value = df_coded.iloc[:,-1]
    d_tree = DecisionTreeClassifier(criterion='entropy', random_state=0)
    d_tree.fit(x_value,y_value)
    iris = load_iris()
    tree.plot_tree(d_tree.fit(iris.data, iris.target))
    plt.show()
    return d_tree

def add_observation(data_frame, test_data):
    """Funktionen lägger observationer
    parameter : dataframe, dataframe
    returvärde : dataframe
    """
    if data_frame.empty:
        print("\nNo loaded data to create test data for")
        return test_data
    data_list = []
    for _ , catname in enumerate(data_frame.columns[1:-1]):
        requirement = data_frame[catname].cat.categories.tolist()
        print(catname + f"\n{requirement}" )
        incorrect = True
        while incorrect:
            new_data = input(f"Choose the index of the desired option 0-{len(requirement)-1}: ")
            check_list = str(list(range(len(requirement))))
            if new_data in check_list:
                incorrect = False
            else:
                incorrect = True
        data_list.append(new_data)
    test_data.loc[len(test_data.index)] = data_list
    return test_data

def classify(data_frame, decision_tree, test_data):
    """Funktionen klassiferar
    parameter : dataframe, beslutträd, dataframe
    returvärde : dictionary
    """
    return_dict = {}
    if data_frame.empty or test_data.empty or decision_tree is None:
        print("\nNo loaded data to test against was found")
        return None
    for item in range(len(test_data)):
        print(item)
        test = test_data.loc[[item]]
        tree_pred = decision_tree.predict(test)
        answer = data_frame.columns[-1]
        requirement = data_frame[answer].cat.categories.tolist()
        return_dict[answer] = requirement[tree_pred[0]]
    return return_dict

def main():
    """Funktionen är huvudfunktion"""
    is_runnnig = True
    data_frame = pd.DataFrame()
    while is_runnnig:
        choice = menu()
        if choice == 1:
            # file_name = input("Enter your file name: ")
            file_name = FILE
            data_frame = load_csv_file(file_name)
            data_list = [name for _ , name in enumerate(data_frame.columns[1:-1])]
            test_data = pd.DataFrame(columns = data_list)
        elif choice == 2:
            print(f"\n{data_frame}")
        elif choice == 3:
            data_frame = add_data(data_frame)
        elif choice == 4:
            decision_tree = build_decision_tree(data_frame)
        elif choice == 5:
            try:
                test_data = add_observation(data_frame, test_data)
            except UnboundLocalError:
                print("\nNo loaded data to create test data for")
        elif choice == 6:
            try:
                cls = classify(data_frame, decision_tree, test_data)
                if cls is not None:
                    for item in cls:
                        # print(f"{item} : {cls.get(item)}")
                        print(cls.get(item))
            except UnboundLocalError:
                print("\nNo loaded data to test against was found")
        if choice == 7:
            is_runnnig = False
            print("\nProgram is closing...")

if __name__ == '__main__':
    main()
