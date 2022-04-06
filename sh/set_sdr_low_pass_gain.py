import xmlrpc.client

with xmlrpc.client.ServerProxy("http://127.0.0.1:8008/") as proxy:
    print("set_low psdd filter gain: %s" % str(proxy.set_low_pass_filter_gain(1)))
#    print("100 is even: %s" % str(proxy.is_even(100)))
