# 가변 인자 (*args, **kwargs)
def sum_all(*args):
    return sum(args)


print(sum_all(1, 2, 3, 4))  # 10


def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


show_info(name="Yuju", age=21, hobby="Coding")
