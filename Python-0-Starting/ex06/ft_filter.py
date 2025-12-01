def ft_filter(funct, iter) -> any:
	if funct is None:
		return [x for x in iter if x]
	return [x for x in iter if funct(x)]

# def test_even(object: any) -> bool:
# 	if object % 2:
# 		return False
# 	return True

# def main():
# 	even = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# 	truefalse = [True, True, False, False, False, True, 0, 0, 1]

# 	print(f"Even list is now {ft_filter(test_even, even)}")
# 	print(f"truefalse list is now {ft_filter(None, truefalse)}")

# 	return 0


# if __name__ == "__main__":
# 	main()
