import networkx as nx

from metro.models import Station, TransferTime, TimeBetweenStations


def get_data_from_database():
    stations = Station.objects.all().values("id_station", "name_station", "name_line")
    transfers = TransferTime.objects.all().values("id1", "id2", "time")
    travel_times = TimeBetweenStations.objects.all().values("id_st1", "id_st2", "time")

    return list(stations), list(transfers), list(travel_times)


stations, transfers, travel_times = get_data_from_database()

G = nx.Graph()

# Добавление станций как узлов
for station in stations:
    G.add_node(station["id_station"], label=station["name_station"], line=station["name_line"])

# Добавление ребер между последовательными станциями на одной линии
for i in range(len(stations) - 1):

    if stations[i]["name_line"] == stations[i + 1]["name_line"]:
        G.add_edge(stations[i]["id_station"], stations[i + 1]["id_station"])

# Добавление пересадочных соединений с учетом времени пересадки
for transfer in transfers:
    if transfer["id1"] in G.nodes() and transfer["id2"] in G.nodes():
        G.add_edge(transfer["id1"], transfer["id2"], weight=int(transfer["time"]))

# Добавление времени движения поездов между станциями как веса ребер
for connection in travel_times:
    id_st1 = connection["id_st1"]
    id_st2 = connection["id_st2"]
    time = float(connection["time"])
    if G.has_edge(id_st1, id_st2):
        G[id_st1][id_st2]['weight'] = time
    else:
        G.add_edge(id_st1, id_st2, weight=time)


# Функция получения пути с пересадками и временем
def get_paths_with_details(paths):
    paths_with_details = []
    for path in paths:
        path_details = {
            "stations": [G.nodes[station]['label'] for station in path],
            "time": sum(G[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1)),
            "transfers": []
        }

        # Определение пересадки
        for i in range(len(path) - 1):
            if not G.has_edge(path[i], path[i + 1]):
                continue
            edge_data = G[path[i]][path[i + 1]]
            if 'weight' in edge_data and edge_data['weight'] > 0:
                if G.nodes[path[i]]['line'] != G.nodes[path[i + 1]]['line']:
                    path_details["transfers"].append({
                        "station": G.nodes[path[i + 1]]['label'],
                        "time": edge_data['weight']
                    })
        paths_with_details.append(path_details)

    return paths_with_details


def get_shortest_path(start_id, end_id):
    # Проверка, что оба идентификатора присутствуют в графе
    if start_id in G.nodes() and end_id in G.nodes():

        # Поиск всех кратчайших путей по времени (весу)
        all_shortest_paths = list(nx.all_shortest_paths(G, source=start_id, target=end_id, weight='weight'))

        if not all_shortest_paths:
            print(f"Маршрутов между станциями {start_id} и {end_id} не найдено")
        else:
            print(f"Кратчайший маршрут от станции {start_id} до станции {end_id}")

            # Вывод всех кратчайших путей с деталями
            paths_with_details = get_paths_with_details(all_shortest_paths)
            for path_details in paths_with_details:

                path = path_details

                return path
    else:
        print("Одна или обе станции отсутствуют в графе!")
