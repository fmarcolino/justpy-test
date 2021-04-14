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


def my_click_03(self, msg):
    print(msg)
    self.text = 'I was clicked'


def handling_events_03():
    wp = jp.WebPage()
    wp.debug = True
    d = jp.Div(
        text='Not clicked yet',
        a=wp,
        classes='w-48 text-xl m-2 p-1 bg-blue-500 text-white'
    )
    d.on('click', my_click_03)
    d.additional_properties = [
        'screenX',
        'pageY',
        'altKey',
        'which',
        'movementX',
        'button',
        'buttons'
    ]
    return wp


def my_click_04(self, msg):
    self.text = 'I was clicked'
    self.set_class('bg-blue-500')

def my_mouseenter(self, msg):
    self.text = 'Mouse entered'
    self.set_class('bg-red-500')

def my_mouseleave(self, msg):
    self.text = 'Mouse left'
    self.set_class('bg-teal-500')


def handling_events_04():
    wp = jp.WebPage()
    d = jp.Div(
        text='Not clicked yet',
        a=wp,
        classes='w-64 text-2xl m-2 p-2 bg-blue-500 text-white',
        click=my_click_04,
        mouseenter=my_mouseenter,
        mouseleave=my_mouseleave
    )
    return wp
