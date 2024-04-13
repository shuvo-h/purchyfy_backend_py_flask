

def create_order(payload):
    catalogue_id = payload.get('catalogue_id')
    catalogue_id = payload.get('catalogue_id')
    price = payload.get('price')
    quantity = payload.get('quantity')
    total_price = payload.get('total_price')
    status = "pending"

    
    # check catalogue exit
    # check if this contact already has an active order for this shop
    # price from db and to total price same
    # upsert contact table with phone unique
    # pending order quantity + current order quantity doest exceed inventory
    # create order with contact id 
