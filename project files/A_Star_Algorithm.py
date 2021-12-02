import math

#----------------------------------------------------------------------------------------------------------------

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


Coordinates = {
#el menofia
"shebin":[30.554928799816988, 31.012393143088957],
"minuf":[30.45841991481536, 30.933867041463532],
"tala":[30.683127111837056, 30.950034191578247],
"birket as sab": [30.627495984801378, 31.07244250380298],
"el-bagour":[30.43186671298956, 31.031983255977398],
"ashmun":[30.300117313578117, 30.97564036423758],
"quwaysna":[30.56765698894867, 31.149568418149613],
"el sadat city":[30.362811748009076, 30.533153025293895],
"el shohada": [30.59768043193886, 30.895758793318098],
#el gharbia
"Kafr El-Zayat":[30.828935887979828, 30.81468363315086],
"basioun":[30.941234859668185, 30.819787152459256],
"tanta":[30.78236661466976, 31.003931835360497],
"qutur":[30.97124133198592, 30.952896608684792],
"El-Mahalla El-Kubra":[30.969841036674914, 31.166019730570685],
"As Santah":[30.749281457375343, 31.129532111290036],
"Samannoud":[30.96202482138702, 31.241725792395766],
"zefta":[30.714483753839744, 31.240197668420624],
#el kalubia
"banha":[30.46954041758182, 31.18372798445176],
"qalyub":[30.180143566835696, 31.20638419614639],
"Al Qanatir Al Khayriyyah":[30.194609758641715, 31.13391214967144],
"Shubra Al Khaymah":[30.124142365522676, 31.260465002556664],
"el khankah":[30.22039965655326, 31.368612270866304],
"kafr shokr":[30.552839823187284, 31.255430468410704],
"shibin el qanatir":[30.31214792794175, 31.32292278281032],
"toukh":[30.353756127836252, 31.2014138527108]
}


#--------------------------------------------------------------------------------------------------

def straightLineDistance(cityOne, cityTwo):
    """
    the straight line between two cites to be the heuristic function
    :param cityOne: city number one
    :param cityTwo: city number two
    :return: the distance between cityOne and cityTwo
    """
    R = 6373.0  # radius of the earth
    lat1 = math.radians(cityOne[0])
    lat2 = math.radians(cityTwo[0])
    long1 = math.radians(cityOne[1])
    long2 = math.radians(cityTwo[1])
    distanceLat = lat2 - lat1
    distanceLong = long2 - long1
    a = math.sin(distanceLat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(distanceLong / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


def a_star(source, destination):
    """Optimal path from source to destination using straight line distance heuristic

    :param source: Source city name
    :param destination: Destination city name
    :returns: Heuristic value, cost and path for optimal traversal

    """
    # HERE THE STRAIGHT LINE DISTANCE VALUES ARE IN REFERENCE TO BUCHAREST AS THE DESTINATION
    straight_line = {}
    for i in Coordinates.keys():
        straight_line[i] = straightLineDistance(Coordinates[i], Coordinates[destination])

    from queue import PriorityQueue
    priority_queue, visited = PriorityQueue(), {}
    priority_queue.put((straight_line[source], 0, source, [source]))
    visited[source] = straight_line[source]
    while not priority_queue.empty():
        (heuristic, cost, vertex, path) = priority_queue.get()
        if vertex == destination:
            return heuristic, cost, path
        for next_node in GRAPH[vertex].keys():
            current_cost = cost + GRAPH[vertex][next_node]
            heuristic = current_cost + straight_line[next_node]
            if not next_node in visited or visited[next_node] >= heuristic:
                visited[next_node] = heuristic
                priority_queue.put((heuristic, current_cost, next_node, path + [next_node]))
