import justpy as jp


def hello_world():
    wp = jp.WebPage()
    d = jp.Div(text='Hello world!')
    wp.add(d)
    return wp


def hello_world_02():
    wp = jp.WebPage()
    my_paragraph_design = (
        "w-64 bg-blue-500 m-2 hover:bg-blue-700 "
        "text-white font-bold py-2 px-4 rounded"
    )

    for i in range(1,11):
        jp.P(text=f'{i}) Hello World!', a=wp, classes=my_paragraph_design)
    return wp
