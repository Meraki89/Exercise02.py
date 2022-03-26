import copy


def count_integer(numbers, integer):
    count = int(0)
    for item in numbers:
        if integer not in numbers:
            count = 42
        if item == integer:
            count += 1
    return int(count)


def list_func(numbers, integer):
    print(f"Original list: {numbers}")

    rep_lst = [6 if item == integer else item for item in numbers]
    new_lst = copy.deepcopy(rep_lst)

    new_lst.reverse()
    print(f"Reversed list: {new_lst}")

    if integer in numbers:
        return rep_lst
    else:
        return []


def compare_lists(list1, list2):
    common = [e for e in list1 if e in list2]
    final = []
    [final.append(e) for e in common if e not in final]
    return final


def remove_duplicates(lst):
    print(f"Original list: {lst}")
    result = []
    [result.append(e) for e in lst if e not in result]
    print(f"List without duplicates: {result}")
    return result


def dict_func(dictionary):
    dictionary2 = copy.deepcopy(dictionary)
    a = dictionary.setdefault("Type", "unknown type")
    b = dictionary.setdefault("Brand", "unknown brand")
    c = dictionary.setdefault("Price", "unknown price")
    print(f"You have a {a} from {b} that costs {c} money.")
    default_os = dictionary2.setdefault("OS", "Linux")
    print(f"Your operating system is {default_os}")
    print(dictionary2)
    return dictionary2
