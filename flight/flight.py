import pandas as pd
import csv

class Flight:
    def __init__(self, folder = 'data'):
        self.folder = folder
        self.parameters = {} # 存储所有flight的参数信息
        self.flights = {} # 存储所有flight的飞行数据, key是文件名

    def set_folder(self, folder):
        self.folder = folder

    def read_para(self, filename = 'parameters.csv'):
        file_path = self.folder + '/' + filename
        # read file
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                flight_id = row['flight']
                self.parameters[flight_id] = {
                    'speed': row['speed'],
                    'payload': row['payload'],
                    'altitude': row['altitude'],
                    'date': row['date'],
                    'local_time': row['local_time'],
                    'route': row['route']
                }
        return self.parameters

    def read_flight(self, flight_number):
        file_path = self.folder + '/flights/' + str(flight_number) + '.csv'
        # init
        self.flights[flight_number] = {}
        # read file
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                for key in row.keys():
                    if key not in self.flights[flight_number]:
                        self.flights[flight_number][key] = []
                    self.flights[flight_number][key].append(row[key])
        return self.flights

    def read_all_flights(self):
        # init
        self.flights = {}
        # read all flights
        for flight_number in self.parameters.keys():
            self.read_flight(flight_number)
        return self.flights

if __name__ == '__main__':
    # init
    flights = Flight()
    flights.set_folder('D:\\Project\\DroneEnergyConsumption\\data')

    # read parameters
    flights.read_para()
    print(flights.parameters)

    # read flight 1
    flights.read_flight(1)
    # print(flights.flights)

    # read all flights
    # flights.read_all_flights()
    # print(flights.flights)