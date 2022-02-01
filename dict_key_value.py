import logging
logging.basicConfig(filename='dict.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
class InvalidDataType(Exception):
    logging.info("InvalidDataType Exception defined by developer")
    pass
class key_value:
    def __init__(self,d):
        self.d=d
        logging.info("dictionary passed for manipulation is {}.".format(self.d))
        try:
            if type(self.d) != dict:
                raise InvalidDataType
        except InvalidDataType:
            logging.error("dictionary passed is not valid. Please check..")
        except Exception as e1:
            logging.error(e1)
            
    def get_items(self):
        logging.debug("dictionary items identified as {}".format(self.d.items()))
        return self.d.items()

    def get_keys(self):
        logging.debug("dictionary keys identified as {}".format(self.d.keys()))
        return self.d.keys()

    def get_values(self):
        logging.debug("dictionary values identified as {}".format(self.d.values()))
        return self.d.values()

    def from_keys(self):
        '''
        The fromkeys() method returns a dictionary with the specified keys and the specified value.
        dict.fromkeys(keys, value)
        keys	Required. An iterable specifying the keys of the new dictionary
        value	Optional. The value for all keys. Default value is None
        '''
        d={}
        try:
            for k,v in self.d.items():
                if v:
                    d[k]=v
                else:
                    d[k]=None
        except Exception as e:
            logging.error(e)
        logging.debug("from_keys method returns {} for dictionary passed as {}".format(d,self.d))
        return d
    def get_value_of_userinput_key(self):
        '''
        The get() method returns the value of the item with the specified key.
        dictionary.get(keyname, value)
        Parameter	Description
        keyname	Required. The keyname of the item you want to return the value from
        value	Optional. A value to return if the specified key does not exist.Default value None.
        '''
        a=eval(input("Enter keys existing in dictionary {} to get its values: ".format(self.d)))
        #eval function is very important here. Otherwise it will error out. 
        # Eval helps to consider using input with curly braces into valid python expression 
        # which is dictionary in this case. Otherwise it will consider as string.
        logging.info("inside get_value_of_userinput_key method. {} is the userinput received.".format(a))
        try:
            if a not in self.d:
                res="key {} does not exists in dictionary{}".format(a,self.d)
            else:
                res= self.d[a]
        except Exception as e:
            logging.warning(e)
        logging.debug("return value for get_value_of_userinput_key is: ".format(res))
        return res
    
    def insert_default(self,new_key_value_pair):
        '''
        The setdefault() method returns the value of the item with the specified key.
        If the key does not exist, insert the key, with the specified value, see example below
        dictionary.setdefault(keyname, value)
        Parameter	Description
        keyname	Required. The keyname of the item you want to return the value from
        value	Optional.
        If the key exist, this parameter has no effect.
        If the key does not exist, this value becomes the key's value.Default value None
        '''
        try:
            if type(new_key_value_pair) != dict:
                logging.error("invalid key value parameter passed to insert_default function {}".format(new_key_value_pair))
            search_key=list(new_key_value_pair.keys())[0] 
            logging.debug("search key identified for insert_default method is :".format(search_key))
        # new_key_value_pair.keys() gives TypeError as unhashable type: ‘dict_keys’. 
        # hence, [key] has to be converted to string as 'key' by typecasting to list and 
        # indexing 1st element. This step is very important to unpack dictionary key
            value_key=list(new_key_value_pair.values())[0]
            logging.debug("value key identified for insert_default method is :".format(value_key))
            if search_key not in self.d.keys():
                self.d[search_key]=value_key
        except Exception as e:
            logging.error(e)
        logging.info("insert_default returns {}".format(self.d[search_key]))
        return self.d[search_key]
    
    def dict_upd(self, new_kv_pair_upd):
        '''
        The update() method inserts the specified items to the dictionary.
        The specified items can be a dictionary, or an iterable object with key value pairs.
        dictionary.update(iterable)
        Parameter	Description
        iterable	A dictionary or an iterable object with key value pairs, that will be inserted to the dictionary
        '''
        try:
            if type(new_kv_pair_upd) != dict:
                logging.error("invalid data type passed to dict_upd method for new_kv_pair_upd parameter {}".format(new_kv_pair_upd))
            new_key=list(new_kv_pair_upd.keys())[0] # unpack dictionary key as explained in above method
            new_value=list(new_kv_pair_upd.values())[0] # unpack dictionary value as explain in above method
            self.d[new_key]=new_value
        except Exception as e:
            logging.error(e)
        logging.debug("dict_upd method returns {}".format(self.d))
        return self.d
    
    def dict_copy(self):
        '''The copy() method returns a copy of the specified dictionary.
        dictionary.copy()  
        No parameters        
        '''
        x=self.d
        logging.info("copied value is {} returned by dict_copy method".format(x))
        return x
    
    def dict_pop(self, key_to_pop, default_value):
        '''
        The pop() method removes the specified item from the dictionary.
        The value of the removed item is the return value of the pop() method.
        dictionary.pop(keyname, defaultvalue)
        Parameter	Description
        keyname	Required. The keyname of the item you want to remove
        defaultvalue	Optional. A value to return if the specified key do not exist.If this parameter is not specified, and the no item with the specified key is found, an error is raised
        '''
        d={}
        res=''
        res1=''
        try:
            if key_to_pop not in self.d:
                res=default_value
            else:
                pop_value=self.d[key_to_pop]
                res="value of poped key {} is {}".format(key_to_pop, pop_value)
                logging.debug("res value from dict_pop method is : {}".format(res))
            for k,v in self.d.items():
                if key_to_pop != k:
                    d[k]=v
                self.d=d
                res1=" dict after pop of {} is {}".format(key_to_pop, self.d)
                logging.debug("res1 value from dict_pop method is: {}".format(res1))
        except Exception as e:
            logging.error(e)
        return res, res1
        
    def dict_popitem(self):
        '''
        The popitem() method removes the item that was last inserted into the dictionary. 
        In versions before 3.7, the popitem() method removes a random item.
        The removed item is the return value of the popitem() method, as a tuple.
        dictionary.popitem()
        No parameters
        '''
        d={}
        try:
            pop_key=list(self.d)[-1]
            pop_value=self.d[pop_key]
            res={pop_key:pop_value}
            logging.debug("res value from dict_popitem method is: {}".format(res))
            valid_keys=list(self.d)[:-1]
            logging.debug("valid_keys from dict_popitem method is: {}".format(valid_keys))
            for i in valid_keys:
                value=self.d[i]
                logging.debug("value from dict_popitem method is: {}".format(value))
                d[i]=value
                logging.debug("d value from dict_popitem method is: {}".format(d))
            if d != {}:
                self.d=d
        except Exception as e:
            logging.error(e)
            logging.warning("Above error occurred in dict_popitem method call")
        logging.debug("dict_popitem method returns {} and {}".format(res,self.d))
        return res, self.d
    
    def dict_clear(self):
        '''
        The clear() method removes all the elements from a dictionary.
        dictionary.clear()
        No parameters
        '''
        self.d={}
        logging.warning("dictionary is cleared now as requested!!")
        return self.d
    
    
        
            
                
            
        
        
        
        
        
        
        
    
    


            
             