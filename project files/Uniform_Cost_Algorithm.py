GRAPH= {'shebin': {'tala': 18, 'el shohada': 16.5,'minuf':16.4,'el-bagour':14.6,'quwaysna':18.7,'birket as sab': 14},
               'minuf': {'el shohada':18.2, 'shebin': 16.1,'el-bagour':11.4,'ashmun':27,'el sadat city':55.9},
               'tala': {'birket as sab':18.1,'shebin': 18,'el shohada':14.4,'Kafr El-Zayat':25.6,'tanta':15.3,'As Santah':29.2},
               'birket as sab': {'tala':18.1, 'shebin': 14,'quwaysna':13.3,'As Santah':16,'zefta':24.5},
               'el-bagour': {'quwaysna':29.8, 'shebin':14.9,'minuf':11.5,'ashmun':22.5,'banha':26.6,'toukh':39.7,'Al Qanatir Al Khayriyyah':30.8},
               'ashmun': {'el-bagour':23.8, 'minuf':27.1,'el sadat city':61.7,'Al Qanatir Al Khayriyyah':23.5,'toukh':56.3},
               'quwaysna': {'birket as sab':13.9,'shebin':18.1,'el-bagour':18.1,'zefta':21.1,'kafr shokr':26.8,'banha':15.1},
               'el sadat city': {'ashmun':73.8,'minuf':54.5},
               'el shohada': {'tala':14.4,'shebin':17.5,'minuf':18.2},
               'Kafr El-Zayat':{'basioun':20.2,'tanta':27.6,'tala':25.6},
               'basioun':{'qutur':16.8,'tanta':28.8,'Kafr El-Zayat':20.2},
               'qutur':{'basioun':17.1,'tanta':16.3,'El-Mahalla El-Kubra':28.8},
               'El-Mahalla El-Kubra':{'qutur':30.8,'tanta':31.5,'As Santah':30.8,'zefta':33.3,'Samannoud':7.7},
               'Samannoud':{'El-Mahalla El-Kubra':7.8,'As Santah':46.6,'zefta':33.1},
               'zefta':{'Samannoud':35,'El-Mahalla El-Kubra':32.7,'As Santah':17.9,'quwaysna':21.1,'birket as sab':25.3,'kafr shokr':27.9},
               'As Santah':{'Samannoud':48.7,'El-Mahalla El-Kubra':30.3,'birket as sab':16.2,'tanta':25.3},
               'tanta':{'tala':15,'Kafr El-Zayat':26.4,'basioun':28.3,'qutur':16,'El-Mahalla El-Kubra':29.2,'As Santah':25.9},
               'kafr shokr':{'zefta':32.7,'quwaysna':23.1,'banha':13.4},
               'banha':{'kafr shokr':17.7,'quwaysna':17.8,'el-bagour':29.4,'toukh':15.6,'shibin el qanatir':28.8},
               'toukh':{'banha':17.5,'el-bagour':40,'ashmun':57.5,'Al Qanatir Al Khayriyyah':25,'qalyub':22,'shibin el qanatir':14},
               'Al Qanatir Al Khayriyyah':{'toukh':24.7,'ashmun':23.5,'Shubra Al Khaymah':18.5,'qalyub':7.6},
               'Shubra Al Khaymah':{'Al Qanatir Al Khayriyyah':18.4,'qalyub':11.6,'el khankah':22.4},
               'qalyub':{'el khankah':26.9,'shibin el qanatir':20.6,'toukh':22.7,'Al Qanatir Al Khayriyyah':7.6,'Shubra Al Khaymah':12.1},
               'shibin el qanatir':{'banha':29.8,'toukh':14,'qalyub':20.4,'el khankah':17.6},
               'el khankah':{'shibin el qanatir':15.9,'qalyub':27.4,'Shubra Al Khaymah': 24.4},
               }

#--------------------------------------------------------------------------------------------------------

def ucs(source, destination):
    """Cheapest path from source to destination using uniform cost search

    :param source: Source city name
    :param destination: Destination city name
    :returns: Cost and path for cheapest traversal

    """
    from queue import PriorityQueue
    priority_queue, visited = PriorityQueue(), {}
    priority_queue.put((0, source, [source]))
    visited[source] = 0
    while not priority_queue.empty():
        (cost, vertex, path) = priority_queue.get()
        if vertex == destination:
            return cost, path
        for next_node in GRAPH[vertex].keys():
            current_cost = cost + GRAPH[vertex][next_node]
            if not next_node in visited or visited[next_node] >= current_cost:
                visited[next_node] = current_cost
                priority_queue.put((current_cost, next_node, path + [next_node]))
