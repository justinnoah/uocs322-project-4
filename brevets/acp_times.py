"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

race_type = {
    200:  { 'hours': 13.5, 'speed': 15.0 },
    300:  { 'hours': 20.0, 'speed': 15.0 },
    400:  { 'hours': 27.0, 'speed': 15.0 },
    600:  { 'hours': 40.0, 'speed': 15.0 },
    1000: { 'hours': 75.0, 'speed': 13.3 },
    1200: { 'hours': 90.0, 'speed': 13.3 },
    1400: { 'hours': 116.40, 'speed': 12.0 },
    2200: { 'hours': 220.0, 'speed': 10.0 }
}

#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    return arrow.now()


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    return arrow.now()
