from .order_model import OrderModel, ORDER_STATUS
from src.modules.contact.v1.contact_model import ContactModel
from src.config.db_config import db
from src.errorHandlers.appErrorhandler import AppError
from src.utils.sendResFormater import sendRes

def create_order(payload):
    shop_id = payload.get('shop_id')
    total_price = payload.get('total_price')
    order_items = payload.get('order_items')
    contact = payload.get("contact")
    status = ORDER_STATUS.get("PENDING")

    
    # create order with contact id 
    try:
        contactInfo = None
        # Start a transaction
        with db.session.begin():
            # if contact exist update, else add
            contactInfo = ContactModel.query.filter_by(phone=contact['phone']).first()
            
            if contactInfo:
                contactInfo.name = contact['name']
            else:
                contactInfo = ContactModel(name=contact['name'],phone=contact['phone'])
                ContactModel.add_only(contactInfo)
                
            # check if this contact already has an active order for this shop
            existPendingOrder = OrderModel.query.filter_by(status=status,contact_id=contactInfo.id,shop_id=shop_id).first()
            
            if existPendingOrder:
                raise AppError(422,"Order already exist")
            else:
                new_order = OrderModel(
                    contact_id = contactInfo.id,
                    order_items= order_items,
                    shop_id=shop_id,
                    status=status,
                    total_price=total_price
                )
                OrderModel.add_only(new_order)
                # Return the order inside the context manager

            # finally commit inside session.begin() and return from outside this scope
            OrderModel.commit_only()
        
        return sendRes(
            201,
            data={
                "order": new_order.to_dict(),
                "contact": contactInfo.to_dict()
            },
            message="Order created successfully"
        )
    except Exception as e:
        db.session.rollback()
        raise AppError(500,  str(e))