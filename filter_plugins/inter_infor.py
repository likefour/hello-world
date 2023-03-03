from ansible.plugins.filter.core import FilterModule
# filter vlan information from show inter status cmd output
class FilterModule(FilterModule):
    def filters(self):
        return {
            # In the class, define a method called filters() that returns a dictionary of filter names and the functions they map to.
           # 'my_filter': self.my_filter 
           'inter_infor': self.inter_infor
        }

    def inter_infor(self, datas):
        inter_for = {}
        for interface in datas['interfaces']:
            vlan_for = datas['interfaces'][interface]['vlan']
            inter_for[interface] = {
                'vlan': vlan_for
            }
        inter_for = {
            'interface': inter_for
        }
              
        return inter_for
