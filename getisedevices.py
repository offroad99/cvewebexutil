sys.path.append('/Users/gbekmezian/Documents/mycode/ise/ise')
sys.path.append('/Users/gbekmezian/Documents/mycode/ise')
from ise.cream import ERS
ise = ERS(ise_node='10.200.50.43', ers_user='george', ers_pass='Cve1915!', verify=False, disable_warnings=True)

ise.get_identity_groups()['response']

