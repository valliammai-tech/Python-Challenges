import logging
logging.basicConfig(filename='set.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class copy_clear_set:
    # here init method is not defined for set_items as clear will impact copying if set_items defined common in init method
    def copy_set(*args):
        logging.info('set for copying: {}'.format(args))
        new_set=args
        return "old set is {} and copied new set is {}".format(args, new_set)
    def clear_set(*args):
        logging.info('set to be cleared is: {}'.format(args))
        args={}
        return args