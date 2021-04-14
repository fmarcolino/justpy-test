import justpy as jp


def my_click(self, msg):
    self.text = 'I was clicked'


def handling_events_01():
    wp = jp.WebPage()
    d = jp.Div(
        text='Not clicked yet',
        a=wp,
        classes='w-48 text-xl m-2 p-1 bg-blue-500 text-white'
    )
    d.on('click', my_click)
    return wp