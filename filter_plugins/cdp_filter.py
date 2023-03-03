from ansible.plugins.filter.core import FilterModule
# get device information from show cdp neighbor cmd
class FilterModule(FilterModule):
    def filters(self):
        return {
            # In the class, define a method called filters() that returns a dictionary of filter names and the functions they map to.
           # 'my_filter': self.my_filter 
           'cdp_infor': self.cdp_infor
        }

    def my_filter(self, arg):
        return arg.upper()
    
    def test_out(self,data):
        value = []
        for i in data:
            i = i + '2'
            value.append(i)
        return value
    
    def cdp_infor(self, datas):
        ap_infor = {}
        for data in datas['cdp']:
            infor = datas['cdp'][data]
            for item in infor:
                interface = datas['cdp'][data][item]['local_interface']
                platform= datas['cdp'][data][item]['platform']
              #  vlan_infor = vlan_content['interfaces'][interface]['vlan']
                device_id = datas['cdp'][data][item]['device_id']
                if '9120' in platform or 'AIR' in platform:
                   # print( interface + ':  ' + 'platform: ' + platform + '  vlan ' + vlan_infor + '  deviceID: ' + device_id)
                   ap_infor[item] = {
                    'interface': interface,
                    'platform': platform,
                    'deviceID': device_id
                    }
                                    
        return ap_infor
