# default = -24000
import xmlrpc.client

with xmlrpc.client.ServerProxy("http://127.0.0.1:8008/") as proxy:
    print("Set SDRPLAY rx Gain: %s" % str(proxy.set_beacon_offset_freq(-24800)))
#    print("100 is even: %s" % str(proxy.is_even(100)))

