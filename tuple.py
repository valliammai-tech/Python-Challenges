import logging
logging.basicConfig(filename='tuple.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class InvalidTupleError(Exception):
    logging.warning("Invalid tuple data type exception defined")

class InvalidTupleIndex(Exception):
    logging.warning("Invalid tuple index exception defined")

class tuple_t:
    def __init__(self,t):
        self.t=t
        logging.info("tuple is {}".format(self.t))
        try:
            if type(self.t) != tuple:
                raise InvalidTupleError
        except InvalidTupleError:
            logging.critical('Element passed to class tuple_t is not a tuple. It is {}'.format(self.t))
        except Exception as e:
            logging.error('Error occurred in init method of class tuple_t')
            logging.error(e)
            
    def tuple_min(self):
        logging.debug("tuple_min method returns {}".format(self.t)[0])
        return sorted(self.t)[0]
    
    def tuple_max(self):
        logging.debug("tuple_max method returns {}".format(self.t)[-1])
        return sorted(self.t)[-1]
    
    def tuple_len(self):
        count=0
        try:
            for i in self.t:
                count=count+1
        except Exception as e:
            logging.warning("Error occurred in tuple_len method call")
            logging.error(e)
        logging.info("tuple_len method call returns {}".format(count))
        return count
    
    def tuple_count(self,value):
        count=0
        logging.info("value to be counted in list {} is {}".format(self.t,value))
        try:
            if value not in self.t:
                logging.warning("value {} passed to tuple_count function does not exists in tuple {}".format(value,self.t))
            for i in self.t:
                if i==value:
                    count=count+1
        except Exception as e:
            logging.warning("Error occurred in tuple_count method call for tuple {}".format(self.t))
            logging.error(e)
        logging.info("tuple_count method call with value {} and tuple {} returns {}".format(value,self.t,count))
        return count
    
    def tuple_index(self,search_value):
        '''
        The index() method finds the first occurrence of the specified value.
        The index() method raises an exception if the value is not found.
        '''
        logging.info("search key passed to tuple_index function call is {} for tuple {}".format(search_value,self.t))
        res=None
        try:
            if search_value not in self.t:
                raise InvalidTupleIndex
            for ind,val in enumerate(self.t):
                if val==search_value:
                    res=ind
                    break
        except InvalidTupleIndex:
            logging.error('search key {} passed to tuple_index function call does not exists in tuple {}'.format(search_value,self.t))
        except Exception as e:
            logging.warning("Error occurred in tuple_index function call for tuple {}".format(self.t))
            logging.error(e)
        logging.info("tuple_index function call with search key as {} for tuple {} returns {}".format(search_value,self.t,res))
        return res
        
        
    
        
        