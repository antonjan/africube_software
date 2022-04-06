import xmlrpc.client

with xmlrpc.client.ServerProxy("http://127.0.0.1:8008/") as proxy:
    print("Set SDRPLAY rx Gain: %s" % str(proxy.set_Beacom_overall_gain(9)))
#    print("100 is even: %s" % str(proxy.is_even(100)))
