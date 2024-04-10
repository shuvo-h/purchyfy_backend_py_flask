from functools import wraps
import traceback

def catch_err_handler(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        try:
            pass
        except Exception as e:
            # Log or print the exception and its traceback
            print(str(e))
            # traceback.print_exc() # use this in development to print files where the error occured
            raise e
    return wrapper