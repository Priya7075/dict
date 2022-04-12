# book={
# 1: "python programming",
# 2: 'core python programming',
# 3.4: 'Advance python programming'    
# }
# print(book[3.4])#'Advance python programming'
# print(book[10])#keyError:10
# h={1:" ",2: "mama", 3: 7, 4: 6.2,
# 5: [1,4], 6: (4,3), 7: {1,2},
# 8: {3: "indu"}}
# print(h[1],type(h[1]))#str
# print(h[2],type(h[2]))#str "mama"
# print(h,type(h))#{1: ' ',2:'mama', 3: 7, 4: 6.2, 5:[1,4], 6: (4,3), 7:{1,2},8: {3: 'indu'}}
# print(h.keys())#([1,2,3,4,5,6,7,8])
# print(h.values())#(['','mama',7,6.2,[1,4],(4,3),{1,2},{3: 'indu'}])
# print(h.items())#([(1,' '), (2, 'mama'), (3,7), (4,6.2), (5,[1,4]),(6,(4,3)),(7,{1,2}),(8,{3: 'indu'})])
# h={1:"",2: "vip", 3: 7, 4: 6.2,
# 5: [1,4], 6: (4,3), 7: {1,2}, 8:{3:"indu"}}
# h.clear()
# print(h)#{}
# a=[101,102,103,104,105]
# b=dict.fromkeys(a)#{101: NOne, 102:None, 103:None, 104:None, 105:None}
# print(b,type(b))
# print(dict.fromkeys(a,'pass'))#{101: 'pass', 102: 'pass', 103: 'pass', 104: 'pass', 105: 'pass'}
# h={1:" ", 2: "indu", 3: 7, 4:6.2,
# 5: [1,4], 6: (4,3), 7: {1,2}, 8: {3: "mama"} }
# print(h.get(2))#'indu'
# print(h[2])#indu
# h.pop(6)
# print(h)#{1: ' ', 2: 'indu', 3: 7, 4: 6.2, 5: [1, 4], 7: {1, 2}, 8: {3: 'mama'}}
# h.popitem()
# print(h)#{1: ' ', 2: 'indu', 3: 7, 4: 6.2, 5: [1, 4], 7: {1, 2}}
# h={1:"", 2:"python", 3: 7, 4: 6.2,
# 5: [1,4], 6: (4,3), 7: {1,2}, 8: {3: " indu"}}
# h.update({8: 'core python'})
# print(h)#{1: '', 2:'python', 3: 7, 4: 6.2, 5:[1,4], 6:(4,3), 7:{1,2}, 8: 'core python'}
# h.update({9: 'adv python'})
# print(h)#{1: '', 2:'python', 3: 7, 4: 6.2, 5:[1,4], 6:(4,3), 7:{1,2}, 8: 'core python' ,9: 'adv python'}
# h={1:"", 2:"python", 3: 7, 4: 6.2,
# 5: [1,4], 6: (4,3), 7: {1,2}, 8: {3: " indu"}}
# h.setdefault(8, 'devops')
# print(h)#{1: '', 2: 'python', 3: 7, 4: 6.2, 5: [1, 4], 6: (4, 3), 7: {1, 2}, 8: {3: ' indu'}}
# h.setdefault(10, 'devops')
# print(h)#{1: '', 2: 'python', 3: 7, 4: 6.2, 5: [1, 4], 6: (4, 3), 7: {1, 2}, 8: {3: ' indu'}, 10: 'devops'

