import logging
logging.basicConfig(filename='set.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
class set_venn:
    def __init__(self, set1, set2):
        self.set1=set1
        self.set2=set2
        logging.info("set1 {} and set2 {} are the values passed to the set_venn class".format(self.set1,self.set2))
    def set_update(self):
        '''
        The update() method updates the current set, by adding items from another set 
        (or any other iterable).
        If an item is present in both sets, only one appearance of this item will be present in the 
        updated set.
        '''
        logging.info("set_update function returns {}".format(set(list(self.set1)+list(self.set2))))
        return set(list(self.set1)+list(self.set2))
    def set_union(self,*args):
        '''
        The union() method returns a set that contains all items from the original set, and all items from the specified set(s).
        You can specify as many sets you want, separated by commas.
        It does not have to be a set, it can be any iterable object.
        If an item is present in more than one set, the result will contain only one appearance of this item.
        '''
        logging.info("Additional arguments passed to set_union method is: {}".format(args))
        try:
            a=self.set_update()
            a=list(a)
            for i in range(len(args)):
                res=a+(list(args[i]))
        except Exception as e:
            logging.Error(e)
        else:
            logging.debug("set union function under set venn class returns: {}".format(set(res)))
        return set(res)
    def set_intersection(self,*args):
        '''
        The intersection() method returns a set that contains the similarity between two or more sets.
        Meaning: The returned set contains only items that exist in both sets, or in all sets 
        if the comparison is done with more than two sets.
        '''
        res=[]
        logging.info("Additional args passed to set_intersection function: {}".format(args))
        try:
            for i in range(len(args)):
                for j in args[i]:
                    if ((j in self.set1) and (j in self.set2)):
                        res.append(j)
        except Exception as e:
            logging.error(e)
        else:
            logging.debug("set_intersection function returns {}".format(set(res)))
        return set(res)
    def set_intersection_upd(self,*args):
        '''
        The intersection_update() method removes the items that is not present in both sets 
        (or in all sets if the comparison is done between more than two sets).
        The intersection_update() method is different from the intersection() method, 
        because the intersection() method returns a new set, without the unwanted items, 
        and the intersection_update() method removes the unwanted items from the original set.
        '''
        self.set1=self.set_intersection(*args)
        logging.info("set_intersection_upd of self.set1 is: {}".format(self.set1))
        return self.set1
    
    def set_disjoint(self):
        '''
        The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
        '''        
        try:
            for i in self.set1:
                if i in self.set2:
                    return False
                else:
                    return True
        except Exception as e:
            logging.error(e)
        else:
            logging.debug("set_disjoint function completed. verify return value.")
    
    def set_subset(self):
        '''
        The issubset() method returns True if all items in the set exists in the specified set, otherwise it retuns False.
        '''
        l=[]
        try:
            for i in self.set1:
                if i in self.set2:
                    l.append(True)
                else:
                    l.append(False)
            if all(l):
                logging.info("set_subset method return True for sets {} and {}".format(self.set1,self.set2))
                return True
            else:
                logging.info("set_subset method return False for sets {} and {}".format(self.set1,self.set2))
                return False
        except Exception as e:
            logging.warning(e)
        
    def set_superset(self):
        '''
        The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it retuns False.
        issubset() method returns true if an entire set is inside some other set or not, whereas issuperset() method returns true if a set contains some other sets entire item.
        '''
        l=[]
        try:
            for i in self.set2:
                if i in self.set1:
                    l.append(True)
                else:
                    l.append(False)
            if all(l):
                logging.info("set_superset method return True for sets {} and {}".format(self.set1,self.set2))
                return True
            else:
                logging.info("set_superset method return False for sets {} and {}".format(self.set1,self.set2))
                return False
        except Exception as e:
            logging.error(e)
        
    
        
    
        
    