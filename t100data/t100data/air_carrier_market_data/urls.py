# urls.py
from django.urls import path
from . views import *      


urlpatterns = [
    path('list/', MarketDataList.as_view(), name="list"),
    path('top5paxorigin/', 
        Top5AirportsPaxByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Origin Airport"}
        ),
        name="top5paxorigin"),
    path('top5paxdestination/',  
        Top5AirportsPaxByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Destination Airport"}
        ), 
        name="top5paxdestination"),
    path('topdistance_month/',  
        TopDistanceByMonth.as_view(
            extra_context={'title': "Longest Distance by Month"}
        ), 
        name="topdistance_month"),
    path('top5paxfreightorigin/',
        Top5AirportsPaxByFreightOrigin.as_view(
            extra_context={'title': "Top Freight by Origin"}
        ),
        name="top5paxfreightorigin"),
    path('top5paxfreightdestination/',
        Top5AirportsPaxByFreightDestination.as_view(
            extra_context={'title': "Top Freight by Destination"}
        ),
        name="top5paxfreightdestination"),
    path('top5paxmailorigin/',
        Top5AirportsPaxByMailOrigin.as_view(
            extra_context={'title': "Top Mail by Origin"}
        ),
        name="top5paxmailorigin"),
    path('top5paxmaildestination/',
        Top5AirportsPaxByMailDestination.as_view(
            extra_context={'title': "Top Mail by Destination"}
        ),
        name="top5paxmaildestination"),
    path('top5paxdistanceorigin/',
        Top5AirportsPaxByDistanceOrigin.as_view(
            extra_context={'title': "Total Distance by Origin"}
        ),
        name="top5paxdistanceorigin"),        
    path('top5paxdistancedestination/',
        Top5AirportsPaxByDistanceDestination.as_view(
            extra_context={'title': "Total Distance by Destination"}
        ),
        name="top5paxdistancedestination"),
    path('top5paxpassengersbymonth/',
        TopPassengersByMonth.as_view(
            extra_context={'title': "Top Passengers by Month"}
        ),
        name="top5paxpassengersbymonth"),
    path('airlinetopfreight/',
        AirlineMostFreightCarried.as_view(
            extra_context={'title': "Airline with Top Freight"}
        ),
        name="airlinetopfreight"),        
    path('airlinetoppassengers/',
        AirlineMostPassengersCarried.as_view(
            extra_context={'title': "Airline with Top Passengers"}
        ),
        name="airlinetoppassengers"), 
    path('airlinetopmail/',
        AirlineMostMailCarried.as_view(
            extra_context={'title': "Airline with Top Passengers"}
        ),
        name="airlinetopmail"),
    path('airlinetopflightdistance/',
        AirlineMostFlightDistance.as_view(
            extra_context={'title': "Airline with Top Mail"}
        ),
        name="airlinetopflightdistance"),   
    path('airlineorderpassengers/',
        OrderPassengersByMonth.as_view(
            extra_context={'title': "Monthly Total Passengers by Airlines"}
        ),
        name="airlineorderpassengers"), 
    path('averagepassengerlax/',
        AveragePassengerLAX.as_view(
            extra_context={'title': " Passengers Ordered by Average Into LAX, SFO, DFW, ATL, ORD"}
        ),
        name="averagepassengerlax"), 
    path('averagefreightorigin/',
        AverageFreightDeparting.as_view(
            extra_context={'title': " Average Volume of Freight Departing From MIA, MEM, JFK, ANC, and SDF"}
        ),
        name="averagefreightorigin"),         
    path('citypairsmostfreight/',
        CityPairsMostFreight.as_view(
            extra_context={'title': "City Pairs with Most Freight By Longest Distance"}
        ),
        name="citypairsmostfreight"), 
    path('citypairsleastfreight/',
        CityPairsLeastFreight.as_view(
            extra_context={'title': "City Pairs with Least Freight By Longest Distance"}
        ),
        name="citypairsleastfreight"), 


]