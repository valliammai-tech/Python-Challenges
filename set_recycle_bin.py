import random
import logging

logging.basicConfig(filename='set.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class ElementNotExists(Exception):
    pass
class set_recycle:
    def __init__(self, set_items):
        self.set_item=set_items
        logging.info("set provided by user for recycle process is: {}".format(self.set_item))
    def set_remove(self, element):
        '''
        The discard() method removes the specified item from the set.
        This method is different from the remove() method, because the remove() method will 
        raise an error if the specified item does not exist, and the discard() method will not.
        '''
        l=[]
        try:
            if element not in self.set_item:
                raise ElementNotExists
            for i in self.set_item:
                if i != element:
                    l.append(i)
        except ElementNotExists:
            logging.error("Raised user defined exception for set remove method as element {} to be removed from set does not exists".format(element))
        except Exception as e:
            logging.error(e)
        else:
            logging.debug("after element {} removed from set {} is {}".format(element, self.set_item, set(l)))
        return set(l)
    def set_discard(self,element):
        l=[]
        try:
            for i in self.set_item:
                if i != element:
                    l.append(i)
        except Exception as e:
            logging.error(e)
        else:
            logging.debug("after element {} discard from set {} is {}".format(element, self.set_item, set(l)))
        return set(l)
    def set_pop(self):
        '''
        The pop() method removes a random item from the set.
        '''
        to_list=list(self.set_item)
        random.shuffle(to_list)
        logging.info("set pop method shuffles the set items and after pop: {}".format(set(to_list[:-1])))
        return set(to_list[:-1])
            
        
    
            