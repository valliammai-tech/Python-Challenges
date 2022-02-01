import logging
logging.basicConfig(filename='list.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class InvalidList(Exception):
    logging.warning("InvalidList Exception is defined")
class list_list:
    def __init__(self,l):
        self.l=l
        logging.info("list provided is: {}".format(l))
        try:
            if type(self.l) != list:
                raise InvalidList
        except InvalidList:
            logging.error("invalid list type")
        except Exception as e:
            logging.error(e)
    
    def list_append(self,value):
        logging.info("list_append with value {} to append returns {}".format(value,self.l+[value]))
        return self.l+[value]
    
    def list_copy(self):
        logging.info("list copied as {}".format(self.l))
        return self.l
    
    def list_count(self):
        logging.info("list_count returns {}".format(len(self.l)))
        return len(self.l)
    
    def list_extend(self,value):
        logging.info("value passed to extend list is : {}".format(value))
        try:
            if type(value) == list or type(value)==tuple:
                for i in value:
                    self.l=self.l+[i]
        except Exception as e:
            logging.error("Error occurred in list_extend method for list {}".format(self.l))
            logging.error(e)
        logging.debug("list_extend output is {}".format(self.l))
        return self.l
    
    def list_index(self,value):
        '''Returns the index of the first element with the specified value'''
        logging.info("value passed to get index is: {}".format(value))
        try:
            if value not in self.l:
                logging.warning("invalid value {} that does not exists in dictionary is passed".format(value))
                index=''
            for ind,val in enumerate(self.l):
                if val==value:
                    index=ind
                    break
        except Exception as e:
            logging.error("Error occurred in list_index method call for list {}".format(self.l))
            logging.error(e)
        return index
    
    def list_insert(self,index_pos,value_to_insert):
        '''
        Adds an element at the specified position
        '''
        l=[]
        logging.info("Position {} and Value to insert {} are passed to list_insert method".format(index_pos,value_to_insert))
        try:
            for ind,val in enumerate(self.l):
                if ind==index_pos:
                    l.append(value_to_insert)
                    l.append(val)
                if ind!=index_pos:
                    l.append(val)
            if index_pos>=len(self.l):
                l.append(value_to_insert)
            if l!=[]:
                self.l=l
        except Exception as e:
            logging.error("Error occurred in list_insert method call for list {}".format(self.l))
            logging.warning(e) 
        logging.info("list_insert method call returns {}".format(self.l))  
        return self.l
    
    def list_pop(self,index_pos_to_pop):
        '''
        The pop() method removes the element at the specified position.
        '''
        logging.debug("Index Position to pop or remove value for list_pop method call is {}".format(index_pos_to_pop))
        l=[]
        try:
            if index_pos_to_pop >= len(self.l):
                raise IndexError
            for ind,val in enumerate(self.l):
                if ind!=index_pos_to_pop:
                    l.append(val)
        except IndexError:
            logging.error('pop index out of range for list_pop method call with index position to pop {}'.format(index_pos_to_pop))
        except Exception as e:
            logging.error('Error has occurred in list_pop method call for list {}'.format(self.l))
        if l!=[]:
            self.l=l
        logging.info("list_pop method returns {}".format(self.l))
        return self.l
        
    def list_remove(self,value_to_remove):
        '''Removes the first item with the specified value'''
        l=[]
        logging.info("value to remove {} is passed to list_remove method call for list {}".format(value_to_remove,self.l))
        try:
            if value_to_remove not in self.l:
                raise ValueError
            for val in self.l:
                if val!=value_to_remove:
                    l.append(val)
            if l!=[]:
                self.l=l
        except ValueError:
            logging.error("list.remove(x): x not in list for value {} from list {} in list_remove method call".format(value_to_remove,self.l))
        except Exception as e:
            logging.warning("error occurred in list_remove method call for list {}".format(self.l))
            logging.error(e)
        logging.info("list_remove method call returns {}".format(self.l))
        return self.l
    
    def list_reverse(self):
        logging.info("reversed list is {} for list {}".format(self.l[::-1],self.l))
        return self.l[::-1]
    
    def list_sort(self,reverse_key=False):
        '''
        The sort() method sorts the list ascending by default.
        list.sort(reverse=True|False, key=myFunc)
        Parameter	Description
        reverse	Optional. reverse=True will sort the list descending. Default is reverse=False
        key	Optional. A function to specify the sorting criteria(s)
        '''
        res=None
        try:
            if reverse_key:
                res=(sorted(self.l))[::-1]
            else:
                res=sorted(self.l)
        except Exception as e:
            logging.error("Error occurred in list_sort method call for list {}".format(self.l))
        logging.info("list_sort method call returns {} for list {}".format(res, self.l))
        return res
    
    def list_clear(self):
        self.l=[]
        logging.warning("Oops! List got cleared off as it is requested!!")
        return self.l
                
            
                
                
            
            
            

            
                
    
    
    
    
            
        
    
    
    
        