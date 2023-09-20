# class Book:
#     def __init__(self, name) -> None:
#         self.name = name

#     def read(self):
#         # raise NotImplementedError
#         print('Read this vector chapter')


# class Physics(Book):
#     def __init__(self, name, lab) -> None:
#         self.lab = lab
#         super().__init__(name)

# topon = Physics('topon', True)
# print(issubclass(Physics, Book))
# print(isinstance(topon, Physics))
# print(isinstance(topon, Book))

# topon.read()
# # print(topon.read())

cnt = {}
i = 1
if i not in cnt:
    cnt[i] = 1
else:
    cnt[i] += 1

print(cnt)