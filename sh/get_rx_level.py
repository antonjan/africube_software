# default = -24000
import xmlrpc.client
#fun_proibe_rx_level
#rx_level
with xmlrpc.client.ServerProxy("http://127.0.0.1:8008/") as proxy:
#    print("Get SDRPLAY rx rf level: %s" % str(proxy.get_rx_level()))
     print("rx level %s " % (proxy.get_rx_level()))
#     rxl = complex(proxy.get_rx_level())
#     print("rxl=",rxli.real)
#     print("get SDR RX RF level: ", (proxy.get_rx_level()))
#    print("100 is even: %s" % str(proxy.is_even(100)))

