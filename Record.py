import navio.util
import navio.ublox
from time import sleep
from drone_request import Request
import math

r = Request(email='samples@net.com', password='password')

latitude_file = open('latitude.data', 'r')
longitude_file = open('longitude.data', 'r')

latitude_data = latitude_file.read()[:-1]
longitude_data = longitude_file.read()[:-1]

lat = latitude_data.split(',')
long = longitude_data.split(',')

distance = 111 * math.sqrt((float(long[0]) - float(long[-1])) ** 2 + (float(lat[0]) - float(lat[-1])) ** 2)

r.save_flight(distance=distance, name='My Flight', longitude=longitude_data, latitude=latitude_data, rating=2)

latitude_file = open('latitude.data', 'r')
longitude_file = open('longitude.data', 'r')

latitude_file.read()

ubl = navio.ublox.UBlox("spi:0.0", baudrate=5000000, timeout=2)

ubl.configure_poll_port()
ubl.configure_poll(navio.ublox.CLASS_CFG, navio.ublox.MSG_CFG_USB)

ubl.configure_port(port=navio.ublox.PORT_SERIAL1, inMask=1, outMask=0)
ubl.configure_port(port=navio.ublox.PORT_USB, inMask=1, outMask=1)
ubl.configure_port(port=navio.ublox.PORT_SERIAL2, inMask=1, outMask=0)
ubl.configure_poll_port()
ubl.configure_poll_port(navio.ublox.PORT_SERIAL1)
ubl.configure_poll_port(navio.ublox.PORT_SERIAL2)
ubl.configure_poll_port(navio.ublox.PORT_USB)
ubl.configure_solution_rate(rate_ms=1000)

ubl.set_preferred_dynamic_model(None)
ubl.set_preferred_usePPP(None)

ubl.configure_message_rate(navio.ublox.CLASS_NAV, navio.ublox.MSG_NAV_POSLLH, 1)
ubl.configure_message_rate(navio.ublox.CLASS_NAV, navio.ublox.MSG_NAV_PVT, 1)
ubl.configure_message_rate(navio.ublox.CLASS_NAV, navio.ublox.MSG_NAV_STATUS, 1)
ubl.configure_message_rate(navio.ublox.CLASS_NAV, navio.ublox.MSG_NAV_SOL, 1)
ubl.configure_message_rate(navio.ublox.CLASS_NAV, navio.ublox.MSG_NAV_VELNED, 1)
ubl.configure_message_rate(navio.ublox.CLASS_NAV, navio.ublox.MSG_NAV_SVINFO, 1)
ubl.configure_message_rate(navio.ublox.CLASS_NAV, navio.ublox.MSG_NAV_VELECEF, 1)
ubl.configure_message_rate(navio.ublox.CLASS_NAV, navio.ublox.MSG_NAV_POSECEF, 1)
ubl.configure_message_rate(navio.ublox.CLASS_RXM, navio.ublox.MSG_RXM_RAW, 1)
ubl.configure_message_rate(navio.ublox.CLASS_RXM, navio.ublox.MSG_RXM_SFRB, 1)
ubl.configure_message_rate(navio.ublox.CLASS_RXM, navio.ublox.MSG_RXM_SVSI, 1)
ubl.configure_message_rate(navio.ublox.CLASS_RXM, navio.ublox.MSG_RXM_ALM, 1)
ubl.configure_message_rate(navio.ublox.CLASS_RXM, navio.ublox.MSG_RXM_EPH, 1)
ubl.configure_message_rate(navio.ublox.CLASS_NAV, navio.ublox.MSG_NAV_TIMEGPS, 5)
ubl.configure_message_rate(navio.ublox.CLASS_NAV, navio.ublox.MSG_NAV_CLOCK, 5)


if __name__ == "__main__":
    new_latitude_file = open('latitude.data', 'w+')
    new_longitude_file = open('longitude.data', 'w+')

    while True:
        msg = ubl.receive_message()
        if msg.name() == "NAV_POSLLH":
            outstr = str(msg).split(",")[1:]
            new_latitude = float(outstr[0].split("=")[1]) / 10000000
            new_longitude = float(outstr[1].split("=")[1]) / 10000000
            new_latitude_file.write(str(new_latitude) + ',')
            new_longitude_file.write(str(new_longitude) + ',')