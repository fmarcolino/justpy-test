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


def my_click_02(self, msg):
    self.text = 'I was clicked'
    print(msg.event_type)
    print(msg['event_type'])
    print(msg)


def handling_events_02():
    wp = jp.WebPage()
    d = jp.P(
        text='Not clicked yet',
        a=wp,
        classes='text-xl m-2 p-2 bg-blue-500 text-white'
    )
    d.on('click', my_click_02)
    return wp
