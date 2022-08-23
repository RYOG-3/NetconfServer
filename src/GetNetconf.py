from ncclient import manager
import xmltodict
import xml.dom.minidom


# Create an XML filter for targeted NETCONF queries
netconf_filter = """
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface></interface>
    </interfaces>
</filter>"""

# hostname 抽出
netconf_filter2 = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname></hostname>
    </native>
</filter>"""


with manager.connect(
        host="172.16.0.100",
        port="830",
        username="ryo",
        password="cisco",
        hostkey_verify=False
) as m:

    netconf_reply = m.get_config(source='running', filter=netconf_filter2)
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())


# Parse the returned XML to an Ordered Dictionary
netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]


# Create a list of interfaces
interfaces = netconf_data["interfaces"]["interface"]


for interface in interfaces:
    print("Interface {} enabled status is {}".format(
        interface["name"],
        interface["enabled"]
    )
    )
