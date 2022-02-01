import logging

logging.basicConfig(filename='set.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
class set_diff:
    def __init__(self,set1,set2):
        self.set1=set1
        self.set2=set2
        logging.debug("set1 is {} and set2 is {}".format(set1,set2))
    def find_set_diff(self):
        di=[]
        try:
            for i in self.set1:
                if i not in self.set2:
                    di.append(i)
        except Exception as e:
            logging.error(e)
        else:
            logging.info("set difference is {}".format(set(di)))
        return set(di)
    def set_diff_upd(self):
        '''
        SET inbuilt methods re-creation with user defined functions
        The difference_update() method removes the items that exist in both sets.
        The difference_update() method is different from the difference() method, 
        because the difference() method returns a new set, without the unwanted items, and 
        the difference_update() method removes the unwanted items from the original set.
        '''
        self.set1=self.find_set_diff()
        logging.info("set difference update is {}".format(self.set1))
        return self.set1
    def set_symmetric_diff(self):
        '''
        The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.

        Meaning: The returned set contains a mix of items that are not present in both sets.
        '''
        s=self.find_set_diff()
        di=[]
        try:
            for i in self.set2:
                if i not in self.set1:
                    di.append(i)
        except Exception as e:
            logging.error(e)
        else:
            logging.info("set symmetric difference is {}".format(set(list(s)+di)))
        return set(list(s)+di)
    
    def set_symmetric_diff_upd(self):
        '''
        Remove the items that are present in both sets, AND insert the items that is not present in both sets
        '''
        s=self.set1
        upd=self.set_diff_upd()
        di=[]
        try:
            for i in self.set2:
                if i not in s:
                    di.append(i)
        except Exception as e:
            logging.error(e)
        else:
            logging.info("set symmetric difference update is {}".format(set(list(upd)+di)))
        return set(list(upd)+di)
        
            