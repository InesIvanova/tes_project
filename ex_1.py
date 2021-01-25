def convert_iterable_to_absolute(nums_list):
    result = list(map(lambda x: abs(x), nums_list))
    return result


nums = map(lambda el: float(el), input().split())
print(convert_iterable_to_absolute(nums))