from tkinter import *
from tkinter import messagebox
import map_functions
import BreadthFirstSearch
import DepthFirstSearch
import A_Star_Algorithm
import Uniform_Cost_Algorithm


root = Tk()
root.title('Ai project')
root.geometry("470x270")

#-------------------------------------------------------------------------------------------------------------------
# creating labels
mylabel1 = Label(root, text="select the source")
mylabel2 = Label(root, text="select the destination")
mylabel3 = Label(root, text="select the algorithm")
mylabel4 = Label(root, text="                         ")
mylabel5 = Label(root, text="                         ")

# putting labels on screen
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=3, column=0)
mylabel3.grid(row=6, column=0)
mylabel4.grid(row=8, column=0)
mylabel4.grid(row=9, column=0)


#-------------------------------------------------------------------------------------------------------------------------

# creating dropdown minus
clicked_source = StringVar()
clicked_destination = StringVar()
clicked_algorithm = StringVar()
clicked_source.set("shebin")
clicked_destination.set("shebin")
clicked_algorithm.set("Breadth First")

option = [
#el menofia
'shebin', 'minuf', 'tala', 'birket as sab', 'el-bagour', 'ashmun', 'quwaysna', 'el sadat city', 'el shohada',
#el gharbia
'Kafr El-Zayat', 'basioun', 'tanta', 'qutur', 'El-Mahalla El-Kubra', 'As Santah', 'Samannoud', 'zefta',
#el kalubia
'banha', 'qalyub', 'Al Qanatir Al Khayriyyah', 'Shubra Al Khaymah', 'el khankah', 'kafr shokr', 'shibin el qanatir', 'toukh']


source = OptionMenu(root, clicked_source, *option)
destination = OptionMenu(root, clicked_destination,
                         *option)
algorithms = OptionMenu(root, clicked_algorithm,
                        "Breadth First", "Depth First", "A*", "Uniform cost")


# putting dropdown minus on screen
source.grid(row=1, column=4)
destination.grid(row=4, column=4)
algorithms.grid(row=7, column=4)

#--------------------------------------------------------------------------------------

# execution function

def execute():
    start = clicked_source.get()
    end = clicked_destination.get()
    method = clicked_algorithm.get()

    if (start=="shebin" and end=="shebin" and method=="Breadth First"):
        messagebox.showinfo('error! something is wrong',
                            "make sure source and destination don't equal each other ")

    else:
        print('--------------------------')
        print('source: ' + start)
        print('destination: ' + end)
        print('algorithm: ' + method)
        if (method == "Breadth First"):
            result_path = BreadthFirstSearch.BFS(start, end)
            print('path: ')
            print(result_path)
            map_functions.create_marks(result_path)
            map_functions.create_routes()
        elif (method == "Depth First"):
            result_path = DepthFirstSearch.DFS(start, end)
            print('path: ')
            print(result_path)
            map_functions.create_marks(result_path)
            map_functions.create_routes()

        elif (method=="A*"):
             huristic, cost, result_path = A_Star_Algorithm.a_star(start, end)
             print('path: ')
             print(result_path)
             #messagebox.showinfo('cost',
                                # "the cost is:  " + cost)
             map_functions.create_marks(result_path)
             map_functions.create_routes()
        else:
             cost, result_path = Uniform_Cost_Algorithm.ucs(start, end)

             print('path: ')
             print(result_path)
             map_functions.create_marks(result_path)
             map_functions.create_routes()
        root.quit()
#----------------------------------------------------------------------
# creating button
search = Button(root, text="Search", padx=40, command=execute)
exit_button = Button(root, text="Exit program", padx=40, command=root.quit)

# putting button on screen
search.grid(row=10, column=1, columnspan=2)
exit_button.grid(row=10, column=5, columnspan=2)
#---------------------------------------------------------------------

root.mainloop()
