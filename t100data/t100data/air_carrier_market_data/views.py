# Create your views here.
import pdb
from django.views.generic import ListView
from django.db.models import Max, Sum, Avg, Min

from . models import MarketData

class MarketDataList(ListView):
    model = MarketData

# What are the top 5 airports in terms of: Total passengers by origin
class Top5AirportsPaxByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_pax=Sum('passengers')) \
                        .order_by('-total_pax')[0:5]
    template_name="rankorder_list_origin.html"

# What are the top 5 airports in terms of: Total passengers by destination
class Top5AirportsPaxByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_pax=Sum('passengers')) \
                                 .order_by('-total_pax')[0:5]
    template_name="rankorder_list_destination.html"

#top 5 airports in terms of total freight by origin
class Top5AirportsPaxByFreightOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('orig_iata_code','orig_city_name').annotate(total_pax=Sum('freight')).order_by('-total_pax')[0:5]
    template_name="rankorder_list_freightorigin.html"


#top 5 airports in terms of total freight by destination
class Top5AirportsPaxByFreightDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name').annotate(total_pax=Sum('freight')).order_by('-total_pax')[0:5]
    template_name="rankorder_list_freightdestination.html"

#top 5 airports in terms of total mail by origin
class Top5AirportsPaxByMailOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('orig_iata_code','orig_city_name').annotate(total_pax=Sum('mail')).order_by('-total_pax')[0:5]
    template_name="rankorder_list_mailorigin.html"

#top 5 airports in terms of total mail by destination
class Top5AirportsPaxByMailDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name').annotate(total_pax=Sum('mail')).order_by('-total_pax')[0:5]
    template_name="rankorder_list_maildestination.html"

#top 5 airports in terms of total distance by origin
class Top5AirportsPaxByDistanceOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('orig_iata_code','orig_city_name').annotate(total_pax=Sum('distance')).order_by('-total_pax')[0:5]
    template_name="rankorder_list_distanceorigin.html"

#top 5 airports in terms of total distance by destination
class Top5AirportsPaxByDistanceDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name').annotate(total_pax=Sum('distance')).order_by('-total_pax')[0:5]
    template_name="rankorder_list_distancedestination.html"

# Which airport reported the most passengers by month?
class TopPassengersByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_passengers_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_passengers=Sum('passengers')) \
                .order_by('-total_passengers')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list
# Which airport reported the longest distance by month?
class TopDistanceByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_distance_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_distance=Max('distance')) \
                .order_by('-total_distance')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

        #which airline reported the most freight carried
class AirlineMostFreightCarried(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('carrier_name').annotate(total_pax=Sum('freight')).order_by('-total_pax')[0:1]
    template_name="airlinemostfreight.html"

        #which airline reported the most passengers carried
class AirlineMostPassengersCarried(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('carrier_name').annotate(total_pax=Sum('passengers')).order_by('-total_pax')[0:1]
    template_name="airlinemostpassengers.html"

        #which airline reported the most mail carried
class AirlineMostMailCarried(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('carrier_name').annotate(total_pax=Sum('mail')).order_by('-total_pax')[0:1]
    template_name="airlinemostmail.html"

        #which airline reported the longest flight distance
class AirlineMostFlightDistance(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('carrier_name').annotate(total_pax=Max('distance')).order_by('-total_pax')[0:1]
    template_name="airlinemostflightdistance.html"

#rank order passengers carried by month for airlines: AA(American Airlines), AS (Alaska Airlines), DL (Delta Airlines), UA (United Airlines), WN (Soutwest Airlines)

class OrderPassengersByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_passengers_by_month.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7) :

            queryset = MarketData.objects.values('carrier_id', 'carrier_name','month') \
            .filter(month__exact=month, carrier_id__in=['AA','AS','DL','UA','WN']) \
            .annotate(total_passengers=Sum('passengers')) \
            .order_by('-total_passengers')[0:5]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

        #average number of passengers for flight into LAX

class AveragePassengerLAX(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name').filter(dest_iata_code__in=['LAX','SFO','DFW','ATL','ORD']).annotate(total_pax=Avg('passengers')).order_by('-total_pax')[0:5]
    template_name="average_passenger_intolax.html"

class AverageFreightDeparting(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('orig_iata_code','orig_city_name').filter(orig_iata_code__in=['MIA','MEM','JFK','ANC','SDF']).annotate(total_pax=Avg('freight')).order_by('-total_pax')[0:5]
    template_name="average_freight_origin.html"

class CityPairsMostFreight(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('orig_city_name', 'dest_city_name','distance').annotate(max_freight=Max('freight')).order_by('-max_freight')[0:1]
    template_name="citypairsmostfreight.html"

class CityPairsLeastFreight(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('orig_city_name', 'dest_city_name','distance').annotate(max_mail=Max('mail')).order_by('-max_mail')[0:1]
    template_name="citypairsleastfreight.html"    