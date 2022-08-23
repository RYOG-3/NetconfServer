from ncclient import manager
import xmltodict
import xml.dom.minidom


# ホスト名を変更するときの書き方
netconf_data = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>R1</hostname>
    </native>
</config>"""


with manager.connect(
        host="172.16.0.100",
        port="830",
        username="ryo",
        password="cisco",
        hostkey_verify=False
) as m:

    netconf_reply = m.edit_config(netconf_data, target="running")
