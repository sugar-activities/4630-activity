from sugar.activity import activity

class vp(vonskeetproductions)Activity(activity.Activity):
    '''
    The base class for the vp (vonskeet productions) activity.
    '''
    
    def __init__(self, handle):
        activity.Activity.__init__(self, handle)
        
    def write_file(self, file_path):
        '''
        Implement this method to save your activity's state.
        '''
        raise NotImplementedError
    
    def read_file(self, file_path):
        '''
        Implement this method to resume state saved in write_file().
        '''
        raise NotImplementedError
