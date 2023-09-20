class Array_count:
    def __init__(self, m, array) -> None:
          self.m = m
          self.array = array

    def frequency_array(self):        
        count = {}
        list = []        
        for i in array:
            count[i] = count.get(i, 0)+1
        
        for i in range(1, m+1):
            list.append(count.get(i,0))
            
        for i in list:
            print(i)


n,m = map(int, input().split())
array = list(map(int, input().split()))
result = Array_count(m,array)
result.frequency_array()



# def frequency_array(m,array):
#     count = {}
#     list = []
#     for i in array:
#         count[i] = count.get(i, 0)+1
    
#     for i in range(1, m+1):
#         list.append(count.get(i,0))
#     return list  




# n,m = map(int, input().split())

# array = list(map(int, input().split()))

# ans = frequency_array(m,array)
# for i in ans:
#     print(i)

