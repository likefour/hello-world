from ansible.plugins.filter.core import FilterModule
# combile cdp informaiton and vlan information together 
class FilterModule(FilterModule):
    def filters(self):
        return {
            # In the class, define a method called filters() that returns a dictionary of filter names and the functions they map to.
           # 'my_filter': self.my_filter 
           'cdp_inter_info': self.cdp_inter_info
        }

    def cdp_inter_info(self, datas):
        output = []
        for item in datas:
            if 'interface' != item:
                interface = datas[item]['interface']
                plarform = datas[item]['platform']
                deviceID = datas[item]['deviceID']
                vlan_for = datas['interface'][interface]['vlan']
                output.append([interface, plarform, deviceID, vlan_for])
                   
        return output
