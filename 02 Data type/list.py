#Student marks manager
marks=[78,45,89,32,67]
print("All marks:",(marks))
print("First marks:",marks[0])
print("Last marks:",marks[-1])
marks[2]=95
print("After modifiaction :",marks)
marks.append(72)
print("After adding:",marks)
marks.remove(32)
print("After removing:",marks)
marks.sort()
print("Sorted marks:",marks)