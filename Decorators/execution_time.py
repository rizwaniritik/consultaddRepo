__author__='Ritik Rizwani'
__version__='1.0'


from datetime import datetime
def execution_time(func):
    def execute(*args,**kwargs):
        start_time=datetime.now()
        val=func(*args,**kwargs)
        
        end_time=datetime.now()
        diff= (end_time-start_time).total_seconds()
        print('Time Taken:%s seconds' %diff)
        return val
    return execute
class Execution:
    @execution_time
    def add_triplet(self,nums):
        sum=0
        for i in nums:
            for j in nums:
                for k in nums:
                    sum+=i+j+k
        return sum

    

if __name__=='__main__':
    obj=Execution()
    print(obj.add_triplet([5,4,6,7,8,9,5,6,5,6,5,6,5,65,6,5,6,5,65,6,9,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]))

