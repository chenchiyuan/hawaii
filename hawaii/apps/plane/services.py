# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from bs4 import BeautifulSoup
import requests
from django.conf import settings


class Company(object):
    def __init__(self):
        file_handler = open(settings.PROJECT_HOME + "company.csv", "r")
        lines = file_handler.readlines()
        file_handler.close()
        self.companies = {

        }

        for line in lines:
            name, three = line.split("\t")
            self.companies[three.strip()] = name

    def get_name(self, three):
        return self.companies.get(three, "")


class Route(object):
    def __init__(self, price, tax, flights=[]):
        self.price = price
        self.tax = tax
        self.flights = flights

    @classmethod
    def search(cls, starting, destination, departure, back_time="", seat_type="Y", **kwargs):
        base_url = "http://intf.fare2go.com/tukeq.php"
        params = {
            "fromCity": starting,
            "toCity": destination,
            "fromDate": departure,
            "seatType": seat_type
        }
        if back_time:
            params['returnDate'] = back_time

        url = base_url + "?" + "&".join(map(lambda item: "%s=%s" % (item[0], item[1]), params.items()))
        print(url)
        content = requests.get(url).content
        return cls.parse_xml(content)

    def to_json(self):
        return {
            "price": self.price,
            "tax": self.tax,
            "flights": map(lambda flight: flight.to_json(), self.flights)
        }

    @classmethod
    def parse_xml(cls, content):
        soup = BeautifulSoup(content)
        routes = soup.find_all("r")
        result_routes = []
        for route in routes:
            route_segments = route.find_all("s")
            price = route.find("pm").text
            tax = route.find("x").text
            flights = []
            for route_segment in route_segments:
                number = route_segment.find("no")
                from_city_3 = route_segment.find("f")
                to_city_3 = route_segment.find("t")
                company_3 = route_segment.find("a")
                departure_date = route_segment.find("fd")
                departure_time = route_segment.find("ft")
                arrival_date = route_segment.find("td")
                arrival_time = route_segment.find("tt")
                seat_type = route_segment.find("st")
                flight_price = route_segment.find("m")

                flight_data = {
                    "number": number.text,
                    "staring": from_city_3.text,
                    "destination": to_city_3.text,
                    "company": company_3.text,
                    "departure": departure_time.text,
                    "arrival": arrival_time.text,
                }
                flight = Flight(**flight_data)
                flights.append(flight)
            route = Route(price=price, tax=tax, flights=flights)
            result_routes.append(route)

        return result_routes


class Flight(object):
    def __init__(self, number, staring, destination, company, departure, arrival, amount=1):
        self.number = number
        self.starting = staring
        self.destination = destination
        self.company = company
        self.departure = departure
        self.arrival = arrival
        self.amount = amount

    def to_json(self):
        return {
            "number": self.number,
            "starting": self.starting,
            "destination": self.destination,
            "company": self.company,
            "departure": self.departure,
            "arrival": self.arrival,
            "amount": self.amount
        }


def test():
    return Route.search(starting="PEK", destination="FRA", departure="2013-12-29")