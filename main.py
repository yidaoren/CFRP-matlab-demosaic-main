import matlab.engine
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    eng = matlab.engine.start_matlab()
    # 路径定义为成matlab中的cell模式

    # folder = eng.cell({'TSRnewshifei_1'})

    # 直接通过python定义也可以，原始图像路径
    folder = {'TSRnewshifei_1'}

    # 调用MATLAB函数
    result = eng.read_and_save_pol_imgs_func(folder)
    print(result)  # 输出：2.0


