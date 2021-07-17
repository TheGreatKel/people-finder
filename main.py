import sys
import webbrowser

'''TODO:
Figure out aparments
'''
if sys.argv[1].isdigit():
    #parse address
    h_number = sys.argv[1]
    street = sys.argv[2]
    street_type = sys.argv[3]

    if len(sys.argv)>4:
        town = sys.argv[4]
    else:
        town = "Bronx"

    # if ("Apt" in sys.argv) or ("apt" in sys.argv):
    #     apt = sys.argv[]

    fast_address = f"https://www.fastpeoplesearch.com/address/{h_number}-{street}-{street_type}_{town}-ny"
    true_address = f"https://www.truepeoplesearch.com/resultaddress?streetaddress={h_number}%20{street}%20{street_type}&citystatezip={town},%20NY"
    four_address = f"https://www.411.com/address/{h_number}-{street}-{street_type}/{town}-NY"
    gmaps = f"https://www.google.com/maps/place/{h_number}+{street}+{street_type},+{town},+NY"
    
    webbrowser.open(fast_address)
    webbrowser.open(true_address)
    webbrowser.open(four_address)
    webbrowser.open(gmaps)
else:
    first_name = sys.argv[1]
    last_name = sys.argv[2]
    if len(sys.argv)>3:
        town = sys.argv[3]
    else:
        town = "Bronx"
    fast_p = f"https://www.fastpeoplesearch.com/name/{first_name}-{last_name}_{town}-ny"
    true_p = f"https://www.truepeoplesearch.com/results?name={first_name}%20{last_name}&citystatezip={town},%20NY"
    four_p = f"https://www.411.com/name/{first_name}-{last_name}/{town}-NY"
    
    webbrowser.open(four_p)
    webbrowser.open(fast_p)
    webbrowser.open(true_p)
        
   