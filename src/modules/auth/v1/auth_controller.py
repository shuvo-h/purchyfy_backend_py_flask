from . import auth_service
from src.utils import catchErrorHandler, sendResFormater

# regerster a user 
@catchErrorHandler.catch_err_handler
def register_userCtl(body):
    result = auth_service.registerUserIntoDb(body)
    # return sendResFormater.sendRes(201,result,None,"User created succesfully",True)
    return result


# login a user 
@catchErrorHandler.catch_err_handler
def login_userCtl(body):
    result = auth_service.loginUserFromDb(body)
    # return sendResFormater.sendRes(201,result,None,"User created succesfully",True)
    return result