__author__='Ritik Rizwani'
__version__='1.0'



def count_executions(func):
    def execute(*args,**kwargs):
        
        val=func(*args,**kwargs)
        execute.calls+=1
        print('Number of times function called: %s' %execute.calls)
        
        return val
    execute.calls=0
    return execute
class Execution:
    @count_executions
    def add_triplet(self,nums):
        sum=0
        for i in nums:
            for j in nums:
                for k in nums:
                    sum+=i+j+k
        return sum
    @count_executions    
    def add(self,nums):
        sum=0
        for i in nums:
            sum+=i
        return sum

    

if __name__=='__main__':
    obj=Execution()
    
    print(obj.add_triplet([5,4,6,7,8,9,5,6,5,6,5,6,5,65,6,5,6,5,65,6,9,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]))
    print(obj.add_triplet([5,4,6,7,8,9,5,6,5,6,5,6,5,65,6,5,6,5,65,6,9,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]))
    print(obj.add_triplet([5,4,6,7,8,9,5,6,5,6,5,6,5,65,6,5,6,5,65,6,9,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]))
    print(obj.add([5,4,6,7,8,9,5,6,5,6,5,6,5,65,6,5,6,5,65,6,9,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]))
    print(obj.add([5,4,6,7,8,9,5,6,5,6,5,6,5,65,6,5,6,5,65,6,9,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]))
   

