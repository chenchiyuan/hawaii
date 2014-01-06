# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from bs4 import BeautifulSoup
from django.template.loader import render_to_string
from django.conf import settings
from hawaii.apps.base.models import City, Company
import requests
import datetime
import xmltodict


class Route(object):
    def __init__(self, company_three, starting, destination, price, tax, limit_no, data, turn=0, flights=[]):
        self.company_three = company_three
        self.company = Company.get_name_by_code(company_three)
        self.starting = starting
        self.destination = destination
        self.departure = flights[0].departure
        self.arrival = flights[-1].arrival
        self.price = price
        self.tax = tax
        self.flights = flights
        self.turn = turn
        self.limit_no = limit_no
        self.limits = []
        self.data = data

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
        content = requests.get(url).content
        return cls.parse_xml(content)

    def to_json(self):
        turn = self.turn
        if not int(turn):
            turn = u"直飞"
        else:
            turn = unicode(turn)
        return {
            "company": self.company,
            "company_three": self.company_three,
            "turn": turn,
            "starting": self.starting,
            "destination": self.destination,
            "departure": self.departure,
            "arrival": self.arrival,
            "price": self.price,
            "tax": self.tax,
            "flights": map(lambda flight: flight.to_json(), self.flights),
            "limit_no": self.limit_no,
            "data": self.data
        }

    @classmethod
    def parse_xml(cls, content):
        soup = BeautifulSoup(content)
        datas = xmltodict.parse(content)

        routes = soup.find_all("r")
        result_routes = []
        for index, route in enumerate(routes):
            route_segments = route.find_all("s")
            price = route.find("pm").text
            tax = route.find("x").text
            route_starting = City.get_name_by_code(route.find("f").text)
            route_destination = City.get_name_by_code(route.find("t").text)
            route_company_three = route.find("a").text
            route_limit = route.find("l").text


            route_turn_tag = route.find("zz")
            if not route_turn_tag:
                route_turn = 0
            else:
                route_turn = route_turn_tag.text[0]

            flights = []
            for route_segment in route_segments:
                number = route_segment.find("no")
                from_city = City.get_name_by_code(route_segment.find("f").text)
                to_city = City.get_name_by_code(route_segment.find("t").text)
                company = route_segment.find("a").text
                departure_date = route_segment.find("fd").text
                departure_time = route_segment.find("ft").text
                arrival_date = route_segment.find("td")
                if not arrival_date:
                    arrival_date = departure_date
                else:
                    arrival_date = arrival_date.text

                arrival_time = route_segment.find("tt").text
                seat_type = route_segment.find("st").text
                flight_price = route_segment.find("m")
                duration = route_segment.find("d").text
                modal = route_segment.find("et").text
                status = int(route_segment.find("dp").text)

                flight_data = {
                    "number": number.text,
                    "staring": from_city,
                    "destination": to_city,
                    "company": Company.get_name_by_code(company),
                    "departure": "%s %s:%s" % (departure_date, departure_time[:2], departure_time[2:]),
                    "arrival": "%s %s:%s" % (arrival_date, arrival_time[:2], arrival_time[2:]),
                    "duration": duration,
                    "modal": modal,
                    "status": status,
                    "seat_type": seat_type
                }
                flight = Flight(**flight_data)
                flights.append(flight)

            route = Route(route_company_three, route_starting,
                          route_destination, price=price, data=datas['RS']['R'][index],
                          tax=tax, flights=flights, turn=route_turn, limit_no=route_limit)
            result_routes.append(route)

        return result_routes

    @classmethod
    def get_limits(cls, limit_no):
        url = "http://intf.fare2go.com/limit.php?p=%s" % limit_no
        try:
            content = requests.get(url).content
            soup = BeautifulSoup(content, from_encoding="utf-8")
            limits = soup.find_all("limit")
            final_limits = []
            for limit in limits:
                limit_type = limit.find('type').text
                content = limit.find('content').text
                final_limits.append({"limit_type": limit_type, "content": content})
            return final_limits
        except:
            return []


class Flight(object):
    def __init__(self, number, staring, destination, company, departure, arrival, duration, modal, seat_type="Y",
                 status=1, amount=1, **kwargs):
        self.number = number
        self.starting = staring
        self.destination = destination
        self.company = company
        self.departure = datetime.datetime.strptime(departure, "%Y-%m-%d %H:%M").strftime("%Y-%m-%dT%H:%M:%S")
        self.arrival = datetime.datetime.strptime(arrival, "%Y-%m-%d %H:%M").strftime("%Y-%m-%dT%H:%M:%S")
        self.duration = duration
        self.amount = amount
        self.modal = modal
        self.status = status
        self.seat_type = seat_type

    def to_json(self):
        return {
            "number": self.number,
            "starting": self.starting,
            "destination": self.destination,
            "company": self.company,
            "departure": self.departure,
            "arrival": self.arrival,
            "amount": self.amount,
            "duration": self.duration,
            "modal": self.modal,
            "status": self.status,
            "seat_type": self.seat_type
        }

    @classmethod
    def format_datetime(cls, string):
        return datetime.datetime.strptime(string, "%Y-%m-%dT%H:%M:%S")

    @classmethod
    def get_type(cls, seat_type):
        mapping = {
            "Y": u"经济舱",
            "C": u"商务舱",
            "F": u"头等舱"
        }
        return mapping.get(seat_type, u"经济舱")


class PNR(object):
    @classmethod
    def gen_by_route(cls, route, passengers=[]):
        pnr_url = "http://221.122.114.153/UniFare/Fare2goHttpService.dll/TestMakePNR"
        xml = render_to_string("pnr.html", {
            "route": route,
            "passengers": passengers
        })
        r = requests.post(pnr_url, data=xml)
        data = r.content
        json_data = xmltodict.parse(data)
        return json_data[u'PNRStatus']['PNR']