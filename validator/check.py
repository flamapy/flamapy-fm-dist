from flamapy.core.discover import DiscoverMetamodels 

def model_checker(model):
    dm = DiscoverMetamodels() 
    try: 
        result = dm.use_operation_from_file('Valid', model)
    except:
        return False
    return result

def product_checker():
    return 'API operation for checking product'