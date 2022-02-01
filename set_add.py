import logging

logging.basicConfig(filename='set.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
class MultipleElement(Exception):
    pass
class ElementAlreadyExists(Exception):
    pass

class add_set_element:
    def __init__(self,set_items):
        self.set_items=set_items
        logging.info("set_items provided by user: {}".format(self.set_items))
    def add_element(self,element):
        ele=element
        logging.info("Element to be passed is: {}".format(element))
        try:
            if len(ele.split(',')) > 1:
                raise MultipleElement
            if element in self.set_items:
                raise ElementAlreadyExists
            self.set_items=set(list(self.set_items)+[element])
        except MultipleElement:
            logging.error("set add method will not accept multiple elements {}".format(element))
        except ElementAlreadyExists:
            logging.error("set add method will not add this element as it is already existing in the list {}".format(element))
        except Exception as e:
            logging.error(e)
        else:
            logging.info("Element {} Added to {}".format(element,self.set_items))
        finally:
            logging.info("set add method function execution completed")
        return self.set_items
        
        
        