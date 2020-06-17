#Q1
"""
def group_by_owners(files):
    owners = {}
    for key in files:
        if files[key] in owners.keys():
            owners[files[key]].append(key)
        else:
             owners[files[key]] = [key]   
    return owners

if __name__ == '__main__':
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }    
    print(group_by_owners(files))
"""


"""
Implement the IceCreamMachine's scoops method so that it returns all combinations of one ingredient and one topping. 
If there are no ingredients or toppings, the method should return an empty list.

For example, IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops()
 should return [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']].
"""

"""
class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        result = []
        for i in self.ingredients:
            for k in self.toppings:
                result.append([i, k])
        return result        


if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
    """

 
       

#            
def count_numbers(sorted_list, less_than): 
    less_amount = 0
    i = 0
    for sorted_list[i] in sorted_list:
        if sorted_list[i] < less_than:
            less_amount +=1
            print("gone through", sorted_list[i])
            print("found,", less_amount)
        if 4 in sorted_list:
            print("contains less than") 
        if 4 not in sorted_list:
            print("does not contain less than")   
           # print(f'{less_than}')    test 
    return less_amount      

     
if __name__ == '__main__':
     sorted_list = [1,3,5,7]
     print(count_numbers(sorted_list,4))#needs to print 2   
     