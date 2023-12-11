import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from graphviz import Source
from sklearn.tree import export_graphviz

def menu():
    print("""
    1 Read CSV file
    2 Print current data
    3 Add manual data
    4 Build decision tree
    5 Add new observation
    6 Classify test data
    7 Exit program
          """)
    is_valid = False
    while not is_valid:
        input_data = input('Your choice: ') 
        if input_data in [f'{x}' for x in range(1,8)]:
            is_valid = True
    return input_data
        

def load_csv_file(file_name):
    data = pd.DataFrame()
    try: 
        data = pd.read_csv(file_name, dtype = 'category', sep = ',')
    except FileNotFoundError:
        print('Error when reading file: File', "'"+input_name+"'", 'does not exist')
    return data
        

def add_data(data_frame):
    df_dict = {}
    if not data_frame.empty:
        for index, catname in enumerate(data_frame.columns):
            possible_value = data_frame[catname].cat.categories.tolist()
            if index == 0:
                value = input(f'Data identifier ({catname}): ')
            else:
                print(catname)
                print(f'Possible values: {possible_value}')
                is_valid = False
                while not is_valid:
                    value = input('Input value: ')
                    if value in possible_value:
                        is_valid = True
            df_dict[catname] = value
        new_df = pd.DataFrame([df_dict])
        return_df = data_frame.merge(new_df, how='outer')
        return return_df
    else:
        print('No data in the frame to add to')
        return data_frame
    
def build_decision_tree(data_frame):
    if not data_frame.empty:
        df_coded = pd.DataFrame()
        for _, catname in enumerate(data_frame.columns):
            df_coded[catname] = data_frame[catname].astype('category').cat.codes
        
        X = df_coded.iloc[:,1:-1] 
        y = df_coded.iloc[:,-1]
        
        dtree = DecisionTreeClassifier(criterion='entropy', random_state=0)
        dtree.fit(X,y)

        # graph = Source( export_graphviz(dtree, out_file=None, feature_names=X.columns))
        # graph.format = 'png'
        # graph.render('Dicision_tree',view=True)
        return dtree
    else:
        print('Error no data to create tree from')
        return None

        

if __name__ == '__main__':
    
    data_frame = pd.DataFrame()
    is_running = True
    while is_running:
        choice = menu()
        
        if choice == '1':
            # input_name = input('Filename: ')
            input_name = 'Djur.csv'
            data_frame = load_csv_file(input_name)
        elif choice == '2':
            print(data_frame)
        elif choice == '3':
            data_frame = add_data(data_frame)
        elif choice == '4':
            decision_tree = build_decision_tree(data_frame)
            print(decision_tree)
        elif choice == '5':
            print(f'Your choice is {choice}')
        elif choice == '6':
            print(f'Your choice is {choice}')
        elif choice == '7':
            print('Program closing ...')
            print('Goodbye!')
            is_running = False


        
                
